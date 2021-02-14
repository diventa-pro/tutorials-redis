#!/bin/sh
sleep 10
redis-cli --cluster create redis1:7000 redis2:7000 redis3:7000 --cluster-replicas 0 --no-auth-warning --verbose