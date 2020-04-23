import json

from flask import Flask, render_template, request
import requests

from forms import SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asifrichrah'


# Search form that will take in cuisine ('term' parameter) and city ('location' parameter) from user
@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.is_submitted():
        cuisine_r = request.form['cuisine']
        loc_r = request.form['location']
        params = {'term': cuisine_r, 'location': loc_r}
        api_key = '4OT8ngau2AxIlDyHvrRAugyNpXP8BnXdSGvCDz9pzt6-c8Ff2XIKZNlNpYRFCFSuzJSSkUPYpvKJEqViA0LbclqZKjRe950k37zR73wTLl58060tR5yqcjY_QG15XnYx'
        headers = {'Authorization': 'Bearer %s' % api_key}
        url = 'https://api.yelp.com/v3/businesses/search'

        # make call to Yelp API
        result = requests.get(url, params=params, headers=headers)

        # Convert the JSON string into a dictionary
        business_data = result.json()

        return render_template('foodlist.html', business_data=business_data)
    else:
        return render_template('searchbar.html', form=form)


if __name__ == '__main__':
    app.run()
