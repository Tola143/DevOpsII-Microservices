from flask import Flask, request, jsonify
import data_item as us

app = Flask(__name__)

@app.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    _user = us.find_item(name)
    data = [x for x in _user if x["name"]== name]
    if data:
        us.delete_item(name)
        return jsonify({'message': 'Deleted'}), 200
    else:
        return jsonify({'message': 'No user in record.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1