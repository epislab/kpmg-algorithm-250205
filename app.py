from flask import Flask, render_template, request, redirect, url_for
from com.epislab.exchange.exchange_controller import ExchangeController
from com.epislab.exchange.exchange_model import ExchangeModel
from com.epislab.knapsack.knapsack_controller import KnapsackController
from com.epislab.knapsack.knapsack_model import KnapsackModel


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/won')
def exchange_won():
    return render_template('exchange_won.html')

@app.route('/dollar')
def exchange_dollar():
    return render_template('exchange_dollar.html')


@app.route('/knapsack', methods=["POST", "GET"])
def knapsack():
    if request.method == "POST" :
        max_capacity = int(request.form.get('max_capacity'))
        profit1 = int(request.form.get('profit1'))
        weight1 = int(request.form.get('weight1'))
        profit2 = int(request.form.get('profit2'))
        weight2 = int(request.form.get('weight2'))
        profit3 = int(request.form.get('profit3'))
        weight3 = int(request.form.get('weight3'))
        profit4 = int(request.form.get('profit4'))
        weight4 = int(request.form.get('weight4'))
        controller = KnapsackController(max_capacity = max_capacity,
                                        profit1 = profit1, weight1 = weight1, profit2 = profit2,
                                        weight2 = weight2, profit3 = profit3, weight3 = weight3,
                                          profit4 = profit4, weight4 = weight4)
        resp : KnapsackModel = controller.getResult()
        render_html = '<h1>결과보기</h1>'
        return render_template("knapsack.html", render_html = render_html)
    else:
        return render_template('knapsack.html')






@app.route('/exchange', methods=["POST", "GET"] )
def exchange():
    print("💰거스름돈 계산기💰")
    if request.method == "POST" :
        print("😊POST 접근😊")       
        currency = request.form.get('currency') # USD, WON 상수
        amount = int(request.form.get('amount'))
        print("amount: ", amount)


        controller = ExchangeController(amount=amount, currency=currency)

        resp : ExchangeModel = controller.get_result()

        render_html = '<h1>결과보기</h1>'
        render_html += resp.result

        return render_template(resp.page, 
                               render_html=render_html)

    else:
         print("😊GET 접근😊")
         return render_template('exchange_won.html')




if __name__ == '__main__':
    app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True