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
PATCH_FILE="vendor/go.mau.fi/whatsmeow/group.go"
if [ ! -f "$PATCH_FILE" ]; then
    echo "Error: $PATCH_FILE not found"
    exit 1
fi

# Check if patch is already applied
if grep -q 'OptionalUnixTime("creation")' "$PATCH_FILE"; then
    echo "Patch already applied to $PATCH_FILE"
else
    echo "Applying creation field patch to $PATCH_FILE..."
    sed -i 's/ag\.UnixTime("creation")/ag.OptionalUnixTime("creation")/g' "$PATCH_FILE"
    echo "✓ Patch applied successfully"
fi

echo "All patches applied successfully!"
