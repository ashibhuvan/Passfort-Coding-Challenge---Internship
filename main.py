from flask import Flask
from flask import request
from flask import json
from flask import Response
from datetime import date
app = Flask(__name__)


data = []
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
 
data.append(example)
data.append(example2)
print(data)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/documents')
def api_documents():
	
	data_titles=[]
	for i in range(len(data)):
		data_titles.append({'document_title':data[i]['title']})
	js = json.dumps(data)
	js2 = json.dumps(data_titles)
	resp = Response(js2, status=200, mimetype='application/json')
	
	return resp

@app.route('/documents/<title>',methods=['GET','PUT'])
def api_title(title):
	data_titles=[]
	for i in range(len(data)):
		data_titles.append(data[i]['title'])
	if request.method == 'GET':
		if any(title in s for s in data_titles):
			number = data_titles.index(title)
			js = data[number]['documents']
			js3 = json.dumps(js)
			resp = Response(js3, status = 200, mimetype='application/json')
			return resp	
		else:
			resp = Response(response={'response':'error not found'},status = 400, mimetype='application/json')
			return resp 
	elif request.method == 'POST':
		if any(title in s for s in data_titles):
			number = data_titles.index(title)
			new_data = request.json
			data[number]['documents'].append(new_data['content'])
			data[number]['dates'].append(str(date.today()))
		else:
			resp = Response(response={'response':'title not found'},status = 400, mimetype='application    /json')
                      	return resp

@app.route('/documents/<title>/latest')
def api_title_latest(title):
	data_titles=[]
        for i in range(len(data)):
                data_titles.append(data[i]['title'])
        if request.method == 'GET':
                if any(title in s for s in data_titles):
                        number = data_titles.index(title)
			latest =len(data[number]['documents'])-1
                        js = data[number]['documents'][latest]
                        js3 = json.dumps(js)
                        resp = Response(js3, status = 200, mimetype='application/json')
                        return resp    
                else:
			 resp = Response(response={'response':'error not found'},status = 400, mimetype='application/json')
                 	 return resp


@app.route('/documents/<title>/<timestamp>')
def api_timestamp(title,timestamp):
	data_titles=[]
        for i in range(len(data)):
                data_titles.append(data[i]['title'])
	if any(title in s for s in data_titles):
		revision_dates = []
		title_index = data_titles.index(title)
	
		for i in range(len(data[title_index]['dates'])):
			revision_dates.append(data[title_index]['dates'][i])
		print(revision_dates)
		if any(timestamp in j for j in revision_dates):
			date_index = revision_dates.index(timestamp)
			js = data[title_index]['documents'][date_index]
			js4 = json.dumps(js)
			resp = Response(js4, status = 200, mimetype='application/json')
                        return resp
		
		else:

			 resp = Response(response={'response':'that timestamp not found'},status = 400, mimetype='application/json')
                         return resp
		
	else:
		 resp = Response(response={'response':'title not found'},status = 400, mimetype='application/json')
                 return resp

@app.route('/test_page')
def test_page_fn():
	return type(data)
