class CasasoftClient:
    def __init__(self, session, token_manager):
        self.session = session
        self.token_manager = token_manager

    def request(self, method, url, **kwargs):
        token = self.token_manager.get_token()

        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        kwargs["headers"] = headers
        kwargs.setdefault("timeout", (10, 60))

        response = self.session.request(method, url, **kwargs)

        if response.status_code == 401:
            self.token_manager.invalidate()
            token = self.token_manager.get_token()
            headers["Authorization"] = f"Bearer {token}"
            response = self.session.request(method, url, **kwargs)

        return response
