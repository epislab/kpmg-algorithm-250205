from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == "POST":
       print("🦉POST 방식으로 전송")
       amount = request.form.get("amount")
       print(f"고객이 입력한 금액: {amount}")
       coin500 = 20
       coin100 = 30
       
       return render_template("index.html", coin500=coin500, coin100=coin100)
   else :
       print("🥷GET 방식으로 전송")
   
       return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True