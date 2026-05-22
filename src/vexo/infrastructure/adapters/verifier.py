import bcrypt

from vexo.application.ports import Verifier


class VerifierImpl(Verifier):
    def verify_password(self, password: str, hashed_password) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
