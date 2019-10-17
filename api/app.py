import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, User, Text
from flask_cors import CORS

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'config.DevelopmentConfig'
)
app.config.from_object(app_settings)

app.config['JWT_SECRET_KEY'] = 'ss_ss_ss'
jwt = JWTManager(app)
db.init_app(app)

CORS(app)

##to create access token
@app.route('/login', methods=['POST'])
def login():
	if not request.is_json:
		return jsonify({"msg": "No json request"}), 400

	username = request.json.get('username', None)
	password = request.json.get('password', None)

	if not username:
		return jsonify({"msg": "Missing username param"}), 400
	if not password:
		return jsonify({"msg": "Missing password param"}), 400

	u = User.query.filter_by(username=username).first()
	
	if not u:
		return jsonify({"msg": "no such user"}), 400
	
	if username != u.username or password != u.password:
		return jsonify({"msg": "incorrect user or password"}), 401


	access_token = create_access_token(identity=username)
	return jsonify(user_id=u.id, access_token=access_token), 200

#login 
#
@app.route('/register', methods=['POST'])
def register():
	if not request.is_json:
		return jsonify({"msg": "No json request"}), 400

	username = request.json.get('username', None)
	password = request.json.get('password', None)

	if not username:
		return jsonify({"msg": "Missing username param"}), 400
	if not password:
		return jsonify({"msg": "Missing password param"}), 400

	try:
		u = User(username=username, password=password)
		
		db.session.add(u)
		db.session.commit()
	except Exception as e:
		print(e)
		return jsonify({"msg": "error creating user"}), 400

	
	return jsonify({"msg": "user created succesfully"}), 200


@app.route('/text', methods=['POST'])
@jwt_required
def post_text():
	if not request.is_json:
		return jsonify({"msg": "No json request"}), 400

	user_id = request.json.get('user_id', None)
	text = request.json.get('text', None)

	if not text:
		return jsonify({"msg": "No text inserted"}), 400

	if get_jwt_identity() == User.query.filter_by(id=user_id).first().username:
		try:
			t = Text(user_id=user_id, text=text)
			
			db.session.add(t)
			db.session.commit()
		except Exception as e:
			print(e)
			return jsonify({"msg": "error texting"}), 400
	else:
		return jsonify({"msg": "error"}), 400

	return jsonify({"msg": "text created succesfully"}), 200
 	
@app.route('/text', methods=['GET'])
@jwt_required
def get_text():
	#if not request.is_json:
	#	return jsonify({"msg": "No json request"}), 400

	try:
		texts = Text.query.order_by(Text.texted_on.desc()).all()
		texts_dic = [x.dictionarize() for x in texts]
		
	except Exception as e:
		print(e)
		return jsonify({"msg": "error getting texts"}), 400

	return jsonify(texts_dic), 200

@app.route('/text/<text_id>', methods=['GET'])
@jwt_required
def get_text_id(text_id):
	try:
		texts = Text.query.filter_by(id=text_id)
		texts_dic = [x.dictionarize() for x in texts]
	except Exception as e:
		print(e)
		return jsonify({"msg": "error getting texts"}), 400

	return jsonify(texts_dic), 200

@app.route('/text/<text_id>', methods=['DELETE'])
@jwt_required
def delete_text(text_id):
	try:
		text = Text.query.filter_by(id=text_id).first()
		db.session.delete(text)
		db.session.commit()
	except Exception as e:
		print(e)
		return jsonify({"msg": "error deleting texts"}), 400

	return jsonify({"msg": "text deleted succesfully"}), 200


@app.route('/<user_id>', methods=['GET'])
@jwt_required
def get_text_user(user_id):
	try:
		texts = Text.query.filter_by(user_id=user_id)
		texts_dic = [x.dictionarize() for x in texts]
	except Exception as e:
		print(e)
		return jsonify({"msg": "error getting texts"}), 400

	return jsonify(texts_dic), 200


#test if running
@app.route('/')
def test():
	return "test"

@app.route('/test_running')
def test_running():
	return jsonify(
			{
				"is_running": True,
				"appname": "text-app-jwt"
			}
		), 200


#test if the jwt is working
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
	current_user = get_jwt_identity()
	print(current_user)
	return jsonify(logged_in_as=current_user), 200

#a little documentation to remember what I did without having to open the source file
@app.route('/doc')
def doc():
	return '''
		/				-		return test<br>
		/login 			POST	required json 	params:username/password <br>
		/register 		POST	required json 	params:username/password<br>
		/protected		GET		test protected, should return the identity(username)<br>
		/test_running 	-		return json with fields is_running and appname<br>
		/text 			POST 	required json 	params:user_id/text<br>
		/text 			GET 	return json list of texts, each text  has -> {user_id text texted_on}<br>
		/text/<user_id> GET 	required json 	params in url user_id returns json list<br>
	'''

if __name__ == '__main__':
	app.run()
 