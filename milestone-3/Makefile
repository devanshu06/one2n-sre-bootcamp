PROJECT_NAME := one2n-sre-bootcamp
IMAGE_NAME := dev06/one2n-sre-bootcamp
TAG := rest-api

ifeq ($(OS),Windows_NT)
	PIP := pip
	PYTHON := python
else
	PIP := pip3
	PYTHON := python3
endif

up:
	docker-compose -f docker-compose.yml up --build -d 

down:
	docker-compose -f docker-compose.yml down

build_image:
	docker build -t $(IMAGE_NAME):$(TAG) .

clean_image:
	docker rmi $(IMAGE_NAME):$(TAG)

push_image: 
	docker push $(IMAGE_NAME):$(TAG)

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py
