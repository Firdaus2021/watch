#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def f1():
    return render_template("flask1.html")
@app.route('/metro',methods=['GET','POST'])
def form():
    if (request.method=='POST'):
        n1=int(request.form['abc'])
        n2=int(request.form['xyz'])
        print(n1,n2)
        print('sum = ',n1+n2)
        return render_template("flask1.html")

if __name__ == '__main__':
    app.run()


# In[ ]:




