#!/usr/bin/python3
"""Compress files in web_static folder"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates archive file from the contents
    of web_static folder"""
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_name = 'web_static_{}.tgz'.format(time)
    try:
        local("mkdir -p versions")
        archive_path = 'versions/{}'.format(archive_name)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None
