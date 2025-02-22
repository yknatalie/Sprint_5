import random
import secrets

class Helper:
    @staticmethod
    def generate_email():
        return f'natalia_ivanova_18_{random.randint(1,10000)}@gmail.com'

    @staticmethod
    def generate_password():
        return secrets.token_urlsafe(12)

