#!/usr/bin/python
import os

os.system("python3 -m venv mitt_prosjekt")
os.system("source mitt_prosjekt/bin/activate")
os.system("pip install -r req.txt")
os.system("deactivate")

os.system("touch runSC.sh")
os.system("chmod +x runSC.sh")
os.system("echo '#!/usr/bin/python \nsource mitt_prosjekt/bin/activate \npython joke.py \ndeactivate' > runSC.sh")
os.system("echo '\n \n'")
os.system("./runSC.sh")

#os.system("rm send.py")