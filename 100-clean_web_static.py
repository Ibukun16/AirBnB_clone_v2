#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["34.227.94.180", "100.25.167.156"]


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    try:
        number = int(number)
    except Exception:
        return False
    num_of_arch = local('ls -ltr versions | wc -l', capture=True).stdout
    num_of_arch = int(num_of_arch) - 1
    if num_of_arch <= 0 or num_of_arch == 1:
        return True
    if number == 0 or number == 1:
        arch_to_rm = num_of_arch - 1
    else:
        arch_to_rm = arch_to_rm - number
        if arch_to_rm <= 0:
            return True
    archives = local("ls -ltr versions | tail -n " + str(num_of_arch) + "\
            | head -n \
            " + str(arch_to_rm) + "\
            | awk '{print $9}'", capture=True)
    archives_list = archives.rsplit('\n')
    if len(archives_list) >= 1:
        for a in archives_list:
            if (a != ''):
                local("rm versions/" + a)
                run('rm -rf /data/web_static/releases/' + a.split('.')[0])
