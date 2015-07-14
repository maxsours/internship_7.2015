from flask import Flask
app = Flask(__name__)

@app.route('/<int:number>')
def square(number):
    return "%r" % number ** 2
    
if __name__ == "__main__":
    app.run()
