VERSION=1.16
wget https://overviewer.org/textures/${VERSION} -O /etc/minecraft/versions/${VERSION}.jar
chmod +x /etc/minecraft/versions/${VERSION}.jar
rm /etc/minecraft/versions/client.jar
ln -s /etc/minecraft/versions/${VERSION}.jar /etc/minecraft/versions/client.jar
