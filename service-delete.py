from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt

import data_user as us

app = Flask(__name__)

# username = us.user_name()

# Find data in json
def _find_user(user, username):
    data = [x for x in username if x["user"]==user]
    return data

@app.route('/delete/<username>', methods=['DELETE'])
def delete(username):
    # username = request.form.get('username')
    
    _user = us.find_username(username)
    user = [x for x in _user if x["user"]==username]
    if user:
        us.delete_user(username)
        return jsonify({'message': 'Deleted'}), 200
    else:
        return jsonify({'message': 'No user in record.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1