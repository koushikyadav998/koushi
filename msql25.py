import mysql.connector
from flask import Flask, request, render_template_string

app = Flask(name)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="companyDB"
    )

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Add Employee</h2>
    <form method="POST" action="/add">
        Name: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br>
        Salary: <input type="number" name="salary"><br>
        <input type="submit" value="Add">
    </form>
    
    <h2>Employees</h2>
    <table border="1">
        <tr><th>ID</th><th>Name</th><th>Email</th><th>Salary</th><th>Actions</th></tr>
        {% for emp in employees %}
        <tr>
            <td>{{ emp[0] }}</td>
            <td>{{ emp[1] }}</td>
            <td>{{ emp[2] }}</td>
            <td>{{ emp[3] }}</td>
            <td>
                <a href="/edit/{{ emp[0] }}">Edit</a>
                <a href="/delete/{{ emp[0] }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    salary = request.form['salary']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (first_name, email, salary) VALUES (%s, %s, %s)",
                  (name, email, salary))
    conn.commit()
    conn.close()
    return index()

@app.route('/edit/<int:id>')
def edit_employee(id):
    pass

@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return index()

if name == 'main':
    app.run(debug=True)