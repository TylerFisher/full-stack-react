![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# full-stack-react-example

### Quickstart

First, install requirements and load data

```
$ cd example
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run python manage.py loaddata fixtures.json
$ cd ../fullstack/staticapp
$ npm install
```

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server. Note that you need the Python server running in a separate tab.

  ```
  $ cd fullstack/staticapp
  $ npm start
  ```
