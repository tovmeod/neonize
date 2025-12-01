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

echo "All patches applied successfully!"
