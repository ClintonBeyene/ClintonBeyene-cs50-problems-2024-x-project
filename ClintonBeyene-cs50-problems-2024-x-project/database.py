import csv
import datetime
import pytz
import requests
import urllib
import uuid
import mysql.connector
import os

from mysql.connector import connect
from werkzeug.security import generate_password_hash
from flask import Flask, request
from dotenv import load_dotenv
from flask import redirect, render_template, session
from functools import wraps

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

conn = connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

def get_connection():
    try: 
        c=conn.cursor(dictionary=True)
        c.execute("select * from jobs")
        jobs= c.fetchall()
        for row in c.fetchall():
           jobs.append(dict(row))
        return jobs
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_connection_from_db(id):
    try:
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))  # Pass the job ID as a dictionary
        job = cursor.fetchone()
        return job
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_users():
    try:
        c=conn.cursor(dictionary=True)
        c.execute("select * from users")
        users= c.fetchall()
        for row in c.fetchall():
            users.append(dict(row))
        return users
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        return None

def get_company():
    try: 
        cursor=conn.cursor(dictionary=True)
        cursor.execute("select * from company")
        company = cursor.fetchall()
        for row in cursor.fetchall():
            company.append(dict(company))
        return company
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        return None

def get_users_from_db(username):
    try:
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))  # Pass the job ID as a dictionary
        user = cursor.fetchall()
        return user
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def get_company_from_db(username):
    try:
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM company WHERE username = %s", (username,))  # Pass the job ID as a dictionary
        company = cursor.fetchall()
        return company
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_login_from_db(username):

    try: 
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        login = cursor.fetchall()
        return login
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def get_company_login_from_db(username):

    try: 
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM company WHERE username = %s", (username,))
        login = cursor.fetchall()
        return login
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def add_users_to_db(username, password, confirmation):
    try:
        cursor = conn.cursor(dictionary=True)
        inserted = "INSERT INTO users (username, hash, created_at, updated_at) VALUES (%s, %s, NOW(), NOW())"
        cursor.execute(inserted, (username, generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_company_to_db(username, companyname, Address, password, confirmation):
    try:
        cursor = conn.cursor(dictionary=True)
        inserted = "INSERT INTO company (username, companyname, Address, hash, created_at, updated_at) VALUES (%s, %s, %s, %s, NOW(), NOW())"
        cursor.execute(inserted, (username, companyname, Address, generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
def get_blog():
    try:  
        c=conn.cursor(dictionary=True)
        c.execute("select * from blogs")
        blogs= c.fetchall()
        for row in c.fetchall():
           blogs.append(dict(row))
        return blogs
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def get_blog_from_db(id):
    try:
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM blogs WHERE id = %s", (id,))
        blog = cursor.fetchone()
        return blog
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def add_application_to_db(job_id, data):
    try:
        cursor=conn.cursor(dictionary=True)
        query = 'INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (job_id, data['full_name'], data['email'], data['linkedin_url'], data['education'], data['work_experience'], data['resume_url']))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def add_job_post_to_db(id, insert):
    try:
        cursor = conn.cursor(dictionary=True)
        query = 'insert into jobs (company_email, company, title, location, salary, currency, responsibilities, requirements) values (%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (insert['company_email'], insert['company'], insert['title'], insert['location'], insert["salary"], insert['currency'], insert['responsibilities'], insert['requirements']))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
 
def apology(message, code):
    return render_template("apology.html", message=message), code

def login_required(f):
  """
  Decorate routes to require login.

  https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
  """

  @wraps(f)
  def decorated_function(*args, **kwargs):
      if session.get("user_id") is None:
          return redirect("/login")
      return f(*args, **kwargs)

  return decorated_function
