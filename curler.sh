#!/bin/bash

while : 

do

curl http://192.168.222.14:5000
sleep $((RANDOM % 300))

done