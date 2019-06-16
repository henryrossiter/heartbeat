import subprocess
import os
import time
import config

repository_url = config.repository
repository_name = config.repository[config.repository.rfind('/')+1:]
build_branch = config.build_branch
wait_time = config.wait_time

print('\n------------------------------------------')
print('--- Launching CD Scripts for {} ---'.format(repository_name))
print('------------------------------------------\n')


if not os.path.exists(repository_name):
    print('Cloning {}'.format(repository_name))
    subprocess.run(['git', 'clone', config.repository])

print('\n-------------------------------')
print('--- Installing dependencies ---')
print('-------------------------------\n')
installer = subprocess.Popen(
                             'npm install',
                             shell=True,
                             cwd=repository_name)
installer.wait()

print('\n-------------------------------')
print('--- Launching Server ---')
print('-------------------------------\n')
subprocess.Popen(
                 'npm start',
                 shell=True,
                 cwd=repository_name)

while True:
    print('\n--------------------------------------')
    print('Pulling changes from {} branch'.format(build_branch))
    print('--------------------------------------\n')
    subprocess.Popen(
                     'git fetch origin',
                     shell=True,
                     cwd=repository_name)
    subprocess.Popen(
                     'git reset --hard origin/{}'.format(build_branch),
                     shell=True,
                     cwd=repository_name)

    time.sleep(5)

    print('\n-----------------------------')
    print('--- Updating dependencies ---')
    print('-------------------------------\n')
    installer = subprocess.Popen(
                     'npm install',
                     shell=True,
                     cwd=repository_name)
    installer.wait()

    time.sleep(wait_time)
