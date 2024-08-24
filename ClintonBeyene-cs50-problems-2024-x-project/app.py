import os
from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date
import string
import re
import mysql.connector
from flask import send_from_directory
from database import apology, login_required, get_connection, get_connection_from_db, get_blog_from_db, add_application_to_db, get_blog, get_users, get_users_from_db, add_users_to_db, get_login_from_db, get_company, add_company_to_db, get_company_from_db, get_company_login_from_db, add_job_post_to_db

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username

        query = get_login_from_db(username)

        # Ensure username exists and password is correct
        if not query:           
            return apology("Username does not exist", 400)
        elif not check_password_hash(query[0]["hash"], password):
            return apology("invalid password", 403)

        # Remember which user has logged in
        if query:
            user_id = query[0].get('id')  # Retrieve the 'id' value
            if user_id is not None:            
                session["user_id"] = user_id
                # Redirect user to home page
                return redirect("/")
            else:
               flash("user id is not in databse")
        else:
           flash("user id is not found in database")                

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logincompany", methods=["GET", "POST"])
def login_company():
    """Log company in"""

    # Forget any user_id
    session.clear()

    # Company reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username

        company = get_company_login_from_db(username)

        # Ensure username exists and password is correct
        if not company:           
            return apology("Username does not exist", 400)
        elif not check_password_hash(company[0]["hash"], password):
            return apology("invalid password", 403)

        # Remember which user has logged in
        if company:
            user_id = company[0].get('id')  # Retrieve the 'id' value
            if user_id is not None:            
                session["user_id"] = user_id
                flash("Company successfully logged in!")
                # Redirect user to home page
                return render_template("jobpost.html")
            else:
               flash("user id is not in databse")
        else:
           flash("user id is not found in database")                

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("logincompany.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    user = get_users()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        symbols = string.punctuation
        # Check if username was submitted
        if not username:
            return apology("Username is required", 400)
        # Check if password was submitted
        elif not password:
            return apology("Password is required", 400)
        # Check if confirmation password was submitted
        elif not confirmation:
            return apology("Confirmation password is required", 400)
        # Check if password and confirmation match
        elif password != confirmation:
            return apology("Passwords do not match")
        elif not re.search("[a-zA-Z]", password) or not re.search("[0-9]", password) or not re.search(fr"[{symbols}]", password):
            flash("Password must contain at least one letter, one number, and one symbol")
            return apology("Password must contain at least one letter, one number, and one symbol")
        # Query database for existing username
        existing_user = get_users_from_db(username)
        if existing_user:
            return apology("Username already exists", 400)

        # Add user to the database
        add_users_to_db(username, password, confirmation)

        # Query datbase for newly added users

        added_user = get_users_from_db(username)

        if added_user:
            user_id = added_user[0].get('id')  # Retrieve the 'id' value
            if user_id is not None:
            # Remember who is logged in
                session['user_id'] = user_id
                flash("User successfully registered!")
                return redirect("/")
            else:
                flash("User ID not found in the database.")
        else:
            flash("No user data retrieved from the database.")

    else:
        return render_template("register.html")

@app.route("/registercompany", methods=["GET", "POST"])
def register_company():
    """Register user"""
    company = get_company()
    if request.method == "POST":
        username = request.form.get("username")
        companyname = request.form.get("companyname")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        Address = request.form.get("Address")
        symbols = string.punctuation
        # Check if username was submitted
        if not username:
            return apology("Username is required", 400)
        # Check if password was submitted
        elif not password:
            return apology("Password is required", 400)
        # Check if confirmation password was submitted
        elif not confirmation:
            return apology("Confirmation password is required", 400)
        # Check if password and confirmation match
        elif password != confirmation:
            return apology("Passwords do not match")
        elif not re.search("[a-zA-Z]", password) or not re.search("[0-9]", password) or not re.search(fr"[{symbols}]", password):
            flash("Password must contain at least one letter, one number, and one symbol")
            return apology("Password must contain at least one letter, one number, and one symbol")
        # Query database for existing username
        existing_company = get_company_from_db(username)
        if existing_company:
            return apology("Username already exists", 400)

        # Add user to the database
        add_company_to_db(username, companyname, Address, password, confirmation)

        # Query datbase for newly added users

        added_company = get_company_from_db(username)

        if added_company:
            user_id = added_company[0].get('id')  # Retrieve the 'id' value
            if user_id is not None:
            # Remember who is logged in
                session['user_id'] = user_id
                flash("User successfully registered!")
                return render_template("jobpost.html")
            else:
                flash("User ID not found in the database.")
        else:
            flash("No user data retrieved from the database.")

    else:
        return render_template("registercompany.html")

@app.route("/logout")
def logout():
   # Clear all user id
   session.clear()
   # redirect customer to login page
   return redirect("/")

@app.route('/')
@login_required
def hello_world():
  jobs = get_connection()
  blogs = get_blog()
  return render_template('home.html', jobs=jobs, blogs=blogs)

@app.route('/search', methods=['GET'])
@login_required
def search():
    # Extract the search query from the request parameters
    query = request.args.get('search', '') 
    jobs = get_connection()
    filtered_jobs = [job for job in jobs if query.lower() in (job['title'] or '').lower() or query.lower() in (job['company'] or '').lower()]
    blogs = get_blog()
    filtered_blogs = [blog for blog in blogs if query.lower() in (blog['title'] or '').lower() or query.lower() in (blog['article'] or '').lower()]
    return render_template('search.html', query=query, jobs=filtered_jobs, blogs=filtered_blogs)

@app.route("/postjob")
def jobpost():
   return render_template("logincompany.html")

@app.route('/api/jobs')
@login_required
def job_list():
  jobs = get_connection()
  return jsonify(jobs)

@app.route("/api/users")
@login_required
def user():
   users = get_users()
   return jsonify(users)

@app.route('/job/<id>')
@login_required
def show_job(id):
  job = get_connection_from_db(id) 
  if not job:
     return "Not Found", 400
  else:
    return render_template('jobpage.html', job=job)

@app.route('/api/job/<int:id>')
@login_required
def show_job_construction(id):
  job = get_connection_from_db(id)
  if job:
      return jsonify(job)
  else:
      return jsonify({'message': 'Job not found'}), 404

@app.route('/api/blog/id')
@login_required
def show_blog_post(id):
  blog = get_blog_from_db(id)
  if blog:
      return jsonify(blog)
  else:
      return jsonify({'message': 'Job not found'}), 404

@app.route('/blog/<int:id>')
@login_required
def show_blogs(id):
  blog = get_blog_from_db(id)
  if blog:
    return render_template('blog.html', blog=blog)
  else:
    return render_template({'message': 'blog not found'}), 404

import smtplib

@app.route('/job/<id>/apply', methods=["post"])
def apply_job(id):
    data = request.form
    job = get_connection_from_db(id)
    add_application_to_db(id, data)
    
     # Get the company's email address from the job posting
    company_email = job['company_email']

    # Set up the email message
    subject = f"Application for {job['title']} position"
    body = f"Here is the application for the {job['title']} position at {job['company']}:\n\n{data['full_name']}\n{data['email']}\n{data['linkedin_url']}\n{data['education']}\n{data['work_experience']}\n{data['resume_url']}"
    message = f"Subject: {subject}\n\n{body}"
    
    # Debugging: Print relevant values
    print(f"Company Email: {company_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

    try:
        # Set up the SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("clintonbeyene52@gmail.com", "fqkd lblu kuml ojvt")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Debugging: Print server response
        print(server.login("clintonbeyene52@gmail.com", "fqkd lblu kuml ojvt"))

        # Send the email
        server.sendmail("esubalew1381@gmail.com", company_email, message)
        server.quit()

        return render_template('application_submitted.html', application=data, job=job)
    except smtplib.SMTPAuthenticationError as e:
        # Debugging: Print the exception
        print(f"Authentication Error: {e}")
        return "Authentication failed. Check your credentials."


@app.route('/jobpost', methods=["GET", "post"])
@login_required
def job_post():
  if request.method == "POST":
    insert = request.form
    # Function to add job post to the database
    add_job_post_to_db(id, insert)
    # Render a template to show job posted succefully
    return render_template('jobposted.html', jobpost=insert)
  else:
    # Render the job form for job post submission
    return render_template("jobform.html")

items = [f"item_{i}" for i in range(20)]

@app.route('/alljobs')
@login_required
def show_all_jobs():
    # Retrieve all blogs from the database
    all_jobs = get_connection()
    # Implement a function to get all jobs from the database
    # jobs = all_jobs[offset:offset + limit]
    # Return the rendered template
    return render_template('all_jobs.html', jobs=all_jobs)

@app.route('/allblogs')
@login_required
def show_all_blogs():
    # Retrieve all blogs from the database
    all_blogs = get_blog()  # Implement a function to get all blogs from the database
    return render_template('all_blogs.html', blogs=all_blogs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)