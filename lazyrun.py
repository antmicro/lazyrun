#!/usr/bin/env python3

# There are two use cases. One is a local one - a project with its
# own .lazyrun.yml. The other is a global use case where you have 
# some kind of (perhaps layered) global config, often used containers
# of good quality that are shared between people in repositories.
#
# For now, only the local use case will be implemented.

# later add way to include config in different file/path

import yaml
import sys
import os
import shutil
import stat

config = None
try:
    with open('.lazyrun.yml', 'r') as f:
        config = yaml.safe_load(f)
except IOError as e:
    print("Error opening config file!")
    print("Make sure there is a .lazyrun.yml in the current directory.")
    sys.exit(1)

folder = '.lazyrun'

if not os.path.exists(folder):
    os.makedirs(folder)

podman_bin = 'https://github.com/antmicro/lazyrun/releases/download/0.1/podman'

podman_warning = f"""No podman found. Execute:

cd {os.getcwd()}/{folder}
sudo wget {podman_bin}
sudo chmod a+x podman
cd -

To get it."""

if shutil.which('podman') is None:
    print(podman_warning)

def chmod_plusx(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)

# run through config objects and create appropriate symlinks
for app in config:
    print(f"Creating wrapper for {app}: {config[app]}")
    path = folder + "/" + app
    with open(path, 'w') as f:
        f.write(f"podman run -it {config[app]} {app} $@")
        chmod_plusx(path)

init_script = folder + "/init"
init_script_text = f"""#!/bin/sh
if ! command -v podman &> /dev/null
then
    echo "Podman not found. Please see error message in lazyrun itself."
    exit
fi
export PATH={os.getcwd()}/{folder}:$PATH"""

# create init script
with open(init_script, 'w') as f:
    f.write(init_script_text)
    print(f"Use 'source {init_script}' to enter the lazyrun environment.")
