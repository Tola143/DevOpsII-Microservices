from flask import Flask, request, jsonify
import data_item as us

app = Flask(__name__)

@app.route('/item/<name>', methods=['GET'])
def item(name):
    _item = us.find_item(name)
    return jsonify(_item)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True) #127.0.0.1
