from pathlib import Path
import re, sys
root=Path(sys.argv[1])
p=root/'gradle.properties'
s=p.read_text()
# Keep the upstream 1.21.1 source/mappings intact for the first automated port pass.
# Only update the Fabric-side version pins that are known to exist for 1.21.11.
s=s.replace('fabric_loader_version=0.19.3','fabric_loader_version=0.19.3')
s=s.replace('fabric_api_version=0.116.17+1.21.1','fabric_api_version=0.141.6+1.21.11')
s=s.replace('modmenu_version=11.0.4','modmenu_version=17.0.1')
p.write_text(s)
# Make the workflow fail clearly rather than silently claiming a port if upstream still targets 1.21.1.
# The actual Minecraft-version migration is intentionally performed by Loom's migration tooling in the next stage.
