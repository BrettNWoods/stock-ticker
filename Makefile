test:
	poetry run pytest

local:
	poetry run python3 main.py

build:
	docker build -t stock-ticker:latest .

# I have Fedora as my local system which causes [problems](https://github.com/kubernetes/minikube/issues/17638#issuecomment-1853999005) as it defaults to the [qmeu driver](https://minikube.sigs.k8s.io/docs/drivers/qemu/) using builtin networking. Use the docker driver instead
minikube:
	minikube start --driver docker
	minikube addons enable ingress

deploy:
	minikube image load stock-ticker:latest
	minikube kubectl -- apply -f infrastructure/k8s

