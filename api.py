from flask import Flask, request

from modules.security import *

app = Flask(__name__)

@app.route('/convert-password', methods=["POST"])
def get_password():
    data = request.args.get('password') #Get password the user
    result = generate_password(data)
    if result:
        return result, 200
    else:
        return result, 500

if __name__ == "__main__":
    app.run(port=5050, debug=True)