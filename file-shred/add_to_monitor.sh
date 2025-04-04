#!/bin/bash

path=`pwd`


_dels=("51for_delete.txt" \
        "52for_delete.txt" \
        "53for_delete.txt" 
        )

for _del in ${_dels[@]}; do
    touch ${path}/${_del}
done


for _del in ${_dels[@]}; do
    sudo auditctl -w ${path}/${_del} -p wra
done

echo "Files created and added to ctl"