# Flask web server
Flask web server, where user can to login a user from PostgreSQL database and check unique token.

## Installation

- Install libraries:

```shell
$ pip install Flask
$ pip install flask_sqlalchemy
$ pip install SQLAlchemy
$ pip install pyjwt
$ pip install bs4
$ pip install BeautifulSoup

Download Firefox browser and install geckodriver
```

## Usage

Put geckodriver.exe path to server.py

Put you URI in database.py
   ```shell
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
   ```

## Examples
Run server.py

```python
http://127.0.0.1:5000/webpage
```
Provide a name and submit.

```python
http://127.0.0.1:5000/coin
```
