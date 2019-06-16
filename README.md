# heartbeat
Local Network Continuous Deployment for Create-React-App Applications

### Requirements

- Python 3

### Configuration

Edit ```config.py```

```
repository = <url to react app's git repository>
build_branch = <branch of repository to build from>
wait_time = <time, in seconds, to wait between builds>
```

For example, the following ```config.py``` would result in the master branch of Material-Drawer-Router being rebuilt and deployed on the hosts local network every hour (3600 seconds).
```
repository = 'https://github.com/henryrossiter/Material-Drawer-Router'
build_branch = 'master'
wait_time = 60
```

### Deployment

```
> python main.py
```
