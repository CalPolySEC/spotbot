from flask import Flask, render_template
import spotifyinfo
app = Flask(__name__)
token = spotifyinfo.tokenreauth()

@app.route('/')
def index():
    infile = open('../auth_token', 'r')
    res = spotifyinfo.info(spotifyinfo.tokeneval(infile.readline().strip()))
    infile.close()
    return render_template('index.html', res=res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000, use_reloader=True)
