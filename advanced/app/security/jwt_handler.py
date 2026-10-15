from jose import jwt

from app.config import SECRET_KEY

ALGORITHM = "HS256"

def create_access_token(data: dict):

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )