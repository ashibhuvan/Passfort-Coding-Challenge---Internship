

In order to run the file, you will need Python and Flask. To run the application the first command you will need to enter in terminal once entering the directory is:

$ export FLASK_APP=main.py 

The second command to actually start the Flask server is:

$ flask run

From there you should see the following to show the server is running:


[{'dates': ['2012-01-05', '2012-01-06', '2012-01-07'], 'documents': ['This is the first revision of the wiki for setting up api', 'second revision', 'third revision'], 'title': 'API'}, {'dates': ['2012-01-05', '2012-01-06', '2012-01-07'], 'documents': ['this is the first revision for setting up database wiki', 'the second', '2third'], 'title': 'database'}]
 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


I have included some test data to test the API methods I have created. The test data looks as follows:

example = {
        'title':'API',
        'documents':["This is the first revision of the wiki for setting up api","second revision","third revision"],
        'dates': ["2012-01-05","2012-01-06","2012-01-07"]
    }

example2 = {
        'title':'database',
        'documents':["this is the first revision for setting up database wiki","the second","2third"],
        'dates': ["2012-01-05","2012-01-06","2012-01-07"]
    }


I have included example URL's for each of the API's.

GET /documents --> http://127.0.0.1:5000/documents
GET /documents/<title> --> http://127.0.0.1:5000/documents/API or http://127.0.0.1:5000/documents/database
GET /documents/<title>/latest --> http://127.0.0.1:5000/documents/database/latest
GET /documents/<title>/<timestamp> --> http://127.0.0.1:5000/documents/database/2012-01-06


