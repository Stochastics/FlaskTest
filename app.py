"""Flask Application for Paws Rescue Center."""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Paws Rescue Center 🐾"  

@app.route("/about")
def about():
    outstr = """We are a non-profit organization working as an animal \nrescue.
    We aim to help you connect with the purrfect furbaby for you! The animals
    you find on our website are rescued and rehabilitated animals.
    Our mission is to promote the ideology "adopt, don't shop"! "."""
    return outstr

if __name__ == "__main__":
    """ """
    app.run(debug=True, host="0.0.0.0", port=3000)