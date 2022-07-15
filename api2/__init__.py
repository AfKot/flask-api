from flask import Flask, Response, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ingredients():
    food = (requests.get('http://localhost:5001/get/food')).text
    if food == 'Pizza':
        ingredient = 'Cheese'
    elif food == 'Lobster':
        ingredient = 'Seafood'
    else:
        ingredient = 'Chickens!'
    return render_template('home.html', food=food, ingredient=ingredient)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')