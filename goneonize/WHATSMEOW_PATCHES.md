# WhatsApp Patches for Vendored Dependencies

This document tracks patches applied to vendored whatsmeow code to fix bugs not yet merged upstream.

## Patch 1: Group Creation Field - Optional Instead of Required

### Issue
WhatsApp's API no longer consistently returns the `creation` timestamp field for group metadata. When this field is missing, whatsmeow's parser crashes with error:
```
Error parsing group <jid>: [didn't find required attribute 'creation']
```

This affects `GetJoinedGroups()` and causes groups to be skipped, resulting in incomplete group listings.

### Root Cause
File: `vendor/go.mau.fi/whatsmeow/group.go:707`

The parser uses `UnixTime()` which requires the field to exist:
```go
group.GroupCreated = ag.UnixTime("creation")  // Panics if field missing
```

### Fix
Change to `OptionalUnixTime()` to handle missing field gracefully:
```go
group.GroupCreated = ag.OptionalUnixTime("creation")  // Returns zero time if missing
```

### Precedent
This follows the same pattern used for other optional group fields (commit `38f9aaa`, Sept 30, 2025):
- `group.Name = ag.OptionalString("subject")`
- `group.NameSetAt = ag.OptionalUnixTime("s_t")`

### When to Apply
- After running `go mod vendor` in `goneonize/` directory
- Before building the shared library (`.so`/`.dll`/`.dylib`)
- Automated via `apply-patches.sh` script

### Upstream Status
- **Not fixed in upstream whatsmeow** as of December 2, 2025
- Issue/PR to be submitted to https://github.com/tulir/whatsmeow
- This patch can be removed once upstream fix is merged and neonize updates whatsmeow dependency

### Testing
Verify the fix by:
1. Calling `GetJoinedGroups()` for an account with groups
2. Checking that all groups are returned (no "Error parsing group" warnings)
3. Verifying `GroupCreated` field is populated when available, zero time when missing

---

## Patch 2: Link Code Pairing Nonce - String Instead of Byte Slice

### Issue
Pair code linking fails with the upstream implementation. Testing showed that changing the nonce type from `[]byte{0}` to `"0"` (matching Baileys library implementation) makes pairing work reliably.

### Root Cause
File: `vendor/go.mau.fi/whatsmeow/pair-code.go:120`

The current implementation uses a byte slice:
```go
{Tag: "link_code_pairing_nonce", Content: []byte{0}}
```

This prevents successful pairing in practice.

### Fix
Change to string type (matching Baileys JavaScript implementation):
```go
{Tag: "link_code_pairing_nonce", Content: "0"}
```

### Rationale
- Baileys library (https://github.com/WhiskeySockets/Baileys) uses string `"0"` and works
- Extensive testing (one week) showed pairing fails with `[]byte{0}` but succeeds with `"0"`
- WhatsApp protocol appears to expect string type for this field

### When to Apply
- After running `go mod vendor` in `goneonize/` directory
- Before building the shared library (`.so`/`.dll`/`.dylib`)
- Automated via `apply-patches.sh` script

### Upstream Status
- **Rejected by upstream maintainer** as of November 16, 2024
- PR: https://github.com/tulir/whatsmeow/pull/1003
- Maintainer claims `[]byte{0}` is correct, suggested version mismatch
- However, real-world testing proves string type works and byte slice fails
- This patch should remain until upstream reconsiders or provides working alternative

### Testing
Verify the fix by:
1. Attempting pair code linking with a fresh WhatsApp account
2. Confirming pairing completes successfully
3. Verifying the paired device appears in WhatsApp linked devices

---

## Patch 3: Add BuildClearChat Function - Clear Messages Without Deleting Chat

### Issue
WhatsApp's "Clear Chat" functionality (removing all messages while keeping the chat in the conversation list) is not available in upstream whatsmeow. The library has `BuildDeleteChat` but not `BuildClearChat`.

### Root Cause
File: `vendor/go.mau.fi/whatsmeow/appstate/encode.go`

Upstream whatsmeow does NOT have a `BuildClearChat` function. We need to add it.

### Fix
Add a new function `BuildClearChat` that uses `ClearChatAction` (which exists in whatsmeow's protobuf definitions) to clear all messages from a chat.

**Critical:** The index must have 4 elements per Baileys reference implementation:
```javascript
// Baileys (working implementation)
index: ['clearChat', jid, '1', '0'],  // 4 elements
```

- Element 1: `'clearChat'` - action type
- Element 2: JID - chat identifier
- Element 3: `'1'` - delete all messages (use `'0'` to keep starred messages)
- Element 4: `'0'` - required parameter

```go
func BuildClearChat(target types.JID, lastMessageTimestamp time.Time, lastMessageKey *waCommon.MessageKey) PatchInfo {
    // ... action setup ...
    return PatchInfo{
        Type: WAPatchRegular,
        Mutations: []MutationInfo{{
            Index:   []string{IndexClearChat, target.String(), "1", "0"},  // 4 elements required
            Version: 6,
            Value: &waSyncAction.SyncActionValue{
                ClearChatAction: action,
            },
        }},
    }
}
```

### When to Apply
- After running `go mod vendor` in `goneonize/` directory
- Before building the shared library (`.so`/`.dll`/`.dylib`)
- Automated via `apply-patches.sh` script

### Upstream Status
- **Not available upstream** - Feature addition, not a bug fix
- Consider submitting PR to https://github.com/tulir/whatsmeow after testing

### Testing
Verify the fix by:
1. Calling `clear_chat()` on a group or individual chat
2. Confirming no 409 Conflict error is returned
3. Confirming all messages are removed from the chat
4. Verifying the chat itself remains in the conversation list
