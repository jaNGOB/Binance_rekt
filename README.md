# Binance_rekt

Hello and welcome to Mission: "Geldverbrennung!"


Deployment on server:


1. install miniforge 
```
wget -N https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

bash Miniforge3-Linux-x86_64.sh -b -u -p ~/conda

source ~/conda/bin/activate
```
2. Install packages
```
conda install websocket-client pytz pandas tweepy  
pip install influx_line_protocol  
sudo apt-get install tmux docker.io
```
3. Clone this repository
```
git clone https://github.com/jaNGOB/Binance_rekt.git
```
4. Create a tmux window and deploy the questdb container. 
```
tmux
docker run -p 9009:9009 questdb/questdb
```
5. Update credentials.ini with your twitter api information and a desired database name.  
6. Create another tmux window and start our program
```
tmux
python main.py
```

## tmux
To create a new tmux window: ```tmux```  
To leave the window:         ```Ctrl+B``` then ```D```  
To see existing windows:     ```tmux ls```  
To connect to a window (where x is the window number): ```tmux a -t x```

Good luck and have fun watching people loose money.

To tweet out regularly our hourly findings, we use a CRON-job. To create a new CRON-job, ```crontab -e``` can be typed into the Terminal which will open a file.  
After the file is opened, the following line shoulb be added to the bottom of it.  
```
0 * * * * ~/conda/bin/python3.8 ~/Binance_rekt/twitter.py
```
