from flask import Flask,request,json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Webhooks com python'

@app.route('/issue', methods=['POST'])
def issue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    return data

if __name__ == '__main__':
    app.run(debug=True)