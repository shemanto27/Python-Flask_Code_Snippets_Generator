from flask import (
    Flask, render_template, 
    session, redirect, 
    request, url_for)

from pygments import highlight
from pygments.formatter import HtmlFormatter
from pygments.lexers import Python3Lexer

app = Flask(__name__)

app.secret_key = "2e9ac41b1e0b66a8d93d66400e2300c4b4c2953f"
PLACEHOLDER_CODE =  "print('Hello, World!')"




@app.context_processor
def context():
    if session.get("code") is None:
        session["code"] = PLACEHOLDER_CODE
    lines = session["code"].split("\n")
    return {
        "message" : "Paste Your Python Code Here 🐍",
        "code" : session["code"],
        "num_lines" : len(lines),
        "max_chars" : len(max(lines, key=len)),
    }


@app.route('/', methods=["GET"])
def code():
    return render_template("code_input.html") 


@app.route("/save_code", methods=["POST"])
def save_code():
    session["code"] = request.form.get("code")
    return redirect(url_for("code"))

@app.route("/reset_session", methods=["POST"])
def reset_session():
    session.clear()
    session["code"] = PLACEHOLDER_CODE
    return redirect(url_for("code"))

@app.route("/style", methods=["GET"])
def style():
    formatter = HtmlFormatter()
    context = {
        "message" : "Select Your Style 🎨",
        "style_definations" : formatter.get_style_defs,
        "style_bg_color" : formatter.style.background_color,
        "highlighted_code" : highlight(session["code"], Python3Lexer(), formatter)
    }
    return render_template("style_selection.html", **context)








if __name__ == '__main__':
    app.run(debug=True)