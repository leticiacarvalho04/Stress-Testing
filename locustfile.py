# locustfile.py
from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Tempo entre requisições
    
    @task(3)  # Peso maior (executado 3x mais)
    def test_fast_endpoint(self):
        self.client.get("/fast")
    
    @task(2)
    def test_slow_endpoint(self):
        self.client.get("/slow")
    
    @task(1)  # Peso menor
    def test_error_prone_endpoint(self):
        self.client.get("/error-prone")