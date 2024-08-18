#!/usr/bin/python3
"""A Fabric script module that generates a .tgz archive."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generate tgz archives of the static files using fabric."""
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date_time)
    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    print("Packing web_static to {}".format(filename))
    local("tar -cvzf " + filename + " web_static")
    size = os.stat(filename).st_size
    if os.path.exists(filename):
        print("web_static packed: {} -> {} Bytes".format(filename, size))
        return filename
    else:
        return None
