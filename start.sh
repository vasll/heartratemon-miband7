#!/bin/bash

# Start the npm web app in the background
cd web && npm run serve 2>&1 &
NPM_PID=$!

# Start the Python script in the background
python3 main.py 2>&1 &
PYTHON_PID=$!

# Function to clean up background processes on exit
cleanup() {
    echo "Stopping processes..."
    kill $NPM_PID $PYTHON_PID
    exit
}

# Trap SIGINT and SIGTERM signals to run cleanup
trap cleanup SIGINT SIGTERM

# Wait for both processes to finish
wait $NPM_PID
wait $PYTHON_PID
