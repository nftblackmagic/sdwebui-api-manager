from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

