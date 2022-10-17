#!/bin/bash
docker-compose up -d
sleep 10
docker exec test_client bash -c 'pip install pytest'
docker exec test_client bash -c 'pytest -s'
