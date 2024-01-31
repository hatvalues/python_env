# A Codespaces Environment

This repo has been set up for codespaces. A newer version of Python is installed and the terminal configured with venv.

## Steps to Reproduce
`sudo apt-get update`

`sudo apt-get install build-essential gdb lcov libffi-dev libgdbm-dev liblzma-dev libncurses5-dev libreadline-dev libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev`

`wget https://www.python.org/ftp/python/3.11.7/Python-3.11.7.tgz`

`tar zxvf Python-3.11.7.tgz`

`rm Python-3.11.7.tgz`

`cd Python-3.11.7`

`./configure --enable-optimizations`

`make` option -j [number of procs]

`sudo make altinstall`
`cd ..`

`vim ~/.bashrc` I [insert mode]

add an alias:

alias python="/usr/local/bin/python3.11"

source ~/.venv/bin/activate

`python -m venv ~/.venv`

`source ~/.bashrc`

`rm -rf Python-3.11.7`

