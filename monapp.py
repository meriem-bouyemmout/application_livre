from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)



@app.route("/index.html")
def bonjour():
    return render_template("index.html")


@app.route("/inscription.html")
def inscription():
    return render_template("inscription.html")

@app.route("/traitement.html", methods=['POST', 'GET'])    
def traitement():
    if request.method == 'POST':
       d = request.form
       nom1 = request.form['nom']
       prénom1 = request.form['prénom']
       email1 = request.form['email']
       tel1 = request.form['tel']
       password1 = request.form['password']
       de =[(nom1, prénom1, email1, tel1, password1)]
       conn = sqlite3.connect('client.db')
       cur = conn.cursor()
       for i in de:
        req="insert into client(nom, prénom, email, tel, password) values (?, ?, ?, ?, ?) "
       cur.execute(req, i)
       conn.commit()
       conn.close()
    return render_template("traitement.html")


@app.route("/livre.html")
def livre():
    return render_template("livre.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/connexion.html")
def connexion():
    return render_template("connexion.html")

@app.route("/panier.html")
def panier():
    return render_template("panier.html")    


@app.route("/traitements.html", methods=["POST", "GET"])
def traitements():
    if  request.method == "POST":
        donnees = request.form
        no = donnees.get('nom')
        mdp = donnees.get('password')
        te  = [(no,mdp)]
    
        if no == 'admin' and mdp == '1234':         
         return render_template("admin.html")
        else:
              
         conn = sqlite3.connect('client.db')
         cur = conn.cursor()
        
         for i in te :
        
          req  = "select nom from client where nom = ? and password =?  "                       
         cur.execute(req,i)       
         res = cur.fetchall()
        
         conn.commit()
         conn.close()
        
         if res == [] : 
           return render_template("invalider.html")
         else : 
           return render_template("traitements.html")

@app.route("/update_data/<string:id>", methods=["POST","GET"])
def update_data(id):
    conn = sqlite3.connect('client.db')
    cur = conn.cursor()
    req  = "SELECT * FROM livre where Prix = ? " 
    cur.execute(req,(id,))       
    x = cur.fetchall()
    print(x)
    conn.close()
    if  request.method == "POST" :
      
       nom = request.form['nom_de_livre']
       prix = request.form['Prix']
       type = request.form['Type']
       t = [(nom,prix,type,id)] 
       conn = sqlite3.connect('client.db')
       cur = conn.cursor()
       for i in t :
        req  = "UPDATE livre SET Nom=?, Prix=?, Type=? where Prix=? "  
        print(i)
       cur.execute(req,i)
       conn.commit()      
       conn.close()
       return redirect(url_for("insert"))
        


    return render_template("update_data.html",data=x) 

@app.route("/client.html")
def client():
    conn = sqlite3.connect('client.db')
    conn.row_factory=sqlite3.Row
    cur = conn.cursor()
    req  = "SELECT * FROM client "  
    cur.execute(req)       
    x = cur.fetchall()
            
    return render_template("client.html",data=x)    

@app.route("/livre_data.html")
def livre_data():
    conn = sqlite3.connect('client.db')
    conn.row_factory=sqlite3.Row
    cur = conn.cursor()
    req  = "SELECT * FROM livre "  
    cur.execute(req)       
    x = cur.fetchall()
            
    return render_template("livre_data.html",data=x)    

@app.route("/location.html")
def location():
            
    return render_template("location.html")        

@app.route("/insert/<string:total>", methods=["POST","GET"])
def insert(total):       
    x = total
    if  request.method == "POST" :
      
       noml = request.form['noml']
       location = request.form['location']
       type = request.form['Type']
       t = [(noml,location,total)] 
       conn = sqlite3.connect('client.db')
       cur = conn.cursor()
       for i in t :
        req  = "insert into panier(nom,location,somme_total) values (?,?,?) "  
        print(i)
       cur.execute(req,i)
       conn.commit()      
       conn.close()
       return redirect(url_for('merci'))
        


    return render_template("insert.html",total=x) 


"""@app.route("/insert_into_panier/<string:total>", methods=['POST', 'GET'])    
def insert_into_panier(total):
    x = total
    if request.method == "POST":
       d = request.form
       noml = request.form['noml']
       location = request.form['location']
       t = [(noml,location,x)]
       conn = sqlite3.connect('client.db')
       cur = conn.cursor()
       for i in t :
        req="insert into Panier(nom,location,somme_total) values (?,?,?) "
       cur.execute(req,i)
       conn.commit()
       conn.close()
       return render_template("merci.html")
    return render_template("insert_into_panier.html",total=x)
    
@app.route("/merci.html")
def merci():          
    return render_template("merci.html")        

     

@app.route("/location.html",methods=['POST', 'GET'])    
def location():
    if request.method == 'POST':
       d = request.form
       noml = request.form['noml']
       location = request.form['location']
       total = request.form['total']
       t = [(noml,location,total)]
       conn = sqlite3.connect('client.db')
       cur = conn.cursor()
       for i in t :
        req="insert into Panier(nom,location) values (?,?) where somme_total=? "
       cur.execute(req,i)
       conn.commit()
       conn.close()
    return "kda mena mlhih" """
    


if __name__ == '__main__':
    app.run(debug=True)