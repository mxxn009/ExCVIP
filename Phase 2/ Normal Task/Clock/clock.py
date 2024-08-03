from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def clock():
    now = datetime.now()
    hours = now.strftime('%I')
    minutes = now.strftime('%M')
    seconds = now.strftime('%S')
    return render_template('clock.html', hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)
