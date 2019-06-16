import subprocess
import os
import time
import config

repository_url = config.repository
repository_name = config.repository[config.repository.rfind('/')+1:]
build_branch = config.build_branch
wait_time = config.wait_time


def bordered_print(msg):
    length = len(msg)
    print('\n')
    print('-' * length)
    print(msg)
    print('-' * length)


bordered_print('Launching CD Scripts for {}'.format(repository_name))

if not os.path.exists(repository_name):
    bordered_print('Cloning {}'.format(repository_name))
    subprocess.run(['git', 'clone', config.repository])

bordered_print('Installing dependencies')
installer = subprocess.Popen(
                             'npm install',
                             shell=True,
                             cwd=repository_name)
installer.wait()

bordered_print('Launching Server')
subprocess.Popen(
                 'npm start',
                 shell=True,
                 cwd=repository_name)

while True:
    bordered_print('Pulling changes from {} branch'.format(build_branch))
    fetcher = subprocess.Popen(
                     'git fetch origin',
                     shell=True,
                     cwd=repository_name)
    fetcher.wait()

    resetter = subprocess.Popen(
                     'git reset --hard origin/{}'.format(build_branch),
                     shell=True,
                     cwd=repository_name)
    resetter.wait()

    bordered_print('Updating dependencies')
    installer = subprocess.Popen(
                     'npm install',
                     shell=True,
                     cwd=repository_name)
    installer.wait()

    time.sleep(wait_time)
