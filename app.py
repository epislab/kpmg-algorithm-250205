from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def get_unit_count(amount, won_list):
    money = amount
    won_dict = {}
    for won in won_list:
        won_dict[won] = money // won
        money %= won
    return won_dict

@app.route('/', methods=["POST", "GET"] )
def paid():
    print("💰거스름돈 계산기💰")
    if request.method == "POST" :
        print("😊POST 접근😊")       
        amount = int(request.form.get('amount'))
        print("amount: ", amount)

        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        won_list = [WON_50000, WON_10000, WON_5000,
                        WON_1000, WON_500, WON_100, WON_50, WON_10]
        
        
        won_dict = get_unit_count(amount, won_list)

        for won, count in won_dict.items():
            print(f"{won}원: {count}개")

        render_html = '<h1>결과보기</h1>'
        for won, count in won_dict.items():
            render_html += f"{won}원: {count}개<br/>"

        return render_template('index.html', 
                               render_html=render_html)

    else:
         print("😊GET 접근😊")
         return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True