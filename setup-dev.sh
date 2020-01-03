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
echo "[+] Installing virtualenv"
pip install virtualenv --user
echo "[+] Creating venv folder"
python -m venv venv
echo "[+] Installing dependencies"
./venv/bin/pip install chatterbot fbchat-asyncio discord praw requests googletrans chatterbot.corpus
printf "#!/bin/bash\n./venv/bin/python disc.py" > run.sh
echo "[+] Done"
