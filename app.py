import os
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    time_now = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    
    return """
    <h1>Hello there, I'm a simple python app"</h1>
    <p>The current time is: {time}</p>
    """.format(time=time_now)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    from flask import Flask
from datetime import datetime
app = Flask(__name__)

