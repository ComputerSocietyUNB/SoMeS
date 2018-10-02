import os
from invoke import task


@task
def install(c):
    """ Installs the requirements necessary for this project """
    create(c)
    c.run("pip3 install -r requirements.txt")


@task
def style(c):
    """ Cheks if your code is well formatted for this project """
    c.run("pycodestyle . --ignore=E402,W504 --exclude=venv")


@task
def run(c):
    """ Installs the requirements necessary for this project """
    c.run("python3 main.py")


@task
def create(c):
    """ Create message folders to store messages. """
    if not os.path.isdir('message/sent'):
        os.makedirs('message/sent')
    if not os.path.isdir('image/sent'):
        os.makedirs('image/sent')
