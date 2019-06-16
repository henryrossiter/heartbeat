import pexpect
import subprocess
import os
import time
import config

repository_url = config.repository
repository_name = config.repository[config.repository.rfind('/')+1:]
build_branch = config.build_branch
wait_time = config.wait_time

print('Launching CD Scripts for {}'.format(repository_name))

if not os.path.exists(repository_name):
    print('Cloning {}'.format(repository_name))
    subprocess.run(['git', 'clone', config.repository])

while True:
    print('Pulling changes from {} branch'.format(build_branch))
    subprocess.Popen(
                     'git fetch origin',
                     shell=True,
                     cwd=repository_name)
    subprocess.Popen(
                     'git reset --hard origin/{}'.format(build_branch),
                     shell=True,
                     cwd=repository_name)

    time.sleep(5)
    print('--- Updating dependencies ---')
    updater = pexpect.spawn(
                     'npm install',
                     cwd=repository_name)
    time.sleep(10)

    updater.sendcontrol('c')
    updater.close()

    print('--- Starting Bundler ---')
    bundler = subprocess.Popen(
                     'npm start',
                     cwd=repository_name)
    time.sleep(10)

    bundler.sendcontrol('c')
    bundler.close()
    print('--- Killed Bundler ---')

    time.sleep(100)

    # time.sleep(wait_time)
