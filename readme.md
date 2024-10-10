
# Satisfactory Tools

## About

Various tools for the game "Satisfactory" by Coffee Stain Studios
- Main Page: calculate full list of ingredients and buildings required for component manufacturing.  Click the component you want to manufacture, then adjust the "Qty Per Minute Desired" and click "Calculate".  By default, calculates one building at 100%.
- Hand Crafting Calc: put in the hand crafting details, including how many ingredients in your inventory, and it will calculate how much time it will take.
- Power Calc: only oil is implemented so far.  Enter how much oil you have available to process, and it will calculate: how many refineries you will need to refine fuel, how much waste is generated, how many power plants that fuel can support, and how much power you will generate.
- Re-initialize Database: if you adjust the items in db.py, click this to import them into the sqlite database so they can be used.

## Installation:
Must have Python installed, I used version 3.10  
If you don't already have pipenv installed, run `pip install pipenv`

In the terminal, navigate to the satisfactory-tools folder and run `pipenv install` to create a virtual environment and install all dependencies.

You should be ready to run!

## To Run:
Run `flask run` to start the development server.
In your browser, navigate to http://localhost:5000/init_db/ the first time you run it.

Then, to access the app, navigate to http://localhost:5000/

## Semi-Production Setup (Linux):
I wrote the `sync-and-restart.sh` script awhile ago that runs a "production" server with `gunicorn`, but I never documented the process.  This is my reminder.

## Packages Used:
Uses `flask` and `flask-sqlalchemy`, with an `sqlite` database
Added `python-dotenv` and a `.flaskenv` file to auto-set environment variables.



## TODO List

### In-Progress
- haven't figured out the 'by_hand' items yet
    - just add them as if they come from a miner
    - give them a fake time if you have to until we figure out how to detect it
- ~~need to create a list of what buildings you need to create the factory~~
    - need instead of "miner" to know how much raw material I need
    - probably not same with water extractor, etc - it's because miners have different mk's
- adding a hand-crafting calculator b/c it should be easy and it's handy
    - need to implement 2-ingredient (and 3, 4, etc)
    - can I maybe just leave some ingredients blank?
- adding a power caluclator for building power plants
    - add buildings to model so I can calculate materials required to build the plant (can also do this for components)
    - implement coal
    - implement bio

### Planning
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
- I need a "byproduct" field for Ingredient and to show it on the view
    - Would be sick if I could choose from the various ways to dispose of it and it would build the factory out
- I think we're big enough for a search box now
- Perhaps a drop-down to select the building to filter
- When starting NMS-Tools I realized I'm not handling any user-generated data, never doing any CRUDs.
    - Can/should I get rid of the db entirely?
    - The db gives me tools to handle the relationships for recipes though
    - Which has me wondering if my analysis for building and ingredient counts can be simplified by using the db

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
- ~~still needs a lot of help with styling, maybe a color scheme~~
    - ~~index page is decent~~
    - ~~component page needs a lot of help~~
