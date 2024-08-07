PROJECT_NAME := one2n-sre-bootcamp
IMAGE_NAME := dev06/one2n-sre-bootcamp
VENV_DIR := $(BASE_DIR)/venv
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
	docker compose -f docker-compose.yml up --build -d 

down:
	docker compose -f docker-compose.yml down

# You should run below make action when you are setting up project on your local. For Running Migration in the Docker Please refer to README.md
run_db_migration:
	$(VENV_DIR)/bin/$(PYTHON) -m flask --app main.py db upgrade

build_image:
	docker build -t $(IMAGE_NAME):$(TAG) .

clean_image:
	docker rmi $(IMAGE_NAME):$(TAG)

push_image: 
	docker push $(IMAGE_NAME):$(TAG)

check_python:
	@if which $(PYTHON) > /dev/null; then \
        echo "$(PYTHON) is installed."; \
    else \
        echo "$(PYTHON) is not installed. Please install $(PYTHON) before proceeding."; \
        exit 1; \
    fi

setup_venv: check_python
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment setup at $(VENV_DIR)"

install: setup_venv
	$(VENV_DIR)/bin/$(PIP) install -r requirements.txt

run:
	$(VENV_DIR)/bin/$(PYTHON) main.py