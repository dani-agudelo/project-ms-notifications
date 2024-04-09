from .model import Model


class CodeMfa(Model):
    """
    This class is used to send the code to the user to verify the 2FA
    """

    def __init__(self, email: str, username: str, code: str, verifyUrl: str):
        keys = ("email", "username", "code", "verifyUrl")
        template = "email_verify_mfa.html"
        subject = "Verificación de codigo de 2FA"
        super().__init__(
            email=email,
            username=username,
            code=code,
            verify_url=verifyUrl,
            keys=keys,
            template=template,
            subject=subject,
        )
