from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
