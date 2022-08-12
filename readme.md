
# Satisfactory Tools

## Installation:
Must have Python installed, I used version 3.10  
If you don't already have pipenv installed, run `pip install pipenv`

In the terminal, navigate to the satisfactory-tools folder and run `pipenv install` to create a virtual environment and install all dependencies.

You should be ready to run!

## To run:
Set environment variables (can skip if you're not editing the code):

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

Then, to access the app, navigate to http://localhost:5000/


## "Documentation" (basically just some notes for now):

uses `flask` and `flask-sqlalchemy`, with an `sqlite` database  
does more now, but not sure what to document 
the code seems quite readable to me (but of course it would)


## TODO List

### In-Progress
- adding a hand-crafting calculator b/c it should be easy and it's handy
- ~~still needs a lot of help with styling, maybe a color scheme~~
    - ~~index page is decent~~
    - component page needs a lot of help
- haven't figured out the 'by_hand' items yet
    - just add them as if they come from a miner
    - give them a fake time if you have to until we figure out how to detect it

### Planning
- need to create a list of what buildings you need to create the factory
- get an error when I try and recursively get ingredients for miner items
    - I'm trying to click on the raw material... what _should_ it show me?
    - there's also a check in build_ingredients for what building it comes from
- is there a way to make this callable as an api without decoupling the templates?
    - I think there was, it's in the pluralsight that I hated
    - if not, start considering when is a good time to refactor this into frontend/backend

### Thoughts
- if I create an "order" column in the Ingredients in db, I can choose how they appear
- I could add power requirements, I bet that will be important soon
- I need a place on here I can take notes
    - It would be nice if it could follow me from page to page
        - It could be a menu item that's closed when I get to a new page
    - Need to remember how much of a resource I have available, or how many items are coming down this conveyor

### Complete
- ~~Homepage (components/index.html | components.py/index) should group components by where they're made~~
- ~~in components/index.html make each item a link to /components/$id~~
    - ~~create a new view for an individual component~~
        - ~~show the ingredients for the item~~
        - ~~show the quantity made per cycle, per minute, and ingredients per cycle and per minute~~
        - ~~show the cycle time~~
        - ~~eventually show the ingredients for all ingredients back to an item with a made_in in ('by_hand', 'miner')~~
        - ~~after that, be able to limit the output needed and recalculate all the ingredients~~
            - ~~a slider would be sick~~
            - ~~eh, this number box is fine, I usually want to type it anyway~~
- ~~need to start calculating items per minute, I'm guessing it's a function shared by everything~~
    - ~~qpm; did it mostly in my template (in fact, I should move the last remnant - oh, it's needed)~~
- ~~could use some styling, probably bootstrap~~
- ~~in the component template, calculate how many of the main building you need for the qpm entered~~