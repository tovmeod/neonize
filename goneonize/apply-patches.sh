#!/bin/bash
set -e

# Apply patches to vendored whatsmeow dependencies
# See WHATSMEOW_PATCHES.md for details

echo "Applying whatsmeow patches..."

# Check if vendor directory exists
if [ ! -d "vendor/go.mau.fi/whatsmeow" ]; then
    echo "Error: vendor/go.mau.fi/whatsmeow not found"
    echo "Run 'go mod vendor' first to create vendored dependencies"
    exit 1
fi

# Patch 1: Make group creation field optional
PATCH_FILE_1="vendor/go.mau.fi/whatsmeow/group.go"
if [ ! -f "$PATCH_FILE_1" ]; then
    echo "Error: $PATCH_FILE_1 not found"
    exit 1
fi

# Check if patch is already applied
if grep -q 'OptionalUnixTime("creation")' "$PATCH_FILE_1"; then
    echo "Patch 1 already applied to $PATCH_FILE_1"
else
    echo "Applying creation field patch to $PATCH_FILE_1..."
    sed -i 's/ag\.UnixTime("creation")/ag.OptionalUnixTime("creation")/g' "$PATCH_FILE_1"
    echo "✓ Patch 1 applied successfully"
fi

# Patch 2: Fix link code pairing nonce type
PATCH_FILE_2="vendor/go.mau.fi/whatsmeow/pair-code.go"
if [ ! -f "$PATCH_FILE_2" ]; then
    echo "Error: $PATCH_FILE_2 not found"
    exit 1
fi

# Check if patch is already applied
if grep -q 'Content: "0"' "$PATCH_FILE_2"; then
    echo "Patch 2 already applied to $PATCH_FILE_2"
else
    echo "Applying pair code nonce patch to $PATCH_FILE_2..."
    sed -i 's/Content: \[\]byte{0}/Content: "0"/g' "$PATCH_FILE_2"
    echo "✓ Patch 2 applied successfully"
fi

# Patch 3: Add BuildClearChat function for clearing chat messages
# Upstream whatsmeow does NOT have BuildClearChat - we must add it
# Uses 4-element index per Baileys: ['clearChat', jid, '1', '0']
PATCH_FILE_3="vendor/go.mau.fi/whatsmeow/appstate/encode.go"
if [ ! -f "$PATCH_FILE_3" ]; then
    echo "Error: $PATCH_FILE_3 not found"
    exit 1
fi

# Check if patch is already applied (with correct 4-element index)
if grep -q 'IndexClearChat, target.String(), "1", "0"' "$PATCH_FILE_3"; then
    echo "Patch 3 already applied to $PATCH_FILE_3"
else
    # Check if old broken patch exists (2-element index)
    if grep -q 'func BuildClearChat' "$PATCH_FILE_3"; then
        echo "ERROR: BuildClearChat exists with wrong index. Manual fix required."
        echo "Remove the existing BuildClearChat function and re-run this script."
        exit 1
    fi
    echo "Applying BuildClearChat patch to $PATCH_FILE_3..."
    cat >> "$PATCH_FILE_3" << 'BUILDCLEARCHAT_EOF'

// BuildClearChat builds an app state patch for clearing all messages in a chat.
// This removes messages from the chat but keeps the chat itself in the conversation list.
// Note: Upstream whatsmeow does NOT have this function - this is our patch.
func BuildClearChat(target types.JID, lastMessageTimestamp time.Time, lastMessageKey *waCommon.MessageKey) PatchInfo {
	if lastMessageTimestamp.IsZero() {
		lastMessageTimestamp = time.Now()
	}
	action := &waSyncAction.ClearChatAction{
		MessageRange: &waSyncAction.SyncActionMessageRange{
			LastMessageTimestamp: proto.Int64(lastMessageTimestamp.Unix()),
		},
	}
	if lastMessageKey != nil {
		action.MessageRange.Messages = []*waSyncAction.SyncActionMessage{{
			Key:       lastMessageKey,
			Timestamp: proto.Int64(lastMessageTimestamp.Unix()),
		}}
	}

	return PatchInfo{
		Type: WAPatchRegular,
		Mutations: []MutationInfo{{
			Index:   []string{IndexClearChat, target.String(), "1", "0"},
			Version: 6,
			Value: &waSyncAction.SyncActionValue{
				ClearChatAction: action,
			},
		}},
	}
}
BUILDCLEARCHAT_EOF
    echo "✓ Patch 3 applied successfully"
fi

echo "All patches applied successfully!"
