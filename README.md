# picpay-challenge

## Overview

This is an app I made for a job opportunity at PicPay.

Its specification is described [here](docs/data_platform_junior_challenge.pdf).


## Technologies used

- Python 3

- q - Text as Data

- Docker/docker-compose


## How to run it

Since the application is 'dockerized', it's pretty simple to run it:

    $ git clone https://github.com/gwyddie/picpay-challenge
    $ docker-compose build  # this may take a few minutes
    $ docker-compose up

Just clone it and start docker-compose!


## Tests

The Python app contains a few unit tests that you can run and generate a coverage report with:

    $ cd ingest
    $ python -m coverage run -m pytest


Note: don't forget to `pip install -r requirements.txt`.

---

That's all, folks!

Thank you :)
