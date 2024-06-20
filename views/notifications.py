from . import *


def validate_model(model: Model, req: dict) -> tuple | None:
    if model.validate_keys(req):
        return
    return jsonify({"error": "Missing keys"}), 400


def send_email(model: Model) -> tuple | Response:
    try:
        message = model.message()

        send = NotificationSerivice.send_email(message)

        if send.get("status") == "Succeeded":
            return jsonify({"message": "Email sent"})

        return jsonify({"error": "Email not sent"}), 500
    except Exception as err:
        return jsonify({"error": "Email not sent"}), 500


def process_request(Model: Model, req: Request) -> Response | tuple:
    try:
        model = Model(**req.get_json())
        error = validate_model(model, req.get_json())

        return error or send_email(model)
    except Exception as err:
        print(err)
        return jsonify({"error": "Arguments not found"}), 400


@app.post("/notifications/send-code")
def send_code_mfa() -> Response | tuple:
    return process_request(CodeMfa, request)


@app.post("/notifications/password-reset")
def send_password_reset() -> Response | tuple:
    return process_request(PasswordReset, request)


@app.post("/notifications/invoice")
def send_invoice() -> Response | tuple:
    return process_request(Invoice, request)


@app.post("/notifications/confirmation-service")
def confirmation_service() -> Response | tuple:
    return process_request(ConfirmationService, request)
