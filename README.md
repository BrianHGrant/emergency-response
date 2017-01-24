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

## Port Forwrding:

Port 4545 on guest machine has been forwarded to 4546 on host.

## API Info:

The API is located with the vagrant folder. To access open vagrant box as per instructions above.

    ## open virtual environment
    $ source activate cvdjango

    $ cd proj/emergency_response_api/emergency_data
    ## confirm all migrations are up to date
    $ python manage.py makemigrations
    $ python manage.py migrate

    ## create admin superuser
    $ python manage.py createsuperuser
    ## follow prompts to create username, password, email can be blank

    ## run django app and bind to external IP address

    $ python manage.py runserver 0.0.0.0:4545

    ## to view admin page/browsable endpoints

    ## open your browser in host machine

    ## for admin:

    $ http://localhost:4546/admin
    ## login using superuser info

    ## for endpoints preview:

    $ http://localhost:4546/'endpoint'

    ## ie:

    $ http://localhost:4546/agencies

## Existing API endpoints

    '/incidents' ** - Works, but with memory problems, see issue
    '/agencies'
    '/alarmlevels'
    '/censustracts'
    '/fireblocks' ** - Not working due to current issue

## Pagination
