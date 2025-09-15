from app import create_app   # import factory from app package

app = create_app()

@app.route("/")
def home():
   return "My api is working" 

if __name__ == "__main__":

    app.run(debug=True)
