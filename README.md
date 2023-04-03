# **KoPylot**: Your AI-Powered Kubernetes Assistant 🤖

[![Release](https://img.shields.io/github/v/release/avsthiago/kopylot)](https://img.shields.io/github/v/release/avsthiago/kopylot)
[![Build status](https://img.shields.io/github/actions/workflow/status/avsthiago/kopylot/main.yml?branch=main)](https://github.com/avsthiago/kopylot/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/avsthiago/kopylot/branch/main/graph/badge.svg)](https://codecov.io/gh/avsthiago/kopylot)
[![Commit activity](https://img.shields.io/github/commit-activity/m/avsthiago/kopylot)](https://img.shields.io/github/commit-activity/m/avsthiago/kopylot)
[![License](https://img.shields.io/github/license/avsthiago/kopylot)](https://img.shields.io/github/license/avsthiago/kopylot)

Kopylot is an open-source AI-powered Kubernetes assistant. Its goal is to help developers and DevOps engineers to easily manage and monitor their Kubernetes clusters. 

KoPylot's idea is similar to [Kopilot](https://github.com/knight42/kopilot) from knight42. The main difference at the moment is the usage of Python for implementing it. 

> *Note from the author*: I decided to create a new project instead of contributing to Kopilot mainly because I am a Python developer, and Kopilot is written in Go. I also believe that the tools for interacting with large language models are more mature in the Python ecosystem.

## 🔧 Features:


- 🚧👷‍♀️ **Under Construction!** 👷🚧


## 🚀 Quick Start:

1. Requests an API key from [OpenAI](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).
2. Export the key using the following command:

```bash
export KOPYLOT_AUTH_TOKEN=your_api_key
```
3. Install Kopylot using pip:
```
pip install kopylot
```

4. Run Kopylot:
```
kopylot --help
```


## 📖 Usage:

```
Usage: kopylot [OPTIONS] COMMAND [ARGS]...                                           
                                                                                      
╭─ Options ──────────────────────────────────────────────────────────────────────────╮
│ --version                                                                          │
│ --install-completion        [bash|zsh|fish|powershell  Install completion for the  │
│                             |pwsh]                     specified shell.            │
│                                                        [default: None]             │
│ --show-completion           [bash|zsh|fish|powershell  Show completion for the     │
│                             |pwsh]                     specified shell, to copy it │
│                                                        or customize the            │
│                                                        installation.               │
│                                                        [default: None]             │
│ --help                                                 Show this message and exit. │
╰────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────╮
│ audit     Audit a pod, deployment, or service using an LLM model.                  │
│ chat      Start a chat with kopylot to generate kubectl commands based your        │
│           inputs.                                                                  │
│ ctl       A wrapper around kubectl. The arguments passed to the ctl subcommand are │
│           interpreted by kubectl.                                                  │
│ diagnose  Diagnose a resource e.g. pod, deployment, or service using an LLM model. │
╰────────────────────────────────────────────────────────────────────────────────────╯
```

## 👥 Contributors:

Kopylot is an open-source project and we welcome contributions from the community. If you are interested in contributing, please fork the repository and submit a pull request. We also welcome feedback and suggestions on how we can improve Kopylot.

### Getting started as a contributor


``` bash
git clone https://github.com/avsthiago/kopylot.git
cd kopylot
```

Install the environment and the pre-commit hooks with

```bash
make install
```

## 📄 License:

Kopylot is licensed under the MIT License. See [LICENSE](LICENSE) for more information.


## 📞 Contact: 

If you have any questions or suggestions, feel free to contact me on [https://thiagoalves.ai](https://thiagoalves.ai/contact/).

Thank you for using Kopylot! 🙌
