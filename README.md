# ICT1002-HEHEXD

Map It! A web application written with Flask and analyzes pcap files to produce useful information :)

## Installation
```
git clone git@github.com:djmeowmix25/ICT1002-HEHEXD.git

cd ICT1002-HEHEXD
```
Note: Wireshark needs to be installed on your system for the web application to work.
### Linux/macOS
```
python3 -m virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt

./run.sh
```
### Windows
```
python3 -m virtualenv venv

.\venv\scripts\activate

pip3 install -r requirements.txt

./run_web_server.bat

```
### Please take note that it will take a long time if the pcap file is larger than 1MB.
