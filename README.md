# Scales
A mathematical education application for first graders.

# Requirements
-pip
-python 3.5+
-venv

# Setting up your enviornment
   ## Mac / Linux
       -Go to directory where you want to setup your project.
       -Type the following in your preferred terminal
       $Python3 -m venv env
   ## Windows
       -Go to directory where you want to setup your project.
       -Type the following in command prompt
       $py -m venv env
      
## Clone the repository into your project directory - not inside the generated 'env' folder.

# Activating the environment
  ## Mac / Linux
    source env/bin/activate
  ## Windows
    .\env\Scripts\activate
    
# Deactivating (same for all platforms)
       deactivate


# Installing the requirements from requirements.txt
      pip install -r requirements.txt
  
  
# Installing other dependancies
      -ensure your virtual env is still activated and then: 
      pip install [package name]

## if you find yourself needing more packages to install with pipthey must be added to the requirements.txt file like so:
      pip freeze > requirements.txt
