# Kime Engine

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Kime is a web app for upscaling and enhancing images using generative adversarial networks. This repository contains the engine which wraps the deep learning model and performs the bulk of the computation. 

## Getting Started

**Step 1: Create a virtual environment and install dependencies.**

Create a new Virtual Environment for the project and activate it. If you don't have the `virtualenv` command yet, you can find installation [instructions here](https://virtualenv.readthedocs.io/en/latest/).

```bash
$ virtualenv venv
$ source venv/bin/activate
```

Next, install the project dependencies, which are listed in `requirements.txt`.

```bash
$ pip install -r requirements.txt
```

**Step 2: Update environment variables and start the server.**

Create a new file named `config.json` and update the new file with your Azure credentials. It should look similar to this:

```json
{
  "storage": {
    "azure": {
      "account_name": "...",
      "access_key": "..."
    }
  },

  "backend": {
    "username": "...",
    "secret_hash": "..."
  },
}
```

Now you are ready to start the backend service:

```bash
$ gunicorn --timeout 120 --max-requests 10 -b 127.0.0.1:3785 engine.__main__:app
```
