# Scales-1
A mathematical education application for first graders.

# Requirements
-pip
-python 3.5+
-venv

# Setting up your enviornment
   ## Mac / Linux
       -Go to directory where you want to setup your project.
       -Type the following in your preferred terminal
       -$Python3 -m venv env
   ## Windows
       -Go to directory where you want to setup your project.
       -Type the following in command prompt
       -$py -m venv env
      
## Clone the repository into your project directory - not inside the generated 'env' folder.

# Activating the environment
  ## Mac / Linux
    -source env/bin/activate
  ## Windows
    -.\env\Scripts\activate


# Installing the requirements from requirements.txt

  ## In your terminal type...
  -pip install -r requirements.txt
  
  
# Installing other dependancies with pip install [package name]

## if you find yourself needing more packages to install with pip 
## they must be added to the requirements.txt file like so:

### in project direcotry with requirements.txt type the following:
    -pip freeze > requirements.txt
