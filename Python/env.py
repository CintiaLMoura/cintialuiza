from dotenv import load_dotenv
import os

load_dotenv()

usuario = os.getenv("USUARIO_BOT")
senha = os.getenv("SENHA_BOT")

print(usuario, senha)