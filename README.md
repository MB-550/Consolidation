Project name: Website Django

Table of contents:

*****************************************************
1. Description

2. Installation

3. Usage

4. Credits

****************************************************


****************************************************************************************************************************************************************************
1. Description: 

This is a website template for a blog, poll and user authentication page. You will be able to run this website after following all the instructions for usage and installation.

*****************************************************************************************************************************************************************************

2. Installation: 

First create a local folder on your device. You can name it anything you like just make sure it is empty.
To install this download all the folders and files and save it in the local folder on your device. 
Make sure to install all the necessary requirements which are listed in the requirements file.

If you want to clone the repository run the following command in your terminal. Make sure it is in the correct directory and that Github is installed on your device and make sure you have set up an account.:

"git clone https://github.com/MB-550/Consolidation/tree/master"

To install the requirements file run the following command in your terminal opened in the local folder with all the files and folders you downloaded:

"pip install -r requirements.txt"

The following will appear :

![image](https://github.com/MB-550/Consolidation/assets/149601983/87e42313-83e1-4c6f-84f8-cf7b14e674fa)
(Note on my device the requirements are already satisfied but on your device only requirements that are not satisfied will be installed)

----------------------------------------------------------------------
To setup a virtual environment, make sure your in the correct directory and have the terminal open. Then run the following command to create the virtual environemnt:

"python -m venv env", the env is the name of the virtual environment and you can name it anything you want.

To activate the environment run the following command via the terminal:

Windows: ".\env\Scripts\activate"

macOS or Linux: "source env/bin/activate"

To deactivate the virtual environment run:

"deactivate"

--------------------------------------------------------------------

The next section of installation will be with regards to containeristion via docker:

First dowload Docker at https://www.docker.com/products/docker-desktop and then create an account

Then to ensure Docker is working properly please run the following command in your terminal:

"docker run hello-world"

To create a docker image first navigate to the folder you want to contain, or the folder that has the program you want to contain.
Create a file called Dockerfile(no extension) open it in visual studios or any other code editor, change the encoding to UTF-8.

In the Dockerfile add the following:

html:

FROM nginx

COPY . /usr/share/nginx/html

Python applications :

FROM pypy:latest

WORKDIR /app

COPY . /app

CMD python [Application name goes here]

After the Dockerfile has been created and edited properly you need to build the Docker image by running the following commands:

html:

"docker build -t my-website ./"

Python application:

"docker build -t python-app ./"

And then to run the image run the following command in the terminal this applies to both html and python applications:

"docker run [Image name]"

And then you should have a successfully created a docker image.

*****************************************************************************************************************
Usage: 

To use the website in the parent folder you created that contains all the files and folder you downloaded, open the terminal and run the following command to waht migrations need to take place: 

"python manage.py migrate":

![image](https://github.com/MB-550/Consolidation/assets/149601983/db89ba20-883b-485c-a328-ec0af248b938)

Then to make the necessary migrations run te following command:

"python manage.py makemigrations":

![image](https://github.com/MB-550/Consolidation/assets/149601983/cfd371cb-d9d1-46b0-b40f-cfd3dbb90ff2)

Then run the migrate command again:

![image](https://github.com/MB-550/Consolidation/assets/149601983/2c3bf9ee-3a8e-4a0c-a4b1-cdd56741da55)


Next is to run the server so run the following command to run the server:

"python manage.py runserver 8056":

![image](https://github.com/MB-550/Consolidation/assets/149601983/70f8ae72-c402-486f-8faa-2fa9fa85f125)


After that click on the https link and you will be redirected to the website:

![image](https://github.com/MB-550/Consolidation/assets/149601983/644abe5f-4739-4391-8b70-73bb05e1add2)

Press the sign up button and create a username and password:

![image](https://github.com/MB-550/Consolidation/assets/149601983/2f2d565c-355a-478c-beb0-4b0aceac62bc)

Then go back to the login screen and log in :

![image](https://github.com/MB-550/Consolidation/assets/149601983/3f67a8ad-51ab-4330-a4c2-a958fad2fec6)

Then press the link to the main page:

![image](https://github.com/MB-550/Consolidation/assets/149601983/1fc75215-04d0-44bd-9204-06c2efacd834)

Then from there you can navigate to the other pages, note that you will have to be an admin to have access to the admin page, learn more about this by looking up how django admins work.
Other than that all the other pages will work fine and you will be able to interact with them.

******************************************************************************************************************************************************************
Credits: 

Makeel Bhikshu
Hyperiondev for help with docker and github commands

