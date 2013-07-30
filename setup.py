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
from glob import glob

data_files = []
data_files.append(('/usr/share/httpdtap/scripts-22', glob('scripts-22/*.stp')))
data_files.append(('/usr/share/httpdtap/scripts-24', glob('scripts-24/*.stp')))

setup(
	name = 'httpdtap',
	description = 'Tool for searching for patches of particular component',
	data_files = data_files,
	version = version,
	license = 'ASL2',
	download_url = 'https://github.com/hanzz/httpdtap',
	url = 'https://github.com/hanzz/httpdtap',
	scripts = ["httpdtap"],
	maintainer  = 'Jan Kaluza',
	maintainer_email = 'hanzz.k@gmail.com'
)
