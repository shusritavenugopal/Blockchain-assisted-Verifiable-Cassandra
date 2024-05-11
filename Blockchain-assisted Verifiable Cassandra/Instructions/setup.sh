# Install pip3 for package management
sudo apt-get update
sudo apt-get install python3-pip
python3 -m pip install -U pip

# Install related packages
pip3 install cassandra-driver merkletools py-solc-x
pip3 install web3==5.31.4

# Create py file to run the codes
mkdir project3
cd project3
###  Upload all related files tto this folder ###

# Start ganache service in 2nd terminal
# Create a file to store nvm commands
touch ~/.bashrc
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash

# Activate the commands (need to run this command every time you login)
source ~/.bashrc
# install node 16.14.2 (which are supported by ganache)
nvm install 16.14.2
node -v

# Install the Solidity Compiler
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc
# Install ganache command line tool
npm install ganache --global
#Run ganache
ganache


# Start Cassandra service in 3rd terminal

For Cassandra Installation, please review project2 tutorial

# Stop existing Cassandra service if have any:
sudo service cassandra stop
sudo service cassandra start


# Run the program in the 1st terminal
python3 driver.py