from flask import Flask, render_template, request, redirect, url_for
from com.epislab.exchange.exchange_controller import ExchangeController
from com.epislab.exchange.exchange_model import ExchangeModel


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"] )
def index():
    return render_template('index.html')



@app.route('/exchange', methods=["POST", "GET"] )
def paid():
    print("💰거스름돈 계산기💰")
    if request.method == "POST" :
        print("😊POST 접근😊")       
        amount = int(request.form.get('amount'))
        print("amount: ", amount)


        controller = ExchangeController(amount=amount)

        resp : ExchangeModel = controller.get_result()

        render_html = '<h1>결과보기</h1>'
        render_html += resp.result

        return render_template('exchange_won.html', 
                               render_html=render_html)

    else:
         print("😊GET 접근😊")
         return render_template('exchange_won.html')




if __name__ == '__main__':
    app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True