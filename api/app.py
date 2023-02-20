from flask import Flask, jsonify, abort, request
import mariadb
import urllib.parse
from datetime import datetime

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False  # pour utiliser l'UTF-8 plutot que l'unicode


def execute_query(query, data=()):
    config = {
        'host': 'mariadb',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'ACME'
    }
    """Execute une requete SQL avec les param associés"""
    # connection for MariaDB
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    # execute a SQL statement
    cur.execute(query, data)

    if cur.description:
        # serialize results into JSON
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        list_result = []
        for result in rv:
            list_result.append(dict(zip(row_headers, result)))
        return list_result
    else:
        conn.commit()
        return cur.lastrowid


# we define the route /
@app.route('/')
def welcome():
    liens = [{}]
    liens[0]["_links"] = [{
        "href": "/customers",
        "rel": "customers"
    }]
    return jsonify(liens), 200

""" 
    ##########################################
    ############### customers ################
    ##########################################
"""


@app.route('/customers')
def get_all_customers():
    """recupère la liste des customers"""
    customers = execute_query("select * from customers")
    # ajout de _links à chaque dico customer
    for i in range(len(customers)):
        customers[i]["_links"] = [
            {
                "href": "/customers",
                "rel": "self"
            },
            {
                "href": "/customers/" + urllib.parse.quote(customers[i]["email"]),
                "rel": "self"
            }
        ]
    return jsonify(customers), 200


@app.route('/customers/<string:id>')
def get_customer(id):
    """"Récupère les infos d'un customer en paramètre"""
    customer = execute_query("select * from customers where id=?", (id,))
    return jsonify(customer), 200

@app.route('/customers', methods=['POST'])
def post_customer():
    """"Ajoute un customer"""
    firstname = request.args.get("firstname")
    name      = request.args.get("name")
    email     = request.args.get("email")
    created   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    customers = execute_query("select id from customers")
    id        = max([customer["id"] for customer in customers])+1
    execute_query("insert into customers (id, firstname, name, email, created) values (?,?,?,?,?)", (str(id), firstname, name, email, created))
    # on renvoi le lien du customer que l'on vient de créer
    reponse_json = jsonify({
        "_links": [{
            "href": "/customers/" + str(id),
            "rel": "self"
        }]
    })
    return reponse_json, 201  # created

@app.route('/customers/<string:id>', methods=['PUT'])
def put_customer(id):
    """"modifie un customer"""
    firstname = request.args.get("firstname")
    name      = request.args.get("name")
    email     = request.args.get("email")
    created   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    execute_query("UPDATE customers SET firstname=?, name=?, email=?, created=? WHERE id=?", (firstname, name, email, created, id))
    # on renvoi le lien du customer que l'on vient de modifier
    reponse_json = jsonify({
        "_links": [{
            "href": "/customers/" + id,
            "rel": "self"
        }]
    })
    return reponse_json, 201  # created


@app.route('/customers/<string:id>', methods=['DELETE'])
def delete_customers(id):
    """supprimer un customer"""
    execute_query("delete from customers where id=?", (id,))
    return "", 204  # no data



""" 
    ##########################################
    ################## MAIN ##################
    ##########################################
"""


if __name__ == '__main__':
    # define the localhost ip and the port that is going to be used
    app.run(host='0.0.0.0', port=5000)
