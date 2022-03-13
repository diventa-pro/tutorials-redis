#!/bin/sh
redis-cli --cluster create 172.28.0.4:6379 172.28.0.2:6379 172.28.0.3:6379 172.28.1.4:6379 172.28.1.2:6379 172.28.1.3:6379 --cluster-replicas 1 --verbose