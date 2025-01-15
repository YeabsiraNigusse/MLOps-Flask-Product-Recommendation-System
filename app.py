from flask import Flask, render_template, request
import pickle
import os

# Initialize Flask app
app = Flask(__name__)

# Load the saved SVD model
model_path = os.path.join('model', 'svd_model.pkl')
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Dummy data for user and product IDs
users = list(range(1, 1001))
products = list(range(1, 501))

@app.route('/')
def index():
    return render_template('index.html', users=users, products=products)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    product_id = int(request.form['product_id'])

    prediction = model.predict(user_id, product_id)
    return render_template('result.html', user_id=user_id, product_id=product_id, predicted_rating=prediction.est)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# features i want to add on this application
# 1. add sign up functionality to add new user. basic details should be required
# 2. add login functionality to login to the application
# 3. welcome the user login by getting the user name from the database and show him dashboard
# 4. the dashboard simply show list of some product recommendation based on the user id
# 5. it would be cool if the user sign up and login have email varificationa and password reset functionality and also login with google.



# As a fix though instead of pridicting the rating by taking the user id and product id, 
# i want product pridiction based on user information
# so when i user logs in with some information the model will pridict products based on that user information.
# so the model take user id and pridict the product rating for each product found in the database 
# so i can sort them and show the top 10 products to the user.