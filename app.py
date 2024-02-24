from src.factory import APP as app

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True, load_dotenv=True)
