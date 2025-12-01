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
