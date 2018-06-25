import html

from flask import Flask, render_template, request
import typograf
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        text = dict(request.form)['text'][0]
        beautiful_text = typograf.typograph(text)
        print(beautiful_text)
        return render_template('form.html', text=html.unescape(beautiful_text))

    return render_template('form.html')


if __name__ == "__main__":
    app.run()
