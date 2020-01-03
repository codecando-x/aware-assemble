# aware-assemble 

A simple way to gather, package and send log files to another server.

## Getting Started

Add your log server's ssh private key and reference it in the config.json file.

### Prerequisites

Developed and tested this code on python3.7.

### Installing

The config.json file is self explanatory. Customize it to fit your needs.

The run and place the process in background:

```
python3.7 assemble.py &
```

The process will run once and then will sleep for the duration of the time set in the config file. Then will run again. This gives you the flexibility to choose how often you want to collect logs depending on how much traffic you get. Also lets you choose the lag time between the log event occurence time and your ability to analyze it once it has been processed. On apache you can set it up so that it does not restart the webserver when it rotates the logs, instead it just copies the entries to another file. So you can just configure to send that file over at a certain interval. That way making sure you don't send duplicates over all the time.

Check the history.log file for information of what occured.

## Deployment

Drop it in a folder on every node you would like to gather logs from.

## Built With

python3.7

## Authors

* **Daniel Achim** - *Initial work* - [codecando-x](https://github.com/codecando-x)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
