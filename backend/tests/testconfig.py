from fastapi.testclient import TestClient
import sys 
sys.path.append("main")

from backend.app.main import app

client = TestClient(app)
