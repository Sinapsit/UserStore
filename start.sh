#!/usr/bin/env bash

docker-compose -f docker-compose.yml up -d --build
sleep 5
docker exec userstore_app_1 python manage.py migrate --noinput
docker exec userstore_app_1 python manage.py loaddata dump.json
docker-compose -f docker-compose.yml stop
docker-compose -f docker-compose.yml up