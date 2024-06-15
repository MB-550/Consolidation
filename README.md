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

Installation: 

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


To setup a virtual environment, make sure your in the correct directory and have the terminal open. Then run the following command to create the virtual environemnt:
"python -m venv env", the env is the name of the virtual environment and you can name it anything you want.

To activate the environment run the following command via the terminal:

Windows: ".\env\Scripts\activate"

macOS or Linux: "source env/bin/activate"

To deactivate the virtual environment run:

"deactivate"

The next section of installation will be with regards to containeristion via docker:



Usage: 

To use the website in the parent folder you created that contains all the files and folder you downloaded, open the terminal and run the following command: 

python manage.py runserver 8056

And the following will display:
![image](https://github.com/MB-550/Consolidation/assets/149601983/a50810fe-6559-4d03-97c3-ffe9e097702a)

After that click on the https link and you will be redirected to the website.

Credits: 

Makeel Bhikshu
Hyperiondev for help with docker and github commands

