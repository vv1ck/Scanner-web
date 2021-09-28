mno=$(whoami)
if [ $mno == root ]
  then
    python3 Scanner-web.py
else
    sudo python3 Scanner-web.py
fi
