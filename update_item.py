from flask import Flask, request, jsonify
import data_item as us

app = Flask(__name__)

@app.route('/update/<pre_name>', methods=['PUT'])
def update(pre_name):
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    print(name, category, price, instock)

    _item = us.item(pre_name)
    
    id_name = _item[0][0]

    if request.method == "PUT":
        if (id_name == pre_name):
            us.update_item(name, category, price, instock, pre_name)
            return jsonify({'message': 'Updated successfully.'}), 200
        else:
            return jsonify({'message': 'Cannot update user.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True) #127.0.0.1