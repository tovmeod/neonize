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

# Patch 2: REMOVED - was incorrectly changing []byte{0} to "0"
# The original []byte{0} is correct - it's a null byte nonce, not ASCII '0'

# Patch 3: REMOVED - BuildClearChat is now implemented in pure Python
# See neonize/client.py ChatSettingsStore.clear_chat and neonize/aioze/client.py
# This removes the maintenance burden of patching whatsmeow vendor code

echo "All patches applied successfully!"
