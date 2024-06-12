from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('base.html')

@app.route('/webpages')
def render_webpages_page():  # put application's code here
    return render_template('webpages.html')

@app.route('/styles')
def render_styles_page():  # put application's code here
    return render_template('styles.html')



if __name__ == '__main__':
    app.run()
