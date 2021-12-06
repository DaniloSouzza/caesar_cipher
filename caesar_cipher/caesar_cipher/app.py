from flask import Flask, render_template, request
from utils.utils import Cipher, Date

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    data = {
            'date': Date.get_year()
        }

    if request.method == 'POST' and 'to_encrypt' in request.form:

        cipher = Cipher(request.form['to_encrypt'], 3)
        data['encrypt'] = cipher.cipher_encrypt()

        return render_template(
            'main_page.html',
            data=data
        )

    if request.method == 'POST' and 'to_decrypt' in request.form:

        cipher = Cipher(request.form['to_decrypt'], 3)
        data['decrypt'] = cipher.cipher_decrypt()

        return render_template(
            'main_page.html',
            data=data
        )

    if request.method == 'GET':
        return render_template(
            'main_page.html',
            data=data
        )


if __name__ == "__main__":
    app.run(debug=True)
