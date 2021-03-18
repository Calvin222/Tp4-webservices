from flask import Flask, request, Response
import json
import mysql.connector

app = Flask(__name__)

# Conexion DB
# db = heidisql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="webservices"
# )

task = [{'id':1, 'deadline': '2021-02-18', 'title': 'Tp', 'description': 'tp', 'done':'0'},
{'id':2, 'deadline': '2021-04-22', 'title': 'webservices', 'description': 'aucune idée', 'done':'0'},
{'id':3, 'deadline': '2021-06-28', 'title': 'API', 'description': 'test', 'done':'1'}]

# Route test
# @app.route('/')
# def hello_world():
#     return 'Hello world!'

@app.route('/todo', methods = ['GET', 'POST'])
def todo():
    if request.method == 'GET':
        json_liste = json.dump(task, ensure_ascii=False).encode('UTF-8')
        return Response(json_liste, mimetype='text/json')

        # elif request.method == 'POST':
        #     return '"id":'id',"titre":'+titre+',"description":'+description+',"deadline":'+deadline+''

    elif request.method == 'GET':
        if request.get_json(silent=True) is not None:
            params = request.get_json()
            params1 = params['id']
            params2 = params['deadline']
            params3 = params['title']
            params4 = params['description']
            params5 = params['done']
            task.append({'id':params1, 'deadline':params2, 'title':params3, 'description':params4, 'done':params5})
            return "201 : Created"
        else
            return "400 : Bad request"

@app.route('/task/<id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def Task(id):
    if request.method == 'GET':
        dbcursor = db.cursor()
        dbrequest = "SELECT * From NOMDELATABLEICI Where id" + id
        dbcursor.execute(dbrequest)
        result = dbcursor.fetchall()
        dbcursor.close()
        json_data = json.dump(result, ensure_ascii=False).encode('utf-8')
        return Response(json_data, mimetype='text/json'), 100

        elif request.method == 'PUT':
            dbcursor = db.cursor()
            params = request.get_json()
            title = params['title']
            description = params['description']
            deadline = params['deadline']
            done = params['done']
            dbrequest = "UPDATE NOMDELATABLEICI SET title='', description='' deadline='' done='' WHERE id='' "
            dbcursor.execute(dbrequest)
            dbcursor.close()
            return 100

        elif request.method == 'DELETE':
            dbcursor = db.cursor()
            dbrequest = "DELETE NOMDELATABLEICI WHERE id" + id
            dbcursor.execute(dbrequest)
            return 100

#Delete route to specific todo
@app.route('/todolist/<int:id>', methods=['DELETE'])
def deleteTodo(id):

    connection = connexion_db()
    cursor = connection.cursor()

    if request.method == 'DELETE':

        sql_select_Query = "DELETE FROM todo WHERE id=%s"
        var = [id]

        cursor.execute(sql_select_Query, var)
        return "ok"

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)
