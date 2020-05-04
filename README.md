# CC Component Backend

Super simple Django backend for the cc component. The db was seeded by using the example JSON file as a fixture.

## Live API

You can find the live api at https://joepena.pythonanywhere.com/api/recommendations/

Query Parameter can be passed in in order to filter the card recommendations.

eg. https://joepena.pythonanywhere.com/api/recommendations?score=good&usage=travel

## Getting Started Locally

1. Pull the repo
   > `TODO`
2. Create a virtual env at the root folder.
   > `python -m venv env`
3. Install the required packages
   > `pip install -r requirements.txt`
4. cd into the backend project
   > `cd backend/`
5. Make sure to run a migration
   > `python manage.py migrate`
6. Start the API!
   > `python manage.py runserver`
