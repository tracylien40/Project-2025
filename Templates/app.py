from flask import Flask

#the Flask class
app = Flask(__name__)

# This the defined route in its corresponding view function
@app.route("/")
def home():
    return render_template("index.html")
    
 





# When you run the flask application a page should come upon the screen
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7002
            )