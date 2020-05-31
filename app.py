import firebase_admin
from firebase_admin import credentials, firestore, db
import os
from datetime import datetime
from flask import Flask
from flask import Flask, render_template, redirect, request, url_for, session

PRIVATE_KEY = "static/uwinemotions-firebase-adminsdk-y223w-53aacd7b6b.json"
CRED = credentials.Certificate(PRIVATE_KEY)
firebase_admin.initialize_app(CRED,{'databaseURL':'https://uwinemotions.firebaseio.com'})

db = firestore.client()

app = Flask(__name__, template_folder = 'template', static_url_path = '/static/')

@app.route("/")
@app.route("/index")
def loadHomePage():
	print("Loading Home Page")
	return render_template('index.html')

@app.route('/<path:path>', methods = ['GET'])
def send_file(path):
   strFile = path
   return app.send_static_file(strFile)
   app.use_x_sendfile()

@app.route('/fetchGeopoints', methods=['POST', 'GET'])
def fetchGeopoints():
	user = request.form
	data = {}
	latitude = user["latitude1"]
	longitude = user["longitude1"]
	emoji_id = int(user["emoji_id1"])
	time = datetime.now()
	firebaseDataStore(latitude, longitude, emoji_id, time)
	data = firebaseDataRetrieve()
	#print(loc)
	return render_template('viewHeatMap.html', label = data)
# return render_template('displayHeatMap.html', latitude=latitude, longitude=longitude )
def firebaseDataStore(latitude, longitude, emoji_id, time):
	db = firestore.client()
	docs = db.collection('locations').stream()
	documents_items = 0
	for doc in docs:
		documents_items = documents_items + 1
	doc_ref = db.collection('locations').document(str(documents_items + 1))
	doc_ref.set({
		'emotions': emoji_id,
		'locations': firebase_admin.firestore.GeoPoint(float(latitude), float(longitude)),
		'time': time
	})
def firebaseDataRetrieve():
	docs = db.collection('locations').stream()
	documents_items = 0
	data_retrieve = []
	for doc in docs:
		documents_items = documents_items + 1
		x = doc.to_dict()
		for k, v in x.items():
			if(type(v) == firebase_admin.firestore.GeoPoint):
				latitude = v.latitude
				longitude = v.longitude
			if(k == 'emotions'):
				emotions = v
			elif(k == 'time'):
				time = v;
			else:
				pass;
		data_retrieve.append([emotions, latitude, longitude, time])
		# print([emotions, latitude, longitude, time])
	return data_retrieve
	#return latitude,longitude
@app.route('/viewMap')
def viewMap():
    data = firebaseDataRetrieve()
    print(data)
    print('data retrived')
    return render_template('viewHeatMap.html', label=data)


if __name__ == '__main__':
    ## start API
    app.run()


