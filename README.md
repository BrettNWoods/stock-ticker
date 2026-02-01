# Stock Ticker

This repository contains a simply Flask application and associated Kubernetes infrastructure required to monitor the performance of a stock using [Alpha Vantage](https://www.alphavantage.co/). Given a Symbol and number of days, it will fetch the daily timeseries data for the given number of days as well as the average closing price over those number of days.

# Prerequisites

* A [free API key from Alpha Vantage](https://www.alphavantage.co/support/#api-key)
* [Poetry](https://python-poetry.org/) for dependency management
* [Docker](https://www.docker.com/) for building the image
* [Minikube](https://minikube.sigs.k8s.io/docs/) for deploying the application to a kubernetes cluster
* [Make](https://www.gnu.org/software/make/) for running build and deploy scripts

# Getting Started

## Application

* To run the test suite for that application, run `make test`
* To run a local instance of the application on `localhost:8080`, run `make local`
* To build the image on your system locally, run `make build`

## Infrastructure

* To initialise minikube, run `make minikube`
* To deploy the application to your local cluster, run `make deploy`

Once deployed, you can reach the application running on your cluster by running;

```
curl --resolve "stock-ticker.local:80:$(minikube ip)" http://stock-ticker.local
```

# Architectural Decisions 

## Application
I used Python for this exercise for two reasons;

1. I'm a bit more comfortable with Python for quick implementations.
2. I found that there is a fairly popular [alpha-vantage package](https://github.com/RomelTorres/alpha_vantage) that I could use to simplify my work significantly.

Flask was chosen as it's a quick way to create a webserver but ultimately, gunicorn gets used within the image as it allows for multiple workers and threads to be utilised. Flask also [explicitly says you should not use it in a production environment](https://flask.palletsprojects.com/en/stable/deploying/#deploying-to-production) so the choice was made for me. 

## Infrastructure

Simply, I just created these resources as plain kubernetes manifests. For a production deployment, you would want to package these up using a tool like [helm](https://helm.sh/) or [Kustomize](https://kustomize.io/).

For building the image, I just built the image locally and exposed that to Minikube. For a more robust set up, you need to be building and pushing the image somewhere with `docker push`

# Python Improvements:

I have put in several TO-DO comments within the code that should explain some of the more specific features that should be implemented to make this application more robust. More broadly though, the following should be implemented.

1. Further utilise [dataclasses](https://docs.python.org/3/library/dataclasses.html) so that we are passing around structured objects instead of strings. This would make adding in extra functionality much easier as inputs/outputs are more clearly defined.
2. Put in some actual logging. Could bundle these up with Open Telemetry as it has a fairly [documented Python implementation](https://opentelemetry.io/docs/languages/python/getting-started/). This would allow for better observabillity as we could export and analyse logs without having to view the crashlogs of the application itself.
3. Add in a [mock/monkeypatches](https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html) for the API. Biggest problem here is that free API keys are restricted to 25 calls per day. This would be insufficient if you need to implement/test some functionality that uses the API. I would also suggest creating a dev and prod key so the environments are not interfering with each other.
4. Implement semantic versioning based on Git tags using [poetry-dynamic-versioning](https://pypi.org/project/poetry-dynamic-versioning/)

# Kubernetes Improvements

1. Use the [external-secrets operator](https://external-secrets.io/latest/) to manage the secrets within your chosen secrets manager. This allows us to keep the secrets out of Git and restrict access based on the chosen secrets mnanager instead of giving users permissions on the cluster itself
2. Put in a [HorizontalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) to scale out the number of pods as traffic increases
3. Implement [node scaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/) using [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) or [Karpenter](https://github.com/kubernetes-sigs/karpenter).
4. Use the Gateway API instead of the ingress-nginx class as it is [going EOL on March 2026](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/).
5. Institute an actual CNI instead of [Kindnet](https://github.com/kubernetes-sigs/kindnet) which comes Minikube. Both GKE and EKS come with their own CNI's baked in but it would be worth investigating [Cilium](https://cilium.io/) or [Istio](https://istio.io/) if your looking for network level policies and better network logs. 
6. Observability with [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/).
7. Deploy resources to the cluster using [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) or [Flux](https://fluxcd.io/). 
