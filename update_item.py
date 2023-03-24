from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/update/<pre_name>', methods=['PATCH'])
def update(pre_name):
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _item = us.username(pre_name)
    
    if (_item):
        print(name, category, price, instock)
        us.update_name(name, category, price, instock)
        return jsonify({'message': 'Updated successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot update user.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True) #127.0.0.1