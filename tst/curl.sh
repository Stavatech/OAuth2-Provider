#!/bin/bash

# set username and password appropriately
curl -X POST -d "grant_type=password&username=test1&password=asdf4321" -u"JYNAHw46XJPkrFanslAPUf0bE8auSLOAQ5FnJuZJ:o8ZmpPCzNgsunQVs4dgmV85E8DUyxmZaqMQG2k6eKT9Aqqjhd68Kp3YuuNRnQK1UKXU6BxSKhJ4nWhC1wN8hilxrIM6PAkKOipEYAEKk4NgX87pTt4oKynXy1SkUPUQg" http://192.168.8.101:8000:8000/auth/token/
