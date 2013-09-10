#!/usr/bin/env python
"""
Setup script
"""

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Author: Jan Kaluza

import os,sys
pkg_dir = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                       'src')

from distutils.core import setup
# Do not forget to change VERSION also in httpdtap file
version = '0.1'

import shutil
from glob import glob

data_files = []
data_files.append(('/usr/share/httpdtap/scripts-22', glob('scripts-22/*.stp')))
data_files.append(('/usr/share/httpdtap/scripts-24', glob('scripts-24/*.stp')))
data_files.append(('/usr/share/man/man8', glob('man/*.8')))

setup(
	name = 'httpdtap',
	description = 'Tool for querying httpd using SystemTap scripts.',
	data_files = data_files,
	version = version,
	license = 'ASL2',
	download_url = 'https://github.com/hanzz/httpdtap',
	url = 'https://github.com/hanzz/httpdtap',
	scripts = ["httpdtap"],
	maintainer  = 'Jan Kaluza',
	maintainer_email = 'hanzz.k@gmail.com'
)
