from flask import Flask, render_template, request, redirect
from utils import thumbnail


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        id = request.form.get('id')
        return redirect("/video?id=" + id)
    
    return render_template('index.html')


@app.route('/video')
def video():
    id = request.args.get('id')
    if 'youtube.com' in id:
        url = id
    else:
        url = f"https://www.youtube.com/watch?v={id}"
    
    scraper = thumbnail.Scraper(url)
    try:
        data = scraper.get_data()
        print(data)
        return render_template('video.html', title=data[0], thumbnail=data[1], date=data[2], url=url)
    except Exception:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()   