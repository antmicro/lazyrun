#!/usr/bin/env python3

# default config should be included
# user needs to copy it to config.yml
# read additional "overlay" config, if specified as a parameter
# perhaps later divide between "repositories" and masks (don't overcomplicate)
# run through config objects and create appropriate symlinks

import yaml

config = None
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

for app in config:
    print(f"Creating wrapper for {app}: {config[app]}")
    path = 'apps/' + app
    with open(path, 'w') as f:
        f.write(f"podman run -it {config[app]} {app} $@")
        import os
        import stat

        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)

# later add way to include config in different file/path
