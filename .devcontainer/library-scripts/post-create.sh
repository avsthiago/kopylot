#!/usr/bin/env bash

set -ex 
k3d cluster list | grep -q k3s-default || (k3d cluster create mycluster > k3d.log 2>&1 && export KUBECONFIG=$(k3d kubeconfig write mycluster))

mkdir -p ~/.kube/
k3d kubeconfig get k3s-default > ~/.kube/config

curl -sSL https://install.python-poetry.org | python3 -