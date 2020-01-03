#!/bin/bash
echo "#     #           #####         
##   ## # #####  #     # #    # 
# # # # # #    #       # #   #  
#  #  # # #    #  #####  ####   
#     # # #####        # #  #   
#     # # #   #  #     # #   #  
#     # # #    #  #####  #    # "
echo "DEV setup script"
echo "Written by:
_  _ ____ _  _ ____ ____ ____ _  _ _    _ ____ ____ 
|_/  |__| |\ | |__| |__/ |___ |_/  |    | |___ |___ 
| \_ |  | | \| |  | |  \ |___ | \_ |___ | |    |___ 
                                                    "
if [ "$EUID" -ne 0 ]
  then echo "[!] Please run as root"
  exit
fi
PIP=pip
PYTHON=python
OS=$(awk -F= '/^NAME/{print $2}' /etc/os-release)
FOUND="false"
if [ "$OS" == "\"Ubuntu\"" ] || [ "$OS" == "\"Debian GNU/Linux\"" ] ; then
    echo "[i] Detected Debian or Ubuntu based system"
    apt-get update
    apt-get install python3-venv python3-pip python3 -y
    PIP=pip3
    PYTHON=python3
    FOUND="true"
fi
if [ "$OS" == "Fedora" ] ; then
    echo "[i] Detected Fedora based system"
    dnf update
    dnf install python pip
    FOUND="true"
fi
if [ "$FOUND" == "false" ] ; then
    echo "[!] Using unsupported distro! Install python3 and python3-pip and set aliases for them (python and pip) and then restart this script!"
fi
echo "[+] Installing virtualenv"
$PIP install virtualenv --user
echo "[+] Creating venv folder"
$PYTHON -m venv venv
echo "[+] Installing dependencies"
./venv/bin/pip install wheel
./venv/bin/pip install chatterbot fbchat-asyncio discord praw requests googletrans chatterbot.corpus
echo "[+] Creating run.sh file"
printf "#!/bin/bash\n./venv/bin/python disc.py" > run.sh
echo "[+] Done"
