import os
from dotenv import load_dotenv
import requests
import json
import base64   

load_dotenv()

EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")
SENDER_NAME = os.getenv("SENDER_NAME")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")


def send_email(subject: str, text_content: str, image_path: str = None):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json",
    }
    
    payload = {
        "sender": {"name": SENDER_NAME, "email": EMAIL_FROM},
        "to": [{"email": EMAIL_TO}],
        "subject": subject,
        "textContent": text_content,
    }

    if image_path:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
            
            # add to payload
            payload["attachment"] = [
                {
                    "content": encoded_image,
                    "name": os.path.basename(image_path),
                    "contentId": "image1"
                }
            ]      
    payload = json.dumps(payload)

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


# if __name__ == "__main__":
#     send_email(
#         subject="Is Python SDK work done?",
#         text_content="Hi Sourabh,\nIs Python SDK work complete or not?",
#         image_path = "random_girl.jpg"
#     )
