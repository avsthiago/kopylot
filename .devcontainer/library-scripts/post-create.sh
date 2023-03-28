#!/usr/bin/env bash

set -ex 

# Fix the permissions of the project files
sudo find /workspaces/kopylot -not -user vscode -exec chown vscode:vscode {} \;

# Creates the cluster if it doesn't exist
k3d cluster list | grep -q k3s-default || k3d cluster create mycluster > k3d.log 2>&1

# Stores the kube configurations in the ~/.kube/config
mkdir -p ~/.kube/
k3d kubeconfig get k3s-default > ~/.kube/config

# Installs Poetry
curl -sSL https://install.python-poetry.org | python3 -
