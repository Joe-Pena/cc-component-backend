# CC Component Backend

Super simple Django backend for the cc component. The db was seeded by using the example JSON file as a fixture.

## Live API

You can find the live api at https://joepena.pythonanywhere.com/api/recommendations/

Query Parameter can be passed in in order to filter the card recommendations.

eg. https://joepena.pythonanywhere.com/api/recommendations?score=good&usage=travel

## Getting Started Locally

1. Pull the repo
   > `git clone https://github.com/Joe-Pena/cc-component-backend.git`
2. Create a virtual env at the root folder
   > `python -m venv env`
3. Login to the virtual env
   > `source env/bin/activate`
4. **While logged into the venv shell** Install the required packages
   > `pip install -r requirements.txt`
5. cd into the backend project
   > `cd backend/`
6. Make sure to run a migration
   > `python manage.py migrate`
7. Start the API!
   > `python manage.py runserver`
