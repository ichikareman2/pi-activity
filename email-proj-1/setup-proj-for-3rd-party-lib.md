# Problem
Can't install 3rd party libraries along with system libraries.

# Solution
create virtual environments

# Link
https://www.raspberrypi.com/documentation/computers/os.html#python-on-raspberry-pi

# In short
* run inside proj directory: `python -m venv --system-site-packages env`
    * there will be a python distribution in this directory
    * `-m`
    * `venv` creates virtual env
    * `--system-site-packages` inherit libraries from system/OS
    * `env` environment folder
* run `source env/bin/activate`
    * to activate virtual env
* deactivate using virual env python by running `deactivate`
