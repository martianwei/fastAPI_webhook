from dotenv import load_dotenv
from fastapi import FastAPI, Header, Request, HTTPException
import http
import os
import hmac
import hashlib
load_dotenv()
app = FastAPI()
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')


def generate_hash_signature(
    secret: bytes,
    payload: bytes,
    digest_method=hashlib.sha1
):
    return hmac.new(secret, payload, digest_method).hexdigest()


@app.post("/webhook", status_code=http.HTTPStatus.OK)
async def webhook(request: Request, x_hub_signature: str = Header(None)):
    payload = await request.body()
    # secert = WEBHOOK_SECRET.encode("utf-8")
    # signature = generate_hash_signature(secert, payload)
    # if x_hub_signature != f"sha1={signature}":
    #     raise HTTPException(status_code=401, detail="Authentication error")
    # else:
    print(payload)
    return {}
