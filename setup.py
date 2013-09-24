# -*- coding: utf-8 -*-

import os
import os.path as p
import re

from distribute_setup import use_setuptools; use_setuptools()
from setuptools import setup, find_packages


rel_file = lambda *args: p.join(p.dirname(p.abspath(__file__)), *args)

def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()


if not hasattr(p, 'relpath'):
    def relpath(path, start=p.curdir):
        """Return a relative version of a path"""

        if not path:
            raise ValueError("no path specified")

        start_list = p.abspath(start).split(p.sep)
        path_list = p.abspath(path).split(p.sep)

        # Work out how much of the filepath is shared by start and path.
        i = len(p.commonprefix([start_list, path_list]))

        rel_list = [p.pardir] * (len(start_list)-i) + path_list[i:]
        if not rel_list:
            return p.curdir
        return p.join(*rel_list)
    p.relpath = relpath


def get_version():
    data = read_from(rel_file('src', 'phdoc', '__init__.py'))
    return re.search(r"__version__ = '([^']+)'", data).group(1)


def get_requirements():
    data = read_from(rel_file('REQUIREMENTS'))
    lines = map(lambda s: s.strip(), data.splitlines())
    return filter(None, lines)


def find_package_data():
    files = []
    src_root = p.join(p.dirname(__file__), 'src', 'phdoc')
    static_root = p.join(src_root, 'static')
    for dirpath, subdirs, filenames in os.walk(static_root):
        for filename in filenames:
            if not filename.startswith('.') or filename.startswith('_'):
                abs_path = p.join(dirpath, filename)
                files.append(p.relpath(abs_path, start=src_root))
    return files

setup(
    name             = 'PHDoc',
    version          = get_version(),
    author           = "Remigiusz 'lRem' Modrzejewski",
    url              = 'http://github.com/lrem/phdoc',
    description      = "A Markdown-based wiki crafted for academics.",
    packages         = find_packages(where='src'),
    package_dir      = {'': 'src'},
    package_data     = {'phdoc': find_package_data()},
    entry_points     = {'console_scripts': ['phdoc = phdoc.cli.main:main']},
    install_requires = get_requirements(),
)
