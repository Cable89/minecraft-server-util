#!/usr/bin/bash

# /etc/init.d/minecraft_server
#
### BEGIN INIT INFO
# Provides:          minecraft server
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start minecraft server in screen
# Description:       minecraft is fun
### END INIT INFO

PATH=/usr/local/bin:/usr/bin:/bin

DELAY=30
if [ "$2" != '' ]; then
    if [ "$2" -lt 3600 ]; then
        let DELAY=$2
    else
        let DELAY=3600
    fi
fi

JXMX=8G
JXMS=8G
MINECRAFT_SERVER=minecraft_server.jar

SCREEN=minecraft
MESSAGE="Server restarting in "$(($DELAY + 10))" seconds!"
MINECRAFTDIR=/etc/minecraft
WORLDNAME=island
WORLDDIR=$MINECRAFTDIR/$WORLDNAME
BACKUPDIR=$MINECRAFTDIR/backupdir
TIMESTAMP=$(date +%Y-%m-%d.%H-%M-%S)
BACKUPFILE=$BACKUPDIR/$WORLDNAME.backup.$TIMESTAMP.tar.gz



function server_check {
    ONLINE=$(ps aux | grep "$MINECRAFTDIR/$MINECRAFT_SERVER nogui" | wc -l) 
    SCREENEXIST=$(screen -S $SCREEN -Q select . ; echo $?) # Returns 0 if screen exists
}

function start_minecraft {
    echo "Starting Minecraft"
    screen -S $SCREEN -d -m
    screen -S $SCREEN -p 0 -X stuff "java -Xmx$JXMX -Xms$JXMS -jar $MINECRAFTDIR/$MINECRAFT_SERVER nogui
"
}

function start_minecraft_forceupgrade {
    echo "Starting Minecraft"
    screen -S $SCREEN -d -m
    screen -S $SCREEN -p 0 -X stuff "java -Xmx$JXMX -Xms$JXMS -jar $MINECRAFTDIR/$MINECRAFT_SERVER --forceUpgrade nogui
"
}

function stop_minecraft {
    screen -S $SCREEN -p 0 -X stuff "`printf "say $MESSAGE\r"`"; sleep $DELAY
    screen -S $SCREEN -p 0 -X stuff "`printf "say Server restarting in 10 seconds!\r"`"
    screen -S $SCREEN -p 0 -X stuff "`printf "save-all\r"`"; sleep 5
    screen -S $SCREEN -p 0 -X stuff "`printf "stop\r"`"; sleep 5
    screen -S $SCREEN -p 0 -X quit
}

function run_backup {
    cd $MINECRAFTDIR
    # tar -czf $BACKUPFILE $WORLDNAME
    tar -czf $BACKUPFILE $WORLDNAME ${WORLDNAME}_nether ${WORLDNAME}_the_end
    . /etc/minecraft/minecraft_backup_copy.sh &
}

function update_spigot {
    . /etc/minecraft/minecraft_update_spigot.sh &
}

case "$1" in
    start)
        server_check
        if [ $ONLINE == 2 ] || [ $SCREENEXIST == 0 ]; then
            echo "Minecraft server already running"
        fi
        echo "Starting minecraft server"
        start_minecraft
    ;;
    start_nocheck)
        echo "Starting minecraft server"
        start_minecraft
    ;;
    start_forceupgrade)
        server_check
        if [ $ONLINE == 2 ] || [ $SCREENEXIST == 0 ]; then
            echo "Minecraft server already running"
        fi
        echo "Starting minecraft server"
        start_minecraft_forceupgrade
    ;;
    stop)
        echo "Stopping minecraft server"
        stop_minecraft
    ;;
    restart)
        echo "Restarting minecraft server"        
        server_check
        if [ $ONLINE == 2 ] || [ $SCREENEXIST == 0 ]; then
            stop_minecraft
        fi
        start_minecraft
    ;;
    update_spigot)
        echo "Updating minecraft server"
        server_check
        update_spigot
        echo "Restarting minecraft server"
        if [ $ONLINE == 2 ] || [ $SCREENEXIST == 0 ]; then
            stop_minecraft
        fi
        start_minecraft_forceupgrade
    ;;
    backup)
        server_check
        if [ $ONLINE == 2 ]; then
            stop_minecraft
        fi
        server_check
        if [ $ONLINE == 1 ]; then
            run_backup
            #update_spigot
            start_minecraft
        else
            echo "Unable to stop minecraft server"
        fi
 
    ;;
    status)
        server_check
        if [ $ONLINE == 2 ]; then
            echo "Minecraft server is running"
        elif [ $ONLINE == 1 ]; then
            echo "Minecraft server process not found"
        else
            echo $ONLINE
        fi
    ;;
    *)
        echo  "Usage: {start|stop|restart|update|backup|status} <delay in ms>"
esac
