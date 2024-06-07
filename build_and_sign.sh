#!/usr/bin/env bash

python -m nuitka \
    --standalone \
    --macos-create-app-bundle \
    --macos-app-name="Hello Nuitka" \
    --company-name="Testing" \
    --macos-app-version="0.1" \
    --macos-signed-app-name="com.testing.hello-nuitka" \
    --macos-sign-identity=auto \
    --macos-sign-notarization \
    --assume-yes-for-downloads \
    --output-filename="hello_nuitka" \
    --macos-app-icon="resources/icon.icns" \
    --script-name=test_app.py

# zip the app
zip -r test_app.app.zip test_app.app
    
# send for notarization
xcrun notarytool submit \
    --wait \
    --apple-id $APPLE_ID \
    --password $TEST_APP_PASSWORD \
    --team-id $TEAM_ID \
    test_app.app.zip