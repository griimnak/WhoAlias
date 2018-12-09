<h1>WhoAlias</h1>

A digital footprint lookup tool / alias scraper coded asynchronously in Python3. 
*Requires no API tokens whatsoever*

#### Usage
```sh
python whoalias.py -p <primary_alias> --alts <alt_alias> <alt_alias2> ..

positional arguments:
  -p, --primary    primary alias to lookup

optional arguments:
  -a, --alts       alternate aliases relevant to primary alias for lookup.
  -h, --help       show this help message and exit.
  -v, --verbosity  increase output verbosity.
```

#### Setup
```sh
# Install virtualenv for python3
$ python3 -m pip install virtualenv

# Make your virtual environment
$ python3 -m virtualenv YOUR_ENV_NAME

# Activate the virtualenv
$ source YOUR_ENV_NAME/Scripts/activate

# Install python requirements from within the environment
(ENV) $ pip install -r requirements.txt
```
