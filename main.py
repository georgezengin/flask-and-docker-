# pip3 install flask
import datetime
import json
import os

from flask import Flask, render_template, request

app = Flask('george_app')  # create flask instance

foods = [{'id': 1, 'name': 'jahnoon', 'score': 6, 'calories': 400}
    , {'id': 2, 'name': 'shawarma', 'score': 9, 'calories': 2000}
    , {'id': 3, 'name': 'T-bone', 'score': 10, 'calories': 500}
    , {'id': 4, 'name': 'asado', 'score': 1, 'calories': 1000}]


@app.route('/foods',methods=['POST'])
def add_new_food():
    newFood=request.get_json()
    foods.append(newFood)
    return {'status':'success'}


@app.route('/foods', methods=['GET'])
def get_all_foods():
    return foods


@app.route('/foods', methods=['DELETE'])
def delete_all_foods():
    foods.clear()
    return foods


@app.route('/foods/<int:id>', methods=['GET'])
def get_food_by_id(id):
    try:
        for food in foods:
            if food['id'] == id:
                return food
        return 'no id '
    except:
        return 'we have internal problems we will contact you when we solve them'


@app.route('/welcome')
def welcome_page():
    return f'<h1>welcome to out flask application {datetime.datetime.now()}</h1>'


@app.route('/html')
def render_html():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=os.environ.get('PORT'))
