#!/usr/bin/env python
"""
Setup script
"""

import os,sys
pkg_dir = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                       'src')

from distutils.core import setup
version = '0.1'

import shutil

setup(
    name = 'httpdtap',
    description = 'Tool for searching for patches of particular component',
    data_files = [('/usr/share/httpdtap/',
				   [ 'scripts-22/req_time.stp','scripts-22/req_from.stp', 'scripts-22/req_files.stp', 'scripts-22/req_slower_than.stp' ],
				   [ 'scripts-24/req_time.stp','scripts-24/req_from.stp', 'scripts-24/req_files.stp', 'scripts-24/req_slower_than.stp' ]
				   ) ],
    version = version,
    license = 'ASL2',
    download_url = 'https://github.com/hanzz/httpdtap',
    url = 'https://github.com/hanzz/httpdtap',
    scripts = ["httpdtap"],
    maintainer  = 'Jan Kaluza',
    maintainer_email = 'hanzz.k@gmail.com'
)
