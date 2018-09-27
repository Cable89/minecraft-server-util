#!/bin/bash

FILE=$(find /etc/minecraft/backupdir/ -name island.backup.*.tar.gz | sort -n | tail -1)

cp $FILE /media/nfs/ovsky/OVSky/minecraft/
