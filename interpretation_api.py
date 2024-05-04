from flask import Flask, request, jsonify
from interpreter import interpret

app = Flask(__name__)

@app.route('/interpret', methods=['POST', 'OPTIONS'])
def execute_code():
    if request.method == 'OPTIONS':
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    data = request.json
    code = data['code']
    interpret(code)
    response = jsonify({"message": "Code executed successfully"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)

