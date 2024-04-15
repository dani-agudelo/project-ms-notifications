from dotenv import load_dotenv

from views import app


def main():
    load_dotenv()
    app.run(port=5001, debug=True)


if __name__ == "__main__":
    main()



