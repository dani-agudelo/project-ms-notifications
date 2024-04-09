from os import getenv

from azure.communication.email import EmailClient

from models.message import Message


class NotificationSerivice:
    """
    This class is used to send via email the message to the user.
    """

    @classmethod
    def load_config(cls) -> tuple:
        return getenv("CONNECTION_STRING"), getenv("SENDER_ADDRESS")

    @classmethod
    def send_email(cls, mens: Message):
        try:
            connection_string, sender_addr = cls.load_config()
            client = EmailClient.from_connection_string(connection_string)

            message = {
                "senderAddress": sender_addr,
                "recipients": {
                    "to": [{"address": mens.recipient}],
                },
                "content": {
                    "subject": mens.subject,
                    "html": mens.html,
                },
            }
            return client.begin_send(message).result()

        except Exception as err:
            raise Exception(f"Error: {err}")
