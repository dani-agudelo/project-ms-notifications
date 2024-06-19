from datetime import datetime
from os import getenv

from flask import Flask, Request, Response, jsonify, render_template, request
from flask_cors import CORS

from models.code_mfa import CodeMfa
from models.invoice import Invoice
from models.model import Model
from models.password_reset import PasswordReset
from services.notifications_service import NotificationSerivice

app = Flask(__name__, template_folder="../templates")
CORS(app)


@app.template_filter("datetime_format")
def datetime_format(value, format: str):
    return datetime.fromisoformat(str(value)).strftime(format)


@app.template_filter("currency_format")
def currency_format(value):
    return f"${value:,.2f}"


__flask__ = ["app", "render_template", "request", "Request", "Response", "jsonify"]
__model__ = ["Model", "CodeMfa", "PasswordReset", "Invoice"]
__services__ = ["NotificationSerivice"]
__other__ = ["getenv"]

__all__ = __flask__ + __model__ + __services__ + __other__

from . import notifications
