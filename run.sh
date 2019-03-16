#pip install virtualenv
#pip install virtualenvwrapper
#export WORKON_HOME=$HOME/code/.virtualenvs
#export PROJECT_HOME=$HOME/Documents/Devel
#source /usr/local/bin/virtualenvwrapper.sh

#wget https://github.com/rahulroshan96/django_boilerplate/archive/master.zip
#unzip master.zip
#mv django_boilerplate-master <project_name> // Fix this, mkvirtualenv is not working, not able to create new vent
#cd project_name
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin

