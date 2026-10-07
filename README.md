# Eminus Mobile build automation

This repository intentionally contains only automation. GitHub Actions fetches the upstream Eminus `mc/1.21` source instead of requiring the full source tree to be uploaded here.

The workflow prepares the Fabric dependency pins and builds the upstream source. The resulting compiler output is uploaded as an artifact so the remaining 1.21.11 API migration can be patched from real compiler errors rather than guessed.
