from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def compare_hash(plain_text: str, hashed_text: str) -> bool:
    return bcrypt_context.verify(plain_text, hashed_text)

def get_hash(plain_text: str) -> str:
    return bcrypt_context.hash(plain_text)