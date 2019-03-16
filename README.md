### Introduction

This repository is used to setup django projects with below features configured.
- Django Authentication Login and Logout
- Django Templates 
- Django Static files configured
- Bootstrap configured
- Django crispy-forms configured

### Setup Django Boilerplate

- #### Setup Virtual Environment

```sh
$ pip install virtualenv
$ pip install virtualenvwrapper
$ export WORKON_HOME=$HOME/code/.virtualenvs
$ export PROJECT_HOME=$HOME/Documents/Devel
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv djangoenv
```

- #### Setup Django Project

```sh
$ wget https://github.com/rahulroshan96/django_boilerplate/archive/master.zip
$ unzip master.zip
$ mv django_boilerplate-master <Project-Name>
$ cd <Project-Name>
$ sh run.sh
```


### LICENSE
See [MIT](https://github.com/rahulroshan96/django_boilerplate/blob/master/LICENSE)

Free Software, Hell Yeah.