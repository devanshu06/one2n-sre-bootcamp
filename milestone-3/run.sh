#!/bin/sh

if [ "$RUN_MIGRATION" = "true" ]; then
    echo "Running database migrations..."
    flask --app main.py db upgrade
fi

echo "Starting the Python server..."
python main.py
