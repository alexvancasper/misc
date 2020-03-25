#!/bin/bash

############################################
# bash --version
# GNU bash, version 4.1.2(1)-release (x86_64)
############################################

USER="user1"
PASS="password1"
DSTFOLDER="dstfolder"

declare -a nodes
readarray -t nodes < nodes.lst
let i=0
while (( ${#nodes[@]} > i )); do
    myline=${nodes[i++]}
    echo "LINE: $myline"
    IPADDR=$(echo $myline | /bin/cut -d ":" -f2)
    PATH=$(echo $myline | /bin/cut -d ":" -f3)
    f="$(/bin/basename -- $PATH)"
    /usr/bin/curl -k sftp://$IPADDR:22$PATH --user "$USER:$PASS" -o "$DSTFOLDER/$f"
done


############################################
# nodes.lst
# SERVER1:10.0.0.1:/var/log/show_technical_support.tar.gz
# SERVER2:10.0.1.1:/var/log/show_technical_support.tar.gz


