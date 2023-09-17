from dataclasses import dataclass
import requests
import constants as c
from main import logger


@dataclass
class BlogPost:
    title: str
    link: str

    def send_to_slack(self):
        payload = {
            "text": f"{self.title}",
            "attachments": [
                {
                    "text": f"{self.link}",
                    "unfurl_links": True,
                    "unfurl_media": True,
                }
            ],
        }

        response = requests.post(c.SLACK_WEBHOOK_URL, json=payload)

        if response.status_code != 200:
            raise ValueError(
                logger.error(
                    f"Request to slack returned an error {response.status_code}, "
                    f"the response is:\n{response.text}"
                )
            )
        else:
            logger.info(f"Sent article title {self.title} to slack!")
