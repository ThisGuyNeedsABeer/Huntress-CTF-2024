#!/bin/bash

zbarimg --nodbus -q flag.png | grep -oE flag{.*?} --color=none
