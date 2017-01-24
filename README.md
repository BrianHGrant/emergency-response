# emergency-response
Simulations, Models, and Visualizations of Portland Fire and Rescue data

## _IMPORTANT_
In order for the vagrant box to install correctly, you _must_ download the file 'fire_db' from the shared
drive and put it into:
emergency-response/vagrant/data

If you forget to download the file and try to run 'vagrant up' it will break, and you will have to
'vagrant destroy' before trying to 'vagrant up' again.

## DB Info:
to log into the DB use:

DB name: fire

username: eruser

password: fire


_BUT_ I set it up so you don't have to enter the password, just hit 'ok' if you are asked for a
password in pgadmin.

## API Info:

The API is located with the vagrant folder. To access open vagrant box as per instructions above.
    ## open virtual environment
    $ source activate cvdjango

    $ cd emergency_response_api/emergency_data
    ## confirm all migrations are up to date
    $ python manage.py makemigrations
    $ python manage.py migrate

    ## create admin superuser
    $ python manage.py createsuper
    ## follow prompts to create username, password, email can be blank

    ## run django app

    $ python manage.py runserver

    ## open second terminal window with second ssh connection to vagrant box

    ## to view admin page/browsable endpoints

    $ firefox

    ## in xquartz/firefox window load admin or desired endpoint site

    ## for admin:

    $ http://localhost:8000/admin
    ## login using superuser info

    ## for endpoints preview:

    $ http://localhost:8000/'endpoint'

    ## ie:

    $ http://localhost:8000/agencies
## Existing API endpoints

    '/incidents'
    '/agencies'
    '/alarmlevels'
    '/censustracts'
    '/fireblocks'
