from typing import Literal
from fastapi import APIRouter, Security, Request, HTTPException
from pydantic import BaseModel, Field


class TopicsRouter:

    def __init__(self, auth, engine, prefix):
        self.router = APIRouter()
        self.auth = auth
        self.engine = engine
        self.prefix = prefix

        class SubmitParams(BaseModel):
            topic: Literal['sales', 'pricing']
            description: str = Field(..., min_length=10, max_length=10000)

        @self.router.post(f'{self.prefix}/submit')
        async def submit(
            request: Request,
            params: SubmitParams,
            auth_result: str = Security(self.auth.verify)
        ) -> dict:
            try:
                return await self.engine.submit(request, params)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
