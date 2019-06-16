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

    print('Updating dependencies and restarting compiler')
    subprocess.Popen(
                     'npm install',
                     shell=True,
                     cwd=repository_name)
    subprocess.Popen(
                     'npm start',
                     shell=True,
                     cwd=repository_name)

    time.sleep(wait_time)
