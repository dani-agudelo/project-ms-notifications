from .model import Model


class PasswordReset(Model):
    """
    This class is used to send the email to the user to reset the password of the account.
    """

    def __init__(self, email: str, username: str, newPassword: str, resetUrl: str = ""):
        keys = ("username", "email", "newPassword", "resetUrl")
        template = "email_reset_password.html"
        subject = "Restablecimiento de contraseña"
        super().__init__(
            email=email,
            username=username,
            new_password=newPassword,
            reset_url=resetUrl,
            keys=keys,
            template=template,
            subject=subject,
        )
