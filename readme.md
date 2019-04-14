To run locally
1. Run the main method in ```app.py```
2. open python and test routes which were printed in console

To run in docker:

1. run docker compose up to start database, database console and the app

        User:backend$ docker-compose up

2. Routes are printed in console. Go to


How verification works

User inputs username and password into app.
1. frontend hashes password and or username
2. It then makes a GET request for homepage/notification

        GET http://localhost:5000/<auth>/home

3. if verified return content, otherwise redirect to dumpster


\April 7th\

1. log in functionality
2. put data into DB
3. get data from DB for graphs and statistics
4. azure compatibility
5. get log in page up and see if it can talk with DB
6. get dynamic url and password match
7. session and suth working