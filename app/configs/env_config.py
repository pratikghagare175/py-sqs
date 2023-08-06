import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_KEY")
AWS_ACCESS_SECRET = os.getenv("AWS_SECRET")
