from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)

#an array with contracts
contracts = [
    {
        "id": 1,
        "agency": "Adimmo",
        "occupant": "Pablo",
        "apartment": "11 rue Duchesne",
        "entry_date" : "2022-02-02",
        "entry_inventory" : True,
        "deposit_payment" : "500",
        "exit_date" : "",
        "exit_inventory" : ""
    },
    {
        "id": 2,
        "agency": "Logimmo",
        "occupant": "Maria",
        "apartment": "1 rue Beaufort",
        "entry_date" : "2022-02-02",
        "entry_inventory" : False,
        "deposit_payment" : "600.60",
        "exit_date" : "2022-03-02",
        "exit_inventory" : True
    },
]

# get and jsonify the data
@app.route("/contractapi/contracts")
def get_contracts():
    """ function to get all contracts """
    return jsonify({"Contracts": contracts})

occupants = [
    {
        "id": 1,
        "firstName": "Laura",
        "lastName": "Rodriguez"
    }
]

# get and jsonify the data
@app.route("/occupantapi/occupants")
def get_occupants():
    """ function to get all occupants """
    return jsonify({"Occupants": occupants})

# # get book by provided 'id'
# @app.route("/bookapi/books/<int:book_id>", methods=['GET'])
# def get_by_id(book_id):
#     book = [book for book in books if book['id'] == book_id]
#     if len(book) == 0:
#         abort(404)
#     return jsonify({"Book": books[0]})
# 
# #error handling
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({"error": "not found!"}), 404)
# 
# @app.errorhandler(400)
# def not_found(error):
#     return make_response(jsonify({"error": "Bad request!"}), 400)
# 
# 
if __name__ == '__main__':
    app.run(debug=True)