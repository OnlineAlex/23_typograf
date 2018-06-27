import html
import os
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

import typograf
app = Flask(__name__)
csrf = CSRFProtect(app)
len_secret_keys = 24
csrf.init_app(app)
app.config.update(dict(
    SECRET_KEY=os.urandom(len_secret_keys),
    WTF_CSRF_SECRET_KEY=os.urandom(len_secret_keys)
))


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        text = dict(request.form)['text'][0]
        beautiful_text = typograf.typograph(text)
        return render_template('form.html', text=html.unescape(beautiful_text))

    return render_template('form.html')


if __name__ == "__main__":
    app.run()
