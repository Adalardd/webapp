from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: "flask_request", res: str) -> None:
    with open("vsearch.log", "a") as log:
        print(req, res, file=log)

@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    '''Возвращает результат, полученный при поиске символов во фразе.'''
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results: "
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template("results.html",
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)

@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template("entry.html", the_title="Welcome to search4letters on the web!")

@app.route("/viewlog")
def view_the_log() -> str:
    with open(vsearch.log) as log:
        contents = log.read()
    return contents    

#if __name__ == __"main__":
app.run(debug=True)