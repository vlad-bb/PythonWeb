from flask import Flask
from flask_migrate import Migrate
from .db import db

from datetime import datetime
import pytz

app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    ODESSA_TZ = pytz.timezone("Europe/Kiev")
    timeInOdessa = datetime.now(ODESSA_TZ)
    currentTimeInOdessa = timeInOdessa.strftime("%H:%M")
    msg = f"The current time in Odessa is: {currentTimeInOdessa}"
    return msg, currentTimeInOdessa


if __name__ == '__main__':
    app.run()
