from .model import Model


class ConfirmationService(Model):
    """
    This class is used to send the email to the user to confirm the service.
    """

    def __init__(self, username: str, email: str, service_info: dict):
        keys = ("username", "email", "service_info")
        template = "confirmation_service.html"
        subject = "Confirmación de servicio"
        super().__init__(
            keys=keys,
            username=username,
            email=email,
            service_info=service_info,
            template=template,
            subject=subject,
        )
