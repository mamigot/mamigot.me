# # # # #
# CONFIGURATION: Debian 7.0 x64 ON DIGITALOCEAN
# # # # #

# Update the machine
sudo apt-get update
sudo apt-get upgrade

## http://stackoverflow.com/questions/19816275/no-acceptable-c-compiler-found-in-path-when-installing-python
sudo apt-get install build-essential


# Install Python from source
## Required packages
sudo apt-get install build-essential libncursesw5-dev libreadline-gplv2-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev

## https://docs.python.org/2/using/unix.html#building-python
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
tar -xvzf Python-2.7.9.tgz
cd Python-2.7.9/

./configure
make
make altinstall


# Python utilities
## pip
sudo apt-get install python-pip

## virtualenvwrapper
sudo pip install virtualenvwrapper
### Add the following to ~/.bashrc
### export WORKON_HOME=$HOME/.virtualenvs
### source /usr/local/bin/virtualenvwrapper.sh


# MongoDB
## http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get install -y mongodb-org


# Nginx
sudo apt-get install nginx
## sudo service nginx start
## sudo service nginx stop
## sudo service nginx restart




# # # # #
# USEFUL COMMANDS
# # # # #
#
# Remove package as well as its dependencies
## http://askubuntu.com/questions/443/how-to-remove-an-uninstalled-packages-dependencies
## sudo apt-get remove --auto-remove packagename
#
# Automatically answer 'Yes' when using apt-get install
## http://superuser.com/questions/164553/automatically-answer-yes-when-using-apt-get-install
## sudo apt-get -y install packagename
#
# Reveal VPS's IP address
## ifconfig eth0 | grep inet | awk '{ print $2 }'
