from os import getenv

from flask import Flask, render_template, request, jsonify
from flask import Request, Response

# Inport Models
from models.model import Model
from models.password_reset import PasswordReset
from models.code_mfa import CodeMfa

# Import Services
from services.notifications_service import NotificationSerivice

app = Flask(
    __name__,
    template_folder="../templates"
)

__flask__ = ['app', 'render_template', 'request', 'Request', 'Response', 'jsonify']
__model__ = ['Model', 'CodeMfa', 'PasswordReset']
__services__ = ['NotificationSerivice']
__other__ = ['getenv']

__all__ = [*__flask__, *__model__, *__services__,  *__other__]

from . import notifications
