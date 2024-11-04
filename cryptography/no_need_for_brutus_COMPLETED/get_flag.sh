#!/bin/bash

echo -n "caesarissimplenoneedforbrutus" | md5sum | awk '{print "flag{"$1"}"}'
