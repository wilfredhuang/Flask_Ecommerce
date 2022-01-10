# Populate environment variables from .env file and test if they working

# Rename `os.environ` to `env` for nicer code
from os import environ as env

from dotenv import load_dotenv
load_dotenv()

# print('API_KEY:  {}'.format(env['API_KEY']))
# print('HOSTNAME: {}'.format(env['HOSTNAME']))
# print('PORT:     {}'.format(env['PORT']))
print('FLASK_ENV:     {}'.format(env['FLASK_ENV']))
print('FLASK_APP:     {}'.format(env['FLASK_APP']))
print('DATABASE_URL:     {}'.format(env['DATABASE_URL']))


# Use os.environ to get exceptions for missing env values
# os.getenv() will only return none if a value is missing
