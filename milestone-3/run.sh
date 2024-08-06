#!/bin/sh

flask --app main.py db upgrade \
&& python main.py
