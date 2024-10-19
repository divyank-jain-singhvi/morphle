


from flask import Flask
import subprocess
import datetime
import pytz
import os

app = Flask(__name__)


@app.route('/htop')
def htop():
    # Get name (replace with your name)
    name = "sample_name"

    # Get system username
    username = os.getenv('USER', subprocess.getoutput('whoami'))

    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except subprocess.CalledProcessError:
        top_output = "Error fetching top output"

    # Format the response
    response = f"""
    <pre>
Name: {name}
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}
    </pre>
    """

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)