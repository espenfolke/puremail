#!/bin/bash
clear

FILE=docker-compose.yml

docker-compose -f $FILE kill
docker-compose -f $FILE down
docker-compose -f $FILE up -d migration
docker-compose -f $FILE up -d