from .model import Model


# This is a class that inherits from the Model class
class Invoice(Model):
    """
    This class is used to send the invoice to the user
    """

    def __init__(self, email: str, username: str, payment_info: dict):
        keys = ("email", "username", "payment_info")
        template = "invoice.html"
        subject = "Comprobante de pago"
        super().__init__(
            keys=keys,
            email=email,
            username=username,
            payment_info=payment_info,
            template=template,
            subject=subject,
        )
