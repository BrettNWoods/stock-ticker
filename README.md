# Stock Ticker

This repository contains a simply Flask application and associated Kubernetes infrastructure required to monitor the performance of a stock using [Alpha Vantage](https://www.alphavantage.co/). Given a Symbol and number of days, it will fetch the daily timeseries data for the given number of days as well as the average closing price over those number of days.

# Prequisites

* A [free API key from Alpha Vantage](https://www.alphavantage.co/support/#api-key)
* [Poetry] for dependency management
* [Docker](https://www.docker.com/) (or [Podman](https://podman.io/) with an alias to docker) for building the image
* Minikube for deploying the application to kubernetes
* [Make](https://www.gnu.org/software/make/) for running build and deploy scripts

# Callouts

I used Python for this exercise for two reasons;

1. Honestly, I'm more comfortable with Python
2. I found that there is a fairly popular [alpha-vantage package](https://github.com/RomelTorres/alpha_vantage) that I could use to simplify my work significantly.


Flask was chosen as it's a quick way to create a webserver but ultimately, gunicorn gets used within the image as it allows for multiple workers and threads to be utilised.

# TO-DOs:
1. Utilise dataclasses so that we are passing around structured objects instead of strings.
2. Put in some actual logging.
