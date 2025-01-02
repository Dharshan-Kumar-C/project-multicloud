from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Data for Insurance Plans and Applications
insurance_plans = [
    {"id": 1, "name": "Health Insurance", "price": 5000},
    {"id": 2, "name": "Car Insurance", "price": 7000},
    {"id": 3, "name": "Home Insurance", "price": 3000},
    {"id": 4, "name": "Life Insurance", "price": 10000},
]

applications = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/plans')
def view_plans():
    return render_template('plans.html', insurance_plans=insurance_plans)

@app.route('/apply', methods=['GET', 'POST'])
def apply_insurance():
    if request.method == 'POST':
        plan_id = int(request.form['plan_id'])
        name = request.form['name']
        email = request.form['email']
        plan = next((p for p in insurance_plans if p['id'] == plan_id), None)
        if plan:
            application = {
                "id": len(applications) + 1,
                "plan_name": plan['name'],
                "price": plan['price'],
                "applicant_name": name,
                "applicant_email": email
            }
            applications.append(application)
            return redirect(url_for('application_history'))
    
    return render_template('apply.html', insurance_plans=insurance_plans)

@app.route('/applications')
def application_history():
    return render_template('applications.html', applications=applications)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

