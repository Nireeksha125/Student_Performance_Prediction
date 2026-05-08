from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app)

# Load ML Model
model = pickle.load(
    open('models/student_model.pkl', 'rb')
)

# Database Table
class Prediction(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    math = db.Column(db.Integer)

    reading = db.Column(db.Integer)

    writing = db.Column(db.Integer)

    result = db.Column(db.String(20))


# Home Page
@app.route('/')
def home():

    return render_template('index.html')


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    # Get User Input
    math = int(request.form['math'])

    reading = int(request.form['reading'])

    writing = int(request.form['writing'])

    # ML Prediction
    prediction = model.predict([
        [math, reading, writing]
    ])

    result = prediction[0]

    # Save Prediction to Database
    new_prediction = Prediction(
        math=math,
        reading=reading,
        writing=writing,
        result=result
    )

    db.session.add(new_prediction)

    db.session.commit()

    # Show Result Page
    return render_template(
        'result.html',
        prediction=result
    )


# Dashboard Route
@app.route('/dashboard')
def dashboard():

    filter_value = request.args.get('filter')

    if filter_value:

        all_predictions = Prediction.query.filter_by(
            result=filter_value
        ).all()

    else:

        all_predictions = Prediction.query.all()

    return render_template(
        'dashboard.html',
        predictions=all_predictions
    )

# Edit Prediction
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    data = Prediction.query.get(id)

    if request.method == 'POST':

        data.math = int(request.form['math'])

        data.reading = int(request.form['reading'])

        data.writing = int(request.form['writing'])

        # New Prediction
        prediction = model.predict([
            [
                data.math,
                data.reading,
                data.writing
            ]
        ])

        data.result = prediction[0]

        db.session.commit()

        return redirect('/dashboard')

    return render_template(
        'edit.html',
        data=data
    )

# Delete Prediction
@app.route('/delete/<int:id>')
def delete(id):

    data = Prediction.query.get(id)

    db.session.delete(data)

    db.session.commit()

    return redirect('/dashboard')

# Run Application
if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(debug=True)