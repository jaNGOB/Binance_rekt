# Binance_rekt

Hello and welcome to the new Project :) 


Deployment on server:


1. install miniforge 
```
wget -N https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

bash Miniforge3-Linux-x86_64.sh -b -u -p ~/conda

source ~/conda/bin/activate
```
2. Install packages
```
conda install websocket-client  
pip install influx_line_protocol  
pip install pytz
sudo apt-get install tmux
sudo apt-get install docker.io
```
3. Clone this repository
```
git clone https://github.com/jaNGOB/Binance_rekt.git
```
4. Create a tmux window and deploy the questdb container. 
```
tmux
docker run -p 9000:9000 -p 9009:9009 questdb/questdb
```
5. Create another tmux window and start our program
```
tmux
python main.py
```

## tmux
To create a new tmux window: ```tmux```  
To leave the window:         ```Ctrl+B+D```  
To see existing windows:     ```tmux ls```  
To connect to a window (where x is the window number): ```tmux a -t x```

Good luck and have fun watching people loose money.
