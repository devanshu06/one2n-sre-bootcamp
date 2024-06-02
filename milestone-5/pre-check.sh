#!/bin/bash

command_exists() {
    command -v "$1" &> /dev/null
}

sudo apt-get update

if command_exists docker; then
    echo "Docker is already installed"
else
    echo "Docker is not installed. Installing Docker..."    
    # sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    # curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    # sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    # sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    echo "Docker installed successfully"
fi

if command_exists docker-compose; then
    echo "Docker Compose is already installed"
else
    echo "Docker Compose is not installed. Installing Docker Compose..."
    sudo apt-get install -y docker-compose 
    # DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*?(?=")')
    # sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    # sudo chmod +x /usr/local/bin/docker-compose
    echo "Docker Compose installed successfully"
fi

sudo usermod -aG docker vagrant

echo "Verifying Docker installation..."
docker --version
echo "Verifying Docker Compose installation..."
docker-compose --version

echo "Starting the docker-compose for one2n sre bootcamp Milestone 5"
if command_exists make; then
    echo "make is already installed"
else
    echo "Make is not installed. Installing Make..."    
    sudo apt-get install -y make
    echo "Make installed successfully"
fi

cd /vagrant \
    && make start_vagrant

echo "docker container started please check container logs for errors"

echo "Script execution completed."
