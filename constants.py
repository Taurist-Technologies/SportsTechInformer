from dotenv import load_dotenv
import os

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
GEEK_WIRE_URL = "https://www.geekwire.com/sports"
CNBC_URL = "https://www.cnbc.com/sports/"
TECH_CRUNCH_URL = "https://techcrunch.com/tag/sports/"
SPORTS_TECHNOLOGY_URL = "https://sportstechnologyblog.com/"
