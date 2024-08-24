# A career website for Construction Jobs.
####
#### Description:
Welcome to our Construction Jobs web application! Our platform is designed to connect construction companies with qualified job seekers, providing an easy-to-use and accessible interface for searching and applying to job openings. we also offer a blog section where users can read articles related to the construction industry. With features such as user and company registration, login and logout, and job posting and application, our web application aims to streamline the hiring process for both companies and job seekers. Our platform is built using the Flask framework, HTML, CSS, JavaScript, and a MySQL database, ensuring a reliable and efficient user experience. Try it out today and discover the benefits of our Construction Jobs web application! Here i explain in details how i build the web.

#home.html
Home.html is my basic HTML template for my web page using the Bootstrap framework. It includes a navigation bar with a logo, search bar, and links to different sections of the website. The website is divided into three main sections: welcome, index, and blogs. The main content of the page is included within the `{% block main %}{% endblock %}` tags, which can be overridden in other templates that extend this one.

Here's a breakdown of the code:

- `<!DOCTYPE html>`: Defines the document type and version of HTML.
- `<html lang="en">`: Specifies the language of the document as English.
- `<head>`: Contains meta-information about the document, such as the title and the Bootstrap framework.
- `<body>`: Contains the main content of the document.
- `<nav>`: Represents a navigation bar, which includes the website logo, search bar, and links to different sections of the website.
- `<form>`: Represents a form for searching jobs on the website.
- `<div class="main-container">`: Represents the main content of the page, which can be overridden in other templates that extend this one.

Bootstrap.html code in template is a combination of HTML meta tags, a title tag, and two link tags. These elements are used to define the structure, appearance, and behavior of a web page. Here's a breakdown of each element:

<meta charset="utf-8">: This tag defines the character encoding for the HTML document. In this case, it's set to UTF-8, which is a widely-used character encoding standard.

<meta name="viewport" content="width=device-width, initial-scale=1.0">: This tag defines the viewport for the web page. It tells the browser to scale the content based on the width of the device's screen. In this case, the content is set to scale with the device's width and the initial scale is set to 1.0.

<title>Home</title>: This tag defines the title of the web page, which is displayed in the browser's title bar or in the page's tab.

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">: This tag links to the Bootstrap CSS file, which is a popular CSS framework for designing web pages. The integrity attribute is used to ensure the integrity of the file, and the crossorigin attribute is used to specify the CORS settings.

<link rel="stylesheet" href="/static/styles.css">: This tag links to a custom CSS file (styles.css) located in the /static directory. This file is used to define additional styles for the web page.

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">: This tag links to the Font Awesome CSS file, which is a collection of icons. By including this file, you can use Font Awesome icons in your web page.

My header.html, header1.html, header2.html and header3.html are four variations of a header for a Construction Jobs website, with different navigation links for PostJob, Register, Login, and RegisterCompany, and to return home with construction jobs.

#contacts.html
This is the Contact section of a webpage, displaying social media links for Construction Jobs on Facebook, GitHub, Twitter, email, and phone. Each link is represented by an icon and the name of the platform. The links open in a new tab when clicked. This section is styled using Bootstrap and Font Awesome icons.

#login.html
This is an HTML page for a company login. It includes a header, a main section with a login form, and a footer. The login form has two fields for username and password, and a submit button. The form is styled with custom CSS that sets the background color, font color, and input styles. The page includes a bootstrap.html file for additional styling and a header1.html file for the header. The login form submits to the "/login" endpoint using the POST method.

#register.html
This is an HTML page for registering a new company account. It includes a header, a main section with a registration form, and a footer. The registration form has three fields: username, password, and confirm password. The form is styled with custom CSS that sets the background color, font color, and input styles. The page includes a bootstrap.html file for additional styling and a header2.html file for the header. The registration form submits to the "/registercompany" endpoint using the POST method.

#logincompany.html
This is an HTML page for a company login form, which includes a header, a main section with a login form, and a footer. The login form has two fields: username and password, and a submit button. The form is styled with custom CSS that sets the background color, font color, and input styles. The page includes a bootstrap.html file for additional styling and a header3.html file for the header. The login form submits to the "/logincompany" endpoint using the POST method.

#registercompany.html 
This is an HTML page for a company registration form. It includes a header, a main section with a registration form, and a footer. The registration form has five fields: username, company name, address, password, and confirm password, and a submit button. The form is styled with custom CSS that sets the background color, font color, and input styles. The page includes a bootstrap.html file for additional styling and a header.html file for the header. The registration form submits to the "/registercompany" endpoint using the POST method.

#search.html
This is a Flask template that extends a base template called "home.html". It has a block called "main" that contains the main content of the page. The page displays a list of jobs and blogs that match a search query. If there are no jobs or blogs, nothing is displayed. The jobs and blogs are displayed as a list of links, each with a title and a company name (for jobs). The links point to the show_job and show_blogs pages, respectively. The page is styled with Bootstrap classes.

#welcome.html
This is an HTML file that contains a video background in the first section of the page. The video is set to autoplay, loop, and mute, and it uses a video file named "homepage.mp4". The video is wrapped in a container with a class of "welcome-section" and "main-container". The section contains a single div with a class of "first-module". The video is styled to fit the container using CSS classes. This file is likely used as a landing page or a welcome section for a website.

#jobform.html
This is an HTML form for posting a job. It contains several fields for the user to enter information about the job, including:

Company email (required)
Company name (required)
Job title (required)
Location (required)
Salary (required)
Currency (required)
Job responsibilities (required)
Job requirements (required)
The form action attribute is set to "/jobpost" and the method is set to "post". The form also contains a submit button. The form fields use the "input" and "textarea" HTML elements with corresponding placeholders and name attributes. The form uses CSS classes to style the layout and appearance of the form elements.

#jobitem.html
This is a Flask template that displays a single job item. It extends a base template called "home.html" and has a block called "main". The job information is displayed in a div with a border-bottom class, which contains two columns. The first column contains the job title, location, and salary (if available), while the second column contains a button to apply for the job. The job data is passed to the template using the "job" variable, which is accessed using Jinja2 syntax. The template also includes the "bootstrap.html" template to add Bootstrap styling to the job title and location. The template is used to display a single job item in a list of jobs.

#jobpage.html
The jobpage.html file is a Flask template that displays a job posting on a job board website. It includes the following components:

Bootstrap and custom CSS stylesheets
A header, which is included from the header.html file
A job description, which includes the following information:
Job title
Location
Responsibilities (rendered as an unordered list)
Requirements (rendered as an ordered list)
Salary (rendered as a paragraph)
An application form, which is included from the application_form.html file
A footer, which is included from the footer.html file
The job information is passed to the template using the job variable, which is accessed using Jinja2 syntax. The template uses Bootstrap classes to style the layout and appearance of the job description and application form.

#jobpost.html
This is an HTML file that displays a job posting form. The form is displayed in a fixed navbar at the top of the page, which includes a logo, a search bar, and a menu with links to other pages. The form itself is displayed in a container with a class of "projects-section master-container". The form is included from the jobform.html file. The file also includes the bootstrap.html file, which provides Bootstrap CSS styles. The navbar and the footer are also included in this file, which are likely shared with other pages on the website. The form allows a user to post a job with the following fields:

Company email
Company name
Title of Position
Location
Salary
Currency
Responsibilities
Requirements
The form uses the POST method and submits to the /jobpost endpoint.

#jobposted.html
This is an HTML file that displays a job posting confirmation page. The page includes the following components:

Bootstrap CSS styles, included via the bootstrap.html file
A header, included via the header.html file
A job posting confirmation message, which displays the job title, location, salary, currency, responsibilities, and requirements
A footer, included via the footer.html file
Bootstrap JS and any other required JS files, included via two script tags.
The page displays the job details in a card with a light background. The job details are displayed in an unordered list, with each detail (title, location, salary, etc.) displayed as a list item with a strong tag. The page uses CSS classes to style the layout and appearance of the job details and confirmation message. The page is likely used to display a confirmation message after a user has successfully posted a job.

#all_jobs.html
The all_jobs.html file displays a list of jobs, sorted alphabetically by title in descending order. The jobs are displayed in a container with a class of "jobs-section master-container". Each job is displayed in a row with two columns. The first column contains the job title, location, and salary (if available), while the second column contains a button to apply for the job. The file includes the bootstrap.html file, which provides Bootstrap CSS styles. The header and footer are also included in this file, which are likely shared with other pages on the website. The file uses a Jinja2 for loop to iterate over the sorted list of jobs, and displays each job in a row with a border-bottom class. The file uses Jinja2 syntax to access the job information and display it in the appropriate placeholders. The file also uses Bootstrap classes to style the layout and appearance of the job list.

#application_form.html
This is an HTML file that contains a job application form. The form includes the following fields:

Full Name
Email
LinkedIn URL
Education
Work Experience
Resume URL
The form uses the POST method and submits to the /job/{{ job['id'] }}/apply endpoint. The form uses Bootstrap classes to style the layout and appearance of the form fields. The form includes a header, which is included from the header.html file. The bootstrap.html file is also included, which provides Bootstrap CSS styles. The form is likely used to allow a user to apply for a job posting. The form uses textarea elements to allow the user to input multiple lines of text for the education and work experience fields. The form uses a submit button to submit the form data.

#application_submitted.html
The application_submitted.html file displays a confirmation page after a user has successfully submitted a job application. The page includes the following components:

Bootstrap CSS styles, included via the bootstrap.min.css file
A header, included via the header.html file
A confirmation message, which displays the job title, the user's full name, email, LinkedIn URL, education, work experience, and resume URL.
A footer, included via the footer.html file
The page uses HTML tags to display the confirmation message. The page uses Bootstrap classes to style the layout and appearance of the confirmation message. The page is likely used to display a confirmation message after a user has successfully submitted a job application. The page uses Jinja2 syntax to access the application data and display it in the appropriate placeholders.

#blogs.html
This is an HTML file that displays a grid of blog posts with images and titles. The blog posts are sorted by location in descending order. The file includes a header, which is included from the header.html file. The blog posts are displayed in a container with a class of "projects-section master-container" and a style of "color: #fff". Each blog post is displayed as a link in an anchor tag, with an image and a title. The first blog post is displayed by default, while the remaining blog posts are initially hidden and can be displayed by clicking a "Show all" button. The file uses Bootstrap classes to style the layout and appearance of the blog post grid. The file uses JavaScript to hide the blog posts and show them when the "Show all" button is clicked. The file uses Jinja2 syntax to access the blog data and display it in the appropriate placeholders. The file includes a footer, which is likely shared with other pages on the website.

#blog.html
The blog.html file displays a blog post with a title and an article. The file includes a header, which is included from the header.html file. The blog post is displayed in a container with a class of "jobs-section". The title and article are displayed in a row with a border-bottom class. The title is displayed in a heading tag with a class of "h3" and a style of "color: #fff". The article is displayed in a series of paragraph tags with a style of "color: #fff". The file uses Bootstrap classes to style the layout and appearance of the blog post. The file uses Jinja2 syntax to access the blog data and display it in the appropriate placeholders. The file includes a footer, which is likely shared with other pages on the website.

The article text is displayed using a for loop that iterates over the lines of the article text and displays each line as a separate paragraph. The splitlines() method is used to split the article text into individual lines, which are then displayed as separate paragraphs. This allows for better formatting and readability of the article text.

#all_blogs.html
The all_blogs.html file displays a list of blog post links. The file includes a header, which is included from the header.html file. The blog post links are displayed in a container with a class of "projects-section master-container" and a style of "color: #fff". Each blog post link is displayed in a anchor tag, with an image and a title. The file uses Bootstrap classes to style the layout and appearance of the blog post links. The file uses Jinja2 syntax to access the blog data and display it in the appropriate placeholders. The file includes a footer, which is likely shared with other pages on the website.

The file uses a for loop to iterate over the list of blogs and display a link for each blog. The link includes the blog title and an image, and opens in a new tab when clicked. The file does not include the full blog post, but instead provides a link to the full blog post. The file uses Bootstrap classes to style the layout and appearance of the blog post links, including the "project-tile" class for the anchor tag and the "project-image" class for the image.

The file uses HTML entities to display special characters in the blog title, such as the less-than (<) and greater-than (>) symbols. This ensures that the special characters are displayed correctly in the browser, rather than being interpreted as HTML tags.

Overall, the all_blogs.html file provides a simple and clean layout for displaying a list of blog post links, allowing users to easily browse and access the full blog posts.

#index.html
my index.html file is the main page of a job board website. It displays a list of jobs sorted by title in descending order. The top 3 jobs are displayed in a card format with title, location, and salary. A "Show all" button loads more jobs via AJAX and links to the "/alljobs" page. The page uses Bootstrap for styling and Jinja for templating. JavaScript code handles fetching and displaying more jobs when the user clicks the "Show all" button.

#footer.html
The footer.html file is a footer component that contains links to social media profiles and a copyright notice. It includes a nav element with a class of "nav justify-content-center" to center the links horizontally. Each link is displayed in an anchor tag with a class of "nav-link px-2 text-body-secondary". The anchor tags include icons from the Font Awesome library to represent each social media platform. The footer also includes a copyright notice, which is displayed as a paragraph tag with a class of "text-center text-body-secondary".

The footer is included in other HTML files using the {% include 'footer.html' %} syntax, which allows it to be easily reused across multiple pages. The footer provides a consistent layout and styling for the bottom of the page, while also providing users with links to social media profiles and a copyright notice.

The footer is designed to be simple and minimal, with a focus on providing basic information and links. It does not include any complex functionality or interactivity, but instead serves as a basic footer component for the website.

Overall, the footer.html file is a simple but useful component that provides basic information and links to users, while also maintaining a consistent layout and styling for the bottom of the page.

#apology.html
The apology.html file is a Flask template that extends a base template called "home.html" and displays an image with a custom message. The message is passed to the template using the top variable, and is displayed as the top part of the image. The bottom part of the image is a static string that says "Sorry". The image is generated using the memegen.link service, which creates a custom image with the top and bottom text provided.

The urlencode filter is used to encode the top variable to ensure that any special characters are properly encoded for use in the URL. This is necessary because the memegen.link service requires the text to be URL-encoded.

The image is displayed using an img tag with a class of "border img-fluid". The border class adds a border to the image, and the img-fluid class makes the image responsive, so that it scales nicely on different screen sizes.

The title attribute is used to provide a tooltip for the image, which displays the top variable when the user hovers over the image.

Overall, the apology.html file is a simple but effective template for displaying a custom apology message using the memegen.link service. It extends a base template for consistency and uses the urlencode filter to properly encode the top variable for use in the URL. The img tag is used to display the custom image, and the title attribute is used to provide a tooltip for the image.

i used this apology code from my finance problemsets.

in my directory there is static sub directory that consists image, logo, video and styles.css

#styles.css
Styles.css is a CSS file that contains styles for a website. It defines a number of custom variables using CSS custom properties, including colors, fonts, and other visual elements. The file sets the font, font size, and line height for various HTML elements, including the body, headings, and paragraphs. It also includes styles for the navigation bar, including the links and input fields.

The file also includes media queries to make the navigation bar responsive on smaller screens. It styles the project grid and individual project elements, including the project image and title. It also includes styles for buttons, including hover effects.

The file sets the background color and text color for various sections of the website, including the welcome section, jobs section, projects section, and contact section. It also includes styles for the contact links and details, including hover effects.

Overall, the styles.css file is a comprehensive stylesheet that defines a consistent visual style for the website, including colors, fonts, and layout. It makes use of CSS custom properties to define reusable variables, and includes media queries to make the navigation bar responsive on smaller screens. The file also includes hover effects for buttons and links, and sets the background and text color for various sections of the website.

#database.py
This is a Python module for a Flask web application that provides functions for interacting with a MySQL database. The module imports various modules such as mysql.connector, werkzeug.security, os, datetime, pytz, urllib, uuid, and flask. It also imports some functions from mysql.connector and werkzeug.security.

The module defines several functions for interacting with the database, including:

get_connection: retrieves all jobs from the database and returns them as a list of dictionaries.
get_connection_from_db: retrieves a specific job from the database by its ID and returns it as a dictionary.
get_users: retrieves all users from the database and returns them as a list of dictionaries.
get_company: retrieves all companies from the database and returns them as a list of dictionaries.
get_users_from_db: retrieves a specific user from the database by their username and returns them as a dictionary.
get_company_from_db: retrieves a specific company from the database by their username and returns them as a dictionary.
get_login_from_db: retrieves a specific user login from the database by their username and returns them as a dictionary.
get_company_login_from_db: retrieves a specific company login from the database by their username and returns them as a dictionary.
add_users_to_db: inserts a new user into the database with the given username and hashed password.
add_company_to_db: inserts a new company into the database with the given username, company name, address, and hashed password.
get_blog: retrieves all blogs from the database and returns them as a list of dictionaries.
get_blog_from_db: retrieves a specific blog from the database by its ID and returns it as a dictionary.
add_application_to_db: inserts a new application into the database with the given job ID and application data.
add_job_post_to_db: inserts a new job post into the database with the given data.
apology: returns an apology template with the given message and status code.
login_required: a decorator that redirects the user to the login page if they are not logged in.
The module uses environment variables to store the database connection information, such as the host, port, user, password, and database name. It also defines functions for connecting to the database and fetching data from it, such as jobs, users, and companies. The module also includes functions for adding data to the database, such as adding users, companies, and job posts.

Overall, the database.py module provides a convenient way to interact with the MySQL database, including functions for connecting to the database, fetching and inserting data, and handling errors. The module also includes a decorator for requiring login for certain routes.

#app.py
app.py is a Flask application that provides routes for user and company registration, login, logout, and job posting. It also includes routes for blog and job listings, as well as individual job and blog pages.

The application imports various modules including Flask, render_template, request, redirect, session, flash, jsonify, smtplib, and mysql.connector. It also imports several functions from the database.py module for interacting with the database.

The application includes the following routes:

/login: A route for logging in a user. It checks if the submitted username and password match a user in the database.
/logincompany: A route for logging in a company. It checks if the submitted username and password match a company in the database.
/register: A route for registering a new user. It checks if the submitted username is unique and if the submitted password meets certain requirements.
/registercompany: A route for registering a new company. It checks if the submitted username is unique and if the submitted password meets certain requirements.
/logout: A route for logging out a user.
/: A route for displaying a home page with job and blog listings.
/search: A route for searching job and blog listings based on a query parameter.
/postjob: A route for rendering a job posting form.
/api/jobs: A route for returning a JSON list of all jobs.
/api/users: A route for returning a JSON list of all users.
/job/<id>: A route for rendering a job page based on an ID parameter.
/api/job/<id>: A route for returning a JSON object of a job based on an ID parameter.
/job/<id>/apply: A route for handling job submissions and sending an email to the job poster with the applicant's information.
/jobpost: A route for handling job post submissions.
/jobposted: A route for rendering a confirmation page after a job post has been submitted.
/alljobs: A route for rendering a page with all job listings.
/allblogs: A route for rendering a page with all blog post listings.
The application uses Flask, a Python web framework, to handle HTTP requests and responses. It also uses the session module for session management, the werkzeug.security module for password hashing, and the mysql.connector module for database interactions. It uses the smtplib module for sending emails. The application uses a MySQL database to store user, company, job, and blog data.

The application uses the render_template function to render HTML templates using the Jinja2 template. The application uses the flash function to display messages to the user. The application uses the jsonify function to return JSON objects. The application uses the get_connection, get_connection_from_db, get_blog, get_blog_from_db, add_application_to_db, get_users, get_users_from_db, add_users_to_db, get_login_from_db, get_company, add_company_to_db, get_company_from_db, and add_job_post_to_db functions from the database.py module for database interactions.

Overall, The purpose of this web application is to provide a platform for construction jobs where companies can post job openings and job seekers can search and apply for those jobs. The platform also includes a blog section where users can read articles related to the construction industry. The web application is built using the Flask framework, HTML, CSS, JavaScript, and a MySQL database. It includes features such as user and company registration, login and logout, job posting and application, and blog listings and articles. The platform is designed to be user-friendly and accessible, with a clean and intuitive interface that makes it easy for users to find and apply for jobs, and for companies to post job openings. Overall, the web application aims to connect construction companies with qualified job seekers, and to provide a valuable resource for anyone interested in the construction industry.