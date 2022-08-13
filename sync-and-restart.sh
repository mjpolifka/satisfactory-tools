#!/bin/bash

echo "killing gunicorn..."
pkill gunicorn
echo "gunicorn killed"

echo "pulling new code..."
git pull
echo "code pulled"

echo "restarting gunicorn..."
gunicorn -D app:app
echo "application upated and restarted"