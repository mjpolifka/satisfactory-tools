
# Satisfactory Tools

## Installation:
Must have Python installed, I used version 3.10  
If you don't already have pipenv installed, run `pip install pipenv`

In the terminal, navigate to the satisfactory-tools folder and run `pipenv install` to create a virtual environment and install all dependencies.

You should be ready to run!

## To run:
Set environment variables:

    Windows CMD:
    - set FLASK_ENV=development
    - set FLASK_APP=app.py

    Windows PowerShell:
    - $env:FLASK_ENV="development"
    - $env:FLASK_APP="app.py"

    Linux/Unix/(?Mac?):
    - TODO

Run `flask run` to start the development server.  
In your browser, navigate to http://localhost:5000/init_db/ the first time you run it.

Then to access the app, navigate to http://localhost:5000/


## "Documentation" (basically just some notes for now):

uses `flask` and `flask-sqlalchemy`, with an sqlite database  
doesn't do much yet


## TODO List

### In-Progress
- ~~in components/index.html make each item a link to /components/$id~~
    - ~~create a new view for an individual component~~
        - ~~show the ingredients for the item~~
        - ~~show the quantity made per cycle, per minute, and ingredients per cycle and per minute~~
        - ~~show the cycle time~~
        - eventually show the ingredients for all ingredients back to an item with a made_in in ('by_hand', 'miner')
        - after that, be able to limit the output needed and recalculate all the ingredients

### Planning
- haven't figured out the 'by_hand' items yet
- need to start calculating items per minute, I'm guessing it's a function shared by everything
- could use some styling, probably bootstrap
- is there a way to make this callable as an api without decoupling the templates?
    - if not, start considering when is a good time to refactor this into frontend/backend

### Complete
- ~~Homepage (components/index.html | components.py/index) should group components by where they're made~~