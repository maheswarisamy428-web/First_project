from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name = "Maheswari"
    a = 20
    b = 5

    return f"""
    <h1>Simple Python Program</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Addition:</b> {a + b}</p>
    <p><b>Subtraction:</b> {a - b}</p>
    <p><b>Multiplication:</b> {a * b}</p>
    <p><b>Division:</b> {a / b}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
