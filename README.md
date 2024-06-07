Update: This worked randomly after a while. No idea why, but I'll leave it here as an example of a wxPython + Nuitka app that can be notarized.

# Nuitka macOS Notarization Test App

Minimal example test app to illustrate the issue with notarizing a Nuitka-compiled macOS app.

This repo contains the code as well as an invalid app bundle. Notarization failed with the following not very helpful response:

```json
{
  "logFormatVersion": 1,
  "jobId": "d105a269-fc84-43bb-bf04-3c835660c734",
  "status": "Invalid",
  "statusSummary": "Archive contains critical validation errors",
  "statusCode": 4000,
  "archiveFilename": "test_app.app.zip",
  "uploadDate": "2024-06-07T16:54:11.046Z",
  "sha256": "498b01cf5644c8a6ca11af5bc9a048ec1950723fe9fd54dcb2d2b79041725d8b",
  "ticketContents": null,
  "issues": [
    {
      "severity": "error",
      "code": null,
      "path": "test_app.app.zip/test_app.app/Contents/MacOS/hello_nuitka",
      "message": "The signature of the binary is invalid.",
      "docUrl": "https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/resolving_common_notarization_issues#3087735",
      "architecture": "arm64"
    }
  ]
}
```

Running the suggested debugging command `codesign -vvv --deep --strict` on the .app bundle gives the following output:

```shell
... a bunch of --validated/prepared lines ...
test_app.app: valid on disk
test_app.app: satisfies its Designated Requirement
```

The zip file should not need to be signed in addition to the .app, but signing the zip file doesn't change anything. 

## Steps to reproduce
This requires a paid Apple developer account and all the various hoops to set up a codesigning certificate and such.

1. Create a venv (I tested on both Python 3.10 and 3.12)
2. `pip install -r requirements.txt`
3. Define the following environment variables:
    1. `APPLE_ID` - your Apple ID (email address)
    2. `TEST_APP_PASSWORD` - an [app-specific password](https://support.apple.com/en-us/102654) generated for your Apple ID
    3. `TEAM_ID` - your Apple Developer Team ID
4. Run `./build_and_notarize.sh` to build the Nuitka app with code signing, zip it, then submit for notarization.