BASE_DIR := $(shell pwd)
PROJECT_NAME := one2n-sre-bootcamp

ifeq ($(OS),Windows_NT)
    PIP := pip
    PYTHON := python
else
    PIP := pip3
    PYTHON := python3
endif

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py


