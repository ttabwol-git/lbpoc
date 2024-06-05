"""This file is used to configure the FastAPI application and register routers"""

import os
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI, Request

# importing managers
from api.managers.auth import VerifyToken
from api.managers.mailjet import MailJetClient
from api.managers.slack import SlackWebClient

# importing engines
from topics_engine import TopicsEngine

# importing routers
from topics_router import TopicsRouter


class APIConfig:
    """This class is used to configure the FastAPI application and register routers"""

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.environ['CONFIG_PATH'], 'local.env'))
        self.app = FastAPI()
        RegisterRouters(self.app)


class RegisterRouters:
    """This class is used to register routers to the FastAPI application"""

    def __init__(self, app) -> None:
        self.app = app
        self.auth = VerifyToken()
        self.slack = SlackWebClient()
        self.mailjet = MailJetClient()
        self.prefix = '/api'

        self.routers = [
            (TopicsRouter, TopicsEngine(self.slack, self.mailjet), '/topics')
        ]

        # Register routers
        for router in self.routers:
            initialized_router = router[0](self.auth, router[1], router[2])
            self.app.include_router(initialized_router.router, prefix=self.prefix)

        @self.app.middleware("http")
        async def add_process_time_header(request: Request, call_next):
            """Adds the process time header to the response"""
            request.state.id = str(uuid.uuid4())
            response = await call_next(request)
            return response
