from flask import Flask, render_template

from forms import SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asifrichrah'

#@app.route('/')
#def home():
 #   return render_template('homepage.html')

@app.route('/')
def search():
    form = SearchForm()
    return render_template('searchbar.html', form=form)

if __name__ == '__main__':
    app.run()