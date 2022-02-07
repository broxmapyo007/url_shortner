import os
ENV = os.environ.get('DEPLOYMENT_ENV', 'local')
print(ENV)

if ENV=="local":
    self_url = "http://127.0.0.1:8080"

elif ENV == "heroku_stg":
    self_url = "https://url_shortner_project.herokuapp.com"
# it will be based on request coming
