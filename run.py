from dash import create_app
from db import db_create
app = create_app()
db_create()
if __name__ == '__main__':   
    app.run(debug=True)