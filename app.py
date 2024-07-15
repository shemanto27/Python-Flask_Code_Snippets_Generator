from flask import Flask, render_template

app = Flask(__name__)

PLACEHOLDER_CODE =  "print('Hello, World!')"

@app.context_processor
def context():
    return {
        "message" : "Paste Your Python Code Here 🐍",
        "code" : PLACEHOLDER_CODE,
    }


@app.route('/', methods=["GET"])
def code():
    return render_template("code_input.html") 
# The ** unpacks the dictionary context so that each key-value pair in the dictionary is passed as a separate keyword argument to the render_template function.
















if __name__ == '__main__':
    app.run(debug=True)