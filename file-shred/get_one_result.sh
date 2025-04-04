#!/bin/bash

iam=`pwd`

sudo ausearch -f ${iam}/$1 -i | grep wipe | grep $1