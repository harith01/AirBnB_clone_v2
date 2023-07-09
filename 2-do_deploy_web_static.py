#!/usr/bin/python3
"""Fabric script that distributes an archive
to web servers"""

from fabric.api import run, put, env
from os.path import exists
env.hosts = ['35.153.194.15','	3.83.238.14']


def do_deploy(archive_path):
    """Deploys an archive to the servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        noext = file_name.split(".")[0]
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}{}'.format(file_name, path, noext))
        run('rm /tmp/{}'.format(archive_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noext)
        return True
    except:
        return False
