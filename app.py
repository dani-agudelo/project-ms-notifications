from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer

from views import app


def main():
    load_dotenv()
    # app.run(port=5001, debug=True) # For development
    WSGIServer(("", 5001), app).serve_forever()  # For production


if __name__ == "__main__":
    main()
