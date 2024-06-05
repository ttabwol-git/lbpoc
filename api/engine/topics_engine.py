"""Topics Engine Module"""

import os
from fastapi import HTTPException


class TopicsEngine:
    """Class that handles the logic for submitting topics"""

    def __init__(self, slack, mailjet) -> None:
        self.slack = slack
        self.mailjet = mailjet

    async def submit(self, request, params) -> dict:
        """Method to submit a new topic"""
        response = {}

        if params.topic == 'pricing':

            # Generate the message string
            message = f'Hi Sales Team, \n\nThere\'s a new topic submission for *Pricing*!\n(id: {request.state.id})'
            message += f'\n\n{params.description}'

            # Send email
            response = await self.mailjet.send_email(subject='Test Email from LBPOC', text=message)
            if response is None:
                raise HTTPException(status_code=500, detail='Failed to send email')

        elif params.topic == 'sales':

            # Generate the message string
            message = f'Hi <!here>, there\'s a new message for *Sales*!\n(id: `{request.state.id}`)'
            message += f'\n\n>{params.description}'

            # Send message to Slack
            response = self.slack.send_message(channel=os.environ['SLACK_CHANNEL'], message=message)
            if not response.get('ok', False):
                error_message = 'Failed to post message to Slack: '
                error_message += response.get('error', 'Unknown error')
                raise HTTPException(status_code=500, detail=error_message)

        # Return success response
        return {
            'ok': True,
            'request_id': request.state.id,
            'message': f'{params.topic} topic submitted successfully',
            'details': response
        }
