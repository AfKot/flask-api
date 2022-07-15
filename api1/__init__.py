from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/get/food', methods=['GET'])
def get_Food():
    food = ['Pizza', 'Lobster', 'Chicken Wings']
    randomnum = random.randint(0,2)
    return Response(food[randomnum], mimetype='text/plain')

# Make app callabale from the command line
if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')