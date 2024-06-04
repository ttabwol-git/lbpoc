import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
import uuid

# importing managers
from api.managers.auth import VerifyToken
from api.managers.slack import SlackWebClient

# importing routers
from topics_router import TopicsRouter

# importing engines
from topics_engine import TopicsEngine


class APIConfig:

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.environ['CONFIG_PATH'], 'local.env'))
        self.app = FastAPI()
        RegisterRouters(self.app)


class RegisterRouters:

    def __init__(self, app) -> None:
        self.app = app
        self.auth = VerifyToken()
        self.slack = SlackWebClient()
        self.prefix = '/api'

        self.routers = [
            (TopicsRouter, TopicsEngine(self.slack), '/topics')
        ]

        for router in self.routers:
            initialized_router = router[0](self.auth, router[1], router[2])
            self.app.include_router(initialized_router.router, prefix=self.prefix)

        @self.app.middleware("http")
        async def add_process_time_header(request: Request, call_next):
            request.state.id = str(uuid.uuid4())
            response = await call_next(request)
            return response
