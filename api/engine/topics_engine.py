"""Topics Engine Module"""

import os
from fastapi import HTTPException


class TopicsEngine:
    """Class that handles the logic for submitting topics"""

    def __init__(self, slack) -> None:
        self.slack = slack

    async def submit(self, request, params) -> dict:
        """Method to submit a new topic"""

        if params.topic == 'pricing':
            # TODO: save to queue to be sent by another service
            pass

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

        return {
            'ok': True,
            'request_id': request.state.id,
            'message': f'{params.topic} topic submitted successfully'
        }
