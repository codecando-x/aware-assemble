# aware-assemble

A simple way to gather, package and send log files to another server.

## Getting Started

Add your log server's ssh private key and reference it in the config.json file.

### Prerequisites

Developed and tested this code on python3.8.

### Installing

The config.yaml file is self explanatory. Customize it to fit your needs. You can also use a config.json file if you prefer.

The run and place the process in background:

```
python3.8 assemble.py &
```

The process will run once and then will sleep for the duration of the time set in the config file.

Check the history.log file for information of what occured.

## Deployment

Drop it in a folder on every node you would like to gather logs from.

## Built With

python3.8

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
