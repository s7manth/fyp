#!/bin/bash
for i in 1 2 3 4 5
do
   echo "Run $i"; python experiments/zeroshot-vanilla.py; sleep 120
done
