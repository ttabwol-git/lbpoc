"""This module contains the authentication manager for the API"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
import os
from typing import Optional


class UnauthorizedException(HTTPException):
    def __init__(self, detail: str):
        """Returns HTTP 403"""
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)


class UnauthenticatedException(HTTPException):
    def __init__(self):
        """Returns HTTP 401"""
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication")


class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self):
        """Initializes the PyJWKClient and the configuration for the JWT verification"""
        self.config = {
            'auth0_domain': os.environ['AUTH0_DOMAIN'],
            'auth0_api_audience': os.environ['AUTH0_API_AUDIENCE'],
            'auth0_issuer': os.environ['AUTH0_ISSUER'],
            'auth0_algorithms': os.environ['AUTH0_ALGORITHMS']
        }
        jwks_url = f'https://{self.config["auth0_domain"]}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    async def verify(self, token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())):
        """Verifies the token and returns the payload"""

        # If the token is None, raise an UnauthenticatedException
        if token is None:
            raise UnauthenticatedException

        # Get the signing key from the JWT
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token.credentials).key
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthorizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            raise UnauthorizedException(str(error))

        # Decode the token
        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config['auth0_algorithms'],
                audience=self.config['auth0_api_audience'],
                issuer=self.config['auth0_issuer'],
            )
        except Exception as error:
            raise UnauthorizedException(str(error))

        return payload
