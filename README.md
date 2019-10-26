-------------------------------------------------  
Python Coding Challenge
-------------------------------------------------    


Instructions were as follows:
Wiki Coding Task
We’d like you to create the backend for a wiki, like Wikipedia. With the following requirements:
1. A wiki is a collection of documents
2. Documents are lumps of plain text. No graphics, attachments, or formatting
3. Each document is uniquely identified by a title that is a maximum of 50 characters in
length. This title does not change for the life of a document
4. A document can have multiple revisions, as it is updated over time. We store all historical
revisions of a document
5. We should be able to view the document as it was at any point in time. E.g. we can use
any timestamp to fetch a revision
Your task is to implement a JSON api with the following endpoints:
GET /documents
This should return a list of available titles.
GET /documents/<title>
This should return a list of available revisions for a document.
GET /documents/<title>/<timestamp>
This should return the document as it was at that timestamp.
GET /documents/<title>/latest
This should return the current latest version of the document.
POST /documents/<title>
This allows users to post a new revision of a document.
It should receive JSON in the form: {content: ‘new content...’}.

Technical implementation requirements:
• The code should be production ready; it should have error handling
• You should write some automated tests around your application
• It is up to you to decide which tests and how to write them

---------------------------------
My Solution


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

The post method for /documents is implemented and works but at this point I was close to 3 hours and wanted to stick to the time constrait, which is why there is no unit testing. If you would like to see unit testing implemented, this is something I am more than happy to do, I just wanted to stay true to the time constraint. Please let me know if you need anything else.


