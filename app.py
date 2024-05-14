from flask import Flask, request, render_template, url_for, redirect, flash, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

app.secret_key='1359'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='KIRUBAkaran1234'
app.config['MYSQL_DB']='API'
mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    
    cur=mysql.connection.cursor()
    cur.execute('select * from student_details')
    data=cur.fetchall()
    cur.close()

    return render_template('index.html',data=data)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        
        data = request.get_json()
        name=data['Name']
        age=data['Age']
        roll_no=data['Roll_no']  
        mark1=data['mark1']
        mark2=data['mark2']
        mark3=data['mark3']
        mark4=data['mark4']
        mark5=data['mark5']
            
        cur=mysql.connection.cursor()
        cur.execute('insert into student_details (Name,Age,Roll_no,mark1,mark2,mark3,mark4,mark5) values (%s,%s,%s,%s,%s,%s,%s,%s)',(name,age,roll_no,mark1,mark2,mark3,mark4,mark5))
        cur.connection.commit()
        cur.close()

        return redirect(url_for('home'))
    return render_template('index.html')
      
@app.route('/put/<int:id>',methods=['PUT'])
def put(id):
    
    data = request.get_json()
    name=data['Name']
    age=data['Age']
    roll_no=data['Roll_no']  
    mark1=data['mark1']
    mark2=data['mark2']
    mark3=data['mark3']
    mark4=data['mark4']
    mark5=data['mark5']
            
    cur=mysql.connection.cursor()
    cur.execute('update student_details set Name=%s,Age=%s,Roll_no=%s,mark1=%s,mark2=%s,mark3=%s,mark4=%s,mark5=%s where id=%s',
                (name,age,roll_no,mark1,mark2,mark3,mark4,mark5,id))
    cur.connection.commit()
    cur.close()
    
    return jsonify({'Message':'Updated Successfuly'})

@app.route('/patch/<int:id>',methods=['PATCH'])
def patch(id):
    
    data = request.get_json()
    name=data['Name']
    age=data['Age']
    roll_no=data['Roll_no']  
    mark1=data['mark1']
    mark2=data['mark2']
    mark3=data['mark3']
    mark4=data['mark4']
    mark5=data['mark5']
            
    cur=mysql.connection.cursor()
    cur.execute('update student_details set Name=%s,Age=%s,Roll_no=%s,mark1=%s,mark2=%s,mark3=%s,mark4=%s,mark5=%s where id=%s',
                (name,age,roll_no,mark1,mark2,mark3,mark4,mark5,id))
    cur.connection.commit()
    cur.close()
    
    return jsonify({'Message':'Updated Successfuly'})

@app.route('/delete/<string:id>',methods=['GET','POST','DELETE'])
def delete(id):
    
    cur=mysql.connection.cursor()
    cur.execute('delete from student_details where id=%s',(id,))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)