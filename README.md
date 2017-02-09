# emergency-response
Simulations, Models, and Visualizations of Portland Fire and Rescue data

## _IMPORTANT_

Before running, you must download the [fire_db_2010](https://drive.google.com/file/d/0B7k-dMOX1R5WOWpTZDdhMFBMUW8/view?usp=sharing) database file from the Hack Oregon Emergency Response shared drive.  

Save it to postgresql/data/ (will need to create folder) within this repo.

## Docker

This API is built using Docker containers. It will be easiest to run using [Docker](https://docs.docker.com/) including Docker-Compose and following steps below. If you would like to run natively see these [steps](#native). Any development work should be made with Docker.

## To Setup:

To run the API for the first time:

  1. Save the database file as discussed above.
  2. cd into the root folder of this repo and run:  
      $ docker-compose up
  3. Allow process to run, will take a few minutes the first time as it needs to build the fresh image.
  4. When completed you most likely will be confronted with an error about unable to find or connect to database.
  5. Open a second terminal window in same directory.
  6. While keeping container running, Configure postgres user, database and load the data by running the following commands in order:  

        ## this command will create the eruser  

        $ docker exec -i emergencyresponseapi_db_1 createuser eruser --username=postgres  

        ## this will create the fire database

        $ docker exec -i emergencyresponseapi_db_1 createdb fire -T template_postgis --username=postgres


        ## this will load the data from the dumpfile  

        $ docker exec -i emergencyresponseapi_db_1 psql --username=postgres fire < postgresql/data/fire_db_2010

  7. Run $ docker-compose up again to start api.

  8. Access the api at:

        $ http://localhost:8000/<endpoint>



## API Info:

    ## to view admin page/browsable endpoints

    ## open your browser in host machine

    ## for admin:

    $ http://localhost:8000/admin
    ## login using superuser info

    ## for endpoints preview:

    $ http://localhost:8000/<endpoint>

    ## ie:

    $ http://localhost:8000/agencies

## Existing API endpoints

    "agencies": "http://localhost:8000/agencies/",  
    "alarmlevels": "http://localhost:8000/alarmlevels/",  
    "censustracts": "http://localhost:8000/censustracts/",  
    "fireblocks": "http://localhost:8000/fireblocks/",  
    "typenaturecodes": "http://localhost:8000/typenaturecodes/",  
    "stations": "http://localhost:8000/stations/",  
    "firestations": "http://localhost:8000/firestations/",  
    "fmas": "http://localhost:8000/fmas/",  
    "mutualaid": "http://localhost:8000/mutualaid/",  
    "responderunits": "http://localhost:8000/responderunits/",  
    "incsitfoundclass": "http://localhost:8000/incsitfoundclass/",  
    "incsitfoundsub": "http://localhost:8000/incsitfoundsub/",  
    "incsitfound": "http://localhost:8000/incsitfound/",  
    "incidents": "http://localhost:8000/incidents/"  

## Pagination

    '/incidents' pagination currently set to 10
    ## To select page:
    'http://localhost:4546/incidents?page=NUM'

## DB Info:
to log into the DB use:

DB name: fire  
username: eruser  
password: fire  

_BUT_ I set it up so you don't have to enter the password, just hit 'ok' if you are asked for a password in pgadmin.

## Native

Provided the correct dependencies and versions are installed one should be able to run api outside of Docker.  

To Run:

  1. You will still need to download and save the dumpfile as directed.
  2. Setup the database, user, and import the data. Commands should be similar to above, removing docker syntax and using your postgres admin account:

      ie:

      $ createuser eruser --username=<YOURNAME>  
      $ createdb fire --username=<YOURNAME>  
      $ psql --username=<YOURNAME> fire < postgresql/data/fire_db_2010  

      * You will get some errors unless you have a user named postgres. This should not effect the usability of the api.  

  3. Alter /emergency_response_api/emergency_response_api/settings.py to have correct postgres hostname, most likely change 'db' to 'localhost'

  4. Migrate the database:

      $ python manage.py migrate  

  5. Run the server:

      $ gunicorn emergency_response_api.wsgi:application -b :8000  
