# Ephemeral models

Demonstrates models in django designed to display data received outside the database.

## Contents

* [Requirements](#requirements)
* [Launch preparation and launch](#launch-preparation-and-launch)
    * [Preparations](#preparations)
    * [Launch](#launch)

## Requirements

Ephemeral models demo requires:
* Python 3.11 and higher. If an older version is installed on the machine, it is recommended to use [pyenv](https://github.com/pyenv);
* Docker whose installation instructions can be found [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-engine---community-1);
* virtualenv which can be installed by running `sudo apt-get install virtualenv` on Debian/Ubuntu.

## Launch preparation and launch

### Preparations

First, you need an API key, register on https://www.weatherapi.com/ to get it.

Then you need to install requirements in virtual environment.

```bash
virtualenv -ppython3 ephemeral-models-env
source ./ephemeral-models-env/bin/activate
cd ephemeral-models # go to the root of the project source tree
pip install -r requirements.txt
```

Then you need to start the db server.

```bash
cd docker && docker compose up -d
```

### Launch

After that, you need to roll migrations and run runserver.

```bash
$ env WEATHER_API_KEY=<your-api-key> DEBUG=true SECRET_KEY=secret python manage.py migrate
$ env WEATHER_API_KEY=<your-api-key> DEBUG=true SECRET_KEY=secret python manage.py runserver
```

Create a superuser and log in with his credentials to http://127.0.0.1/admin/.
