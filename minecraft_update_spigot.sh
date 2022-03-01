#!/usr/bin/bash

cd /etc/minecraft/spigot
wget -O BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
new_filename=$(java -jar BuildTools.jar --rev 1.18 | sed -n '/Saved as/p' | sed 's:.*/::')
echo New spigot server is $new_filename 
cp $new_filename /etc/minecraft/
cd /etc/minecraft
chmod +x $new_filename
ln -sf /etc/minecraft/$new_filename  /etc/minecraft/minecraft_server.jar
