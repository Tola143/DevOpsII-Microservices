from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/update/<username>', methods=['POST'])
def update(username):
    # username = str(username)
    # Get the user's login information from the request
    user = request.form.get('username')
    passwd = request.form.get('password')
    name = request.form.get('name')

    _user = us.user_name()
    data = [x for x in _user if x["user"]==username]

    if (data):
        us.update_name(user, passwd, name)
        return jsonify({'message': 'Updated successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot update user.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True) #127.0.0.1