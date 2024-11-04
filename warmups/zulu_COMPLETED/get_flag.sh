#!/bin/bash

strings zulu | grep -oE "flag{.*?}" --color=none
