from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=["POST"])
def checkout():
    values = dict(request.form.items())
    print(request.form)
    # total_fruit = values.
    return render_template('checkout.html', values=values)

if __name__ == '__main__':
    app.run(debug=True)