# casasoft-auth

Cliente Python para autenticação e requisições autenticadas na API
**Casasoft / CloudSlim**.

Este pacote abstrai: - Login - Gerenciamento de token JWT - Renovação
automática em caso de expiração - Session HTTP com retry

Ideal para **ETLs**, **integrações**, **scripts**, **APIs** e
**automação**.

------------------------------------------------------------------------

## 📦 Instalação

Com `pip`:

``` bash
pip install casasoft-auth
```

Ou com `uv` (recomendado):

``` bash
uv pip install casasoft-auth
```

------------------------------------------------------------------------

## 🚀 Uso básico

``` python
from casasoft_auth import create_session, TokenManager, CasasoftClient

LOGIN_URL = "https://auth.api.cloudslim.com.br/login"

session = create_session()

token_manager = TokenManager(
    session=session,
    login_url=LOGIN_URL,
    username="SEU_USUARIO",
    password="SUA_SENHA",
    empresa="CODIGO_EMPRESA"
)

client = CasasoftClient(session, token_manager)

response = client.request(
    "GET",
    "https://integracao.api.cloudslim.com.br/lancamentos",
    params={"periodo": "01/2026"}
)

print(response.json())
```

------------------------------------------------------------------------

## 🔐 Boas práticas (importante)

❌ **Nunca versionar credenciais**

Use variáveis de ambiente:

``` python
import os

token_manager = TokenManager(
    session=session,
    login_url=LOGIN_URL,
    username=os.getenv("CASASOFT_USER"),
    password=os.getenv("CASASOFT_PASS"),
    empresa=os.getenv("CASASOFT_EMPRESA"),
)
```

Exemplo `.env`:

``` env
CASASOFT_USER=api@empresa.com.br
CASASOFT_PASS=senha_super_secreta
CASASOFT_EMPRESA=CODIGO_EMPRESA
```

------------------------------------------------------------------------

## 🧠 O que o pacote faz automaticamente

-   🔁 Retry em erros 5xx
-   🔄 Renovação automática do token em 401
-   🧩 Reutilização de session HTTP
-   🧼 Interface simples e limpa

------------------------------------------------------------------------

## 📌 Requisitos

-   Python \>= 3.9
-   requests \>= 2.28

------------------------------------------------------------------------

## 📄 Licença

MIT License

------------------------------------------------------------------------

## 👤 Autor

Eduardo Henrique Pollheim
