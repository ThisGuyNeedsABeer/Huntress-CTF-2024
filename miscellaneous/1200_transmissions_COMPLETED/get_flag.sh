#!/bin/bash

minimodem --rx -f transmissions.wav 1200 | grep -oE "flag{.*?}" --color=none
