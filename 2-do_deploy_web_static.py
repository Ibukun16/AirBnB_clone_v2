#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""

from datetime import datetime
from fabric.api import *
from os import path


env.hosts = ["34.227.94.180", "100.25.167.156"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """Deploy web files to server."""
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(timestamp))

        # uncompress archive and delete .tgz
        run(f"sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C \
    /data/web_static/releases/web_static_{timestamp}/")

        # remove archive
        run(f'sudo rm /tmp/web_static_{timestamp}.tgz')

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run(f'sudo ln -s /data/web_static/releases/web_static_{timestamp}/ \
                /data/web_static/current')
    except Exception:
        return False

    print("New version deployed!")
    return True
