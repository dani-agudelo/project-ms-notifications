from abc import ABC
from datetime import datetime

from flask import render_template

from .message import Message

# ABC is used to create an abstract class
class Model(ABC):
    """
    This class is used to create a model that can be converted to a json representation
    and can be used to create a message object.
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.template = ""
        self.subject = ""
        self.email = ""
        self.keys = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.date = datetime.now().strftime("%d %b, %Y")
        self.html = render_template(self.template, **self.json())

    def message(self):
        """
        Returns a Message object with the model's attributes.
        """
        return Message(self.subject, self.email, self.html)

    def validate_keys(self, req: dict) -> bool:
        """
        Checks if the keys are in the request.
        """
        return all(k in req for k in self.keys)

    def json(self):
        """
        Returns a dictionary with the model's attributes.
        """
        return {k: v for k, v in self.__dict__.items() if not k.startswith("__")}
