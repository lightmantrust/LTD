# Regulator Quick-Start

1. Download latest PDF bundle (`regulatory-bundle-latest.pdf`) from [releases](https://github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/releases).  
2. Verify signature:  
   ```bash
   cosign verify-blob \
     --certificate-identity-regexp '.*lightmantrust.*' \
     --signature regulatory-bundle-latest.pdf.sig \
     regulatory-bundle-latest.pdf
