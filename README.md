# travel-app
Your Travel Assistant 

# Python Cheat Sheet
## Use an older version of python so you can use torch and tensorflow
+ `brew install pyenv`
+ `brew install pyenv-virtualenv`
+ `export PATH="$HOME/.pyenv/bin:$PATH"`
+ `eval "$(pyenv init --path)"`
+ `eval "$(pyenv init -)`
+ `eval "$(pyenv virtualenv-init -)"`
+ `source ~/.zshrc`
+ `pyenv install 3.11.9`

## Set up python env
+ `python3 --version`  
+ `pip install virtualenv`
+ `pyenv virtualenv 3.11.9 myenv`
+ `pyenv activate myenv`  
## Delete Env
+ `rm -rf env`

# Installing packages
+ `pip install tensorflow`
+ `pip install flask`
+ `pip install jupyter`
+ `pip install notebook ipykernel`
+ 

# Set up env in Jupyter Notebook
+ `python -m ipykernel install --user --name=env --display-name "Python (env)"`  

# Set Hugging Face Token
+ `export HUGGINGFACE_API_TOKEN="your_huggingface_api_token"`
+ Create a .env file in your project directory: `HUGGINGFACE_API_TOKEN=your_huggingface_api_token`
+ `pip install python-dotenv`

# Install Heroku CLI
+ `brew tap heroku/brew && brew install heroku`
+ `heroku --version`



# Github commands
+ Add New Key: `ssh-keygen -t rsa -b 4096 -C "your-email@gmail.com"`
+ Start the SSH agent: `eval "$(ssh-agent -s)"`
+ Add your SSH key to the agent: `ssh-add ~/.ssh/id_rsa`
+ Print Key: `cat ~/.ssh/id_rsa.pub`
+ Add key to github
+ Verify: `ssh -T git@github.com`

