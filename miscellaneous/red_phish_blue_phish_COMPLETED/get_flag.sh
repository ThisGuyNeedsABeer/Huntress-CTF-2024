#!/bin/bash

cat solve.txt | grep -oE "flag{.*?}" | head -n 1
