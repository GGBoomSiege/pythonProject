from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def root():
    # return render_template('user_index.html')
    return jsonify({'company': 'OPSOFT'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8081, debug=True)
