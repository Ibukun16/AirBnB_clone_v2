#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["34.227.94.180", "100.25.167.156"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
       Deploy web files to server.
    """
    # upload archive
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(timestamp))

        # uncompress archive and delete .tgz
        run(f"sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C \
/data/web_static/releases/web_static_{timestamp}/")

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/\
            web_static_{}/ /data/web_static/current'.format(timestamp))

        print("New version deployed!")
        return True

    return False
