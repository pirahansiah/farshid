from dotenv import load_dotenv
import os
load_dotenv()
password=os.environ.get("Farshid")
print(password)