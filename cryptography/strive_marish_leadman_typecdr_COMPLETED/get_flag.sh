#!/bin/bash

python solve.py | grep -oE "flag{.*?}" --color=none
