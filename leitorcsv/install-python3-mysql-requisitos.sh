#!/bin/bash
sudo apt update
sudo apt install mysql-server -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 -y
sudo apt-get install python3-pip -y
pip install pandas
pip install pymysql
pip install sqlalchemy

sudo systemctl start mysql.service
