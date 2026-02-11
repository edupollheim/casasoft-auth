class TokenManager:
    def __init__(self, session, login_url, username, password, empresa):
        self.session = session
        self.login_url = login_url
        self.username = username
        self.password = password
        self.empresa = empresa
        self._token = None

    def get_token(self):
        if self._token:
            return self._token

        payload = {
            "username": self.username,
            "password": self.password,
            "empresa": self.empresa
        }

        response = self.session.post(
            self.login_url,
            json=payload,
            headers={"Accept": "application/json"},
            timeout=(10, 30)
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Erro login Casasoft: {response.status_code} → {response.text}"
            )

        data = response.json()
        self._token = data.get("access")

        if not self._token:
            raise RuntimeError(f"Token não encontrado: {data}")

        return self._token

    def invalidate(self):
        self._token = None
