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
        Deploy archive files to the web server.
    """
    if os.path.exists(archive_path) is False:
        return False

    arch_file = archive_path.split("/")[1]
    new_file = "/data/web_static/releases/" + arch_file.split(".")[0]
    arch_tmp = "/tmp/" + arch_file

    # upload archive
    put(archive_path, "/tmp/")

    # create target dir
    run("sudo mkdir -p " + new_file + "/")

    # uncompress archive into newfile without .tgz extension
    run("sudo tar -xzf /tmp/{} -C {}/".format(arch_file, new_file))

    # remove archive
    run("sudo rm " + arch_tmp)

    # move contents into host web_static
    run("sudo mv " + new_file + "/web_static/* " + new_file + "/")

    # remove extraneous web_static dir
    run("sudo rm -rf " + new_file + "/web_static")

    # delete pre-existing sym link
    run("sudo rm -rf /data/web_static/current")

    # re-establish symbolic link
    run("sudo ln -s " + new_file + " /data/web_static/current")

    print("New version deployed!")
    return True
