
# Satisfactory Tools

## To run:
Set environment variables (examples are in windows cmd):

    Windows CMD:
    - set FLASK_ENV=development
    - set FLASK_APP=app.py

    Windows PowerShell:
    - $env:FLASK_ENV="development"
    - $env:FLASK_APP="app.py"

    Linux/Unix/(?Mac?):
    - TODO

run `flask run` to start the development server  
in your browser, navigate to http://localhost:5000/init_db/ the first time you run it

Then to access the app, navigate to http://localhost:5000/


## "Documentation" (for now, basically just some notes):

uses flask and flask-sqlalchemy, with an sqlite database
doesn't do much yet


## TODO List

### In-Progress
- Homepage (components/index.html | components.py/index) should group components by where they're made

### Planning
- in components/index.html make each item a link to /components/<\id>
    - create a new view for an individual component
        - show the ingredients for the item
        - eventually show the ingredients for all ingredients back to an item with a made_in in ('by_hand', 'miner')
        - after that, be able to limit the output needed and recalculate all the ingredients
- haven't figured out the 'by_hand' items yet
- need to start calculating items per minute, I'm guessing it's a function shared by everything
- could use some styling, probably bootstrap
- is there a way to make this callable as an api without decoupling the templates?
    - if not, start considering when is a good time to refactor this into frontend/backend