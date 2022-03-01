#!/bin/bash

VERSION=1.17
#wget https://overviewer.org/textures/${VERSION} -O /etc/minecraft/versions/${VERSION}.jar
#rm /etc/minecraft/versions/client.jar
#ln -s /etc/minecraft/versions/${VERSION}.jar /etc/minecraft/versions/client.jar

# Debian package. Currently not working for debian 11
#overviewer.py --config=/etc/minecraft/overviewer-config/options.py --genpoi --skip-scan
#overviewer.py --config=/etc/minecraft/overviewer-config/options.py

# Built from source
python3 /etc/minecraft/overviewer_source/overviewer.py --config=/etc/minecraft/overviewer-config/options.py --genpoi --skip-scan
python3 /etc/minecraft/overviewer_source/overviewer.py --config=/etc/minecraft/overviewer-config/options.py

