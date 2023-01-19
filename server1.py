from flask import jsonify
from flask import request
from App import app
import mariadb
import sys

def always():

    try :
        con = mariadb.connect(user="root",password="root",host="localhost",port=3306)
        print("Connected")
        return con
    except mariadb.Error as e :
        
            print(f" Error Connecting to Mariadb server : {e}")
            sys.exit(1)


@app.errorhandler(404)
def not_found(self):
    message = {"status":404 ,'message': 'record not found '}
    response =jsonify(message)
    return response
   


@app.route("/api_v1",methods = ['POST'])
def aff_user():
    global cursor , cur 
    try :
        _json = request.json
        name = _json['name']
        email = _json['email']
        id = _json['id']

        print(name)
        if name and email and request.method == 'POST' :
            print("Dkhalt Hna")
            query = "insert into crud.user(id,nom,email) VALUES  (?,?,?)"
            bin_data=(id,name,email)
            cur = always()
            cursor = cur.cursor()
            
            cursor.execute(query,bin_data)
            
            cur.commit()
            response = jsonify('POST succefully')
            response.status_code = 200
            return response
        else :
            _json = request.json
            name = _json['name']
            email = _json['email']
        
            return not_found()
        
            
    except Exception as es :
        
        print(es)
   


@app.route("/api_v1/supprimer/",methods = ['POST'])
def del_user():
    global cursor , cur 
    try :
        _json = request.json
        id = _json['id']
        

       
        if id and request.method == 'POST' :
            print("Dkhalt Hna")
            query = "delete from  crud.user where id = ?"
            bin_data=(id,)
            cur = always()
            cursor = cur.cursor()
            
            cursor.execute(query,bin_data)
            
            cur.commit()
            response = jsonify('POST succefully')
            response.status_code = 200
            return response
        else :
            _json = request.json
            name = _json['name']
            email = _json['email']
        
            return not_found()
        
            
    except Exception as es :
        
        print(es)
    


@app.route("/api_v1/show/",methods = ['POST'])
def show():
    global cursor , cur 
    try :
        _json = request.json
        table = _json['table']

        if table and request.method == 'POST' :
            print("Dkhalt Hna")
            print(table)
            query = f"SELECT id,nom,email FROM {table}"
            bin_data=(table,)
            cur = always()
            cursor = cur.cursor()
            
            cursor.execute(query,bin_data)
        
            
            list =[]

            for (id, nom , email) in cursor:

                print(nom)

                list.append({"id" :id, "nom":nom,"email":email})
               


            response = jsonify(list)
            response.status_code = 200
            return response
        else :
     
            return not_found()
        
            
    except Exception as es :
        
        print(es)

if __name__ =="__main__":
    app.debug=True
    app.run()


