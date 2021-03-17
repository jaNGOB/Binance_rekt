# Binance_rekt

Hello and welcome to the new Project :) 


Deployment on server:


1. install miniforge 
```
get -N https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

bash Miniforge3-Linux-x86_64.sh -b -u -p ~/conda

source ~/conda/bin/activate
```
2. pip install packages
```
websocket_client  
influx_line_protocol  
pytz
```
5. 'git clone https://github.com/jaNGOB/Binance_rekt.git'

4. install tmux


Just run main.py and it will save the data of all people getting liquidated into QuestDB. 
This happens until you "CTRL+C" out of there.  
Good luck and have fun watching people loose money.
