#!/bin/bash

python3 solve.py | grep -oE flag"{.*?}" --color=none | head -1
