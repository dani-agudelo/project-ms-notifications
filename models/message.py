class Message:
    """
    A class to represent an email message.
    """

    def __init__(self, subject: str, recipient: str, html: str):
        self.subject = subject
        self.recipient = recipient
        self.html = html
