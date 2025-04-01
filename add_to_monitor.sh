#!/bin/bash



_dels=("41for_delete.txt" \
        42for_delete.txt" \
        43for_delete.txt" 
        )

for _del in ${_dels[@]}; do
    touch ${_del}
done


for _del in ${_dels[@]}; do
    sudo auditctl -w ${_del} -p wra
done