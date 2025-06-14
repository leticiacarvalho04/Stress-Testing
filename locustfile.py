from locust import HttpUser, task, between
import random

class PerformanceUser(HttpUser):
    wait_time = between(0.5, 2)
    
    @task(3)
    def fast_endpoint(self):
        self.client.get("/fast")
    
    @task(5)
    def db_operation(self):
        self.client.get("/heavy-db")
    
    @task(1)
    def intensive_operations(self):
        if random.random() > 0.5:
            self.client.get("/memory-intensive")
        else:
            self.client.get("/cpu-intensive")