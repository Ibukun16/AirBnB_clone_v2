#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['34.227.94.180', '100.25.167.156']
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"

def do_pack():
    """generate a tgz archive using fabric"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    print("Packing web_static to {}".format(file_name))
    local("tar -cvzf " + file_name + " web_static")
    size = os.stat(file_name).st_size
    if os.path.exists(file_name):
        print("web_static packed: {} -> {} Bytes".format(file_name, size))
        return file_name
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False
    arch_name = archive_path.split("/")[1]
    arch_path = "/data/web_static/releases/" + arch_name.split(".")[0]
    put(archive_path, '/tmp/')
    run("mkdir -p " + arch_path)
    run("tar -xzf /tmp/{} -C {}/".format(arch_name, arch_path))
    run("rm /tmp/" + arch_name)
    run("mv " + arch_path + "/web_static/* " + arch_path + "/")
    run("rm -rf " + arch_path + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + arch_path + " /data/web_static/current")
    print("New version deployed!")
    return True


def deploy():
    """
    creates and distributes an archive to the web servers

    Return False if no archive has been created
    Call the do_deploy(archive_path) function,
    using the new path of the new archive
    Return the return value of do_deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
