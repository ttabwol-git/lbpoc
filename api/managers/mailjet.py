import os
from mailjet_rest import Client


class MailJetClient:
    
    def __init__(self):
        self.client = None
        
    async def send_email(self, subject: str, text: str) -> dict | None:
        self.client = Client(
            auth=(os.environ['MAILJET_API_KEY'], os.environ['MAILJET_API_SECRET']),
            version='v3.1'
        )
        data = {
            'Messages': [{
                'From': {'Email': 'lbpoc-test@proton.me', 'Name': 'LBPOC Email Service'},
                'To': [
                    {'Email': os.environ['EMAIL_TO_ADDR'], 'Name': os.environ['EMAIL_TO_NAME']}
                ],
                'Subject': subject,
                'TextPart': text
            }]
        }
        result = self.client.send.create(data=data)
        if result.status_code == 200:
            return result.json()
