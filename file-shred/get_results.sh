#!/bin/bash

# sudo ausearch -f /home/<user_name>/test_shred.txt -i | grep wipe
iam=`pwd`

_dels=("41for_delete.txt" \
        "42for_delete.txt" \
        "43for_delete.txt" 
        )

for _del in ${_dels[@]}; do
    sudo ausearch -f ${iam}/${_del} -i | grep wipe
done