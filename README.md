<h1>WhoAlias</h1>

A digital footprint lookup tool / alias scraper coded asynchronously in Python3. 

*Requires no API tokens whatsoever*


##### Youtube Demonstration <a target="_blank" href="https://www.youtube.com/watch?v=qBQ158C0_co">(Click here)</a>

###### Using least ammount of modules possible
requests, BeautifulSoup

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

Completion Log
-------------------
&#10004; <a href="https://github.com/griimnak/WhoAlias/blob/master/whoalias/instagram.py">instagram.py</a>

&#10006; github.py

&#10006; facebook.py

&#10006; twitter.py

&#10006; linkedin.py

&#10006; google.py
