"""Module for the topics router"""

from fastapi import APIRouter, HTTPException, Request, Security
from pydantic import BaseModel, Field
from typing import Literal


class TopicsRouter:
    """Class for the topics router"""

    def __init__(self, auth, engine, prefix):
        self.router = APIRouter()
        self.auth = auth
        self.engine = engine
        self.prefix = prefix

        class SubmitParams(BaseModel):
            """Class for the submit endpoint params"""
            topic: Literal['sales', 'pricing']
            description: str = Field(..., min_length=10, max_length=10000)

        @self.router.post(f'{self.prefix}/submit')
        async def submit(
            request: Request,
            params: SubmitParams,
            auth_result: str = Security(self.auth.verify)
        ) -> dict:
            """Endpoint for submitting a topic"""
            try:
                return await self.engine.submit(request, params)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
