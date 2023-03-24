from flask import Flask, request, jsonify
import datetime

import data_item as us

app = Flask(__name__)

@app.route('/item', methods=['GET'])
def item():
    _item = us.user_name()
    return jsonify(_item)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) #127.0.0.1
