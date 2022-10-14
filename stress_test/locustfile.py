from locust import HttpUser, task


class RequestTest(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello_world_async")
        self.client.get("/hello_world")