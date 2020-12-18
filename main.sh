sudo apt install python3 python3-pip unzip wget -y
python3 -m pip install setuptools
python3 -m pip install flask requests_html requests colorama
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngr*
chmod a=rwx ngr*
./ngrok authtoken 1lolTIS5NFdmO0puF7YIjrkJMpE_3qgbVEiPPWrDE9STfyWGY
#./ngrok http 1024
python3 main.py