from flaskblog import app

# To run Project "flask run"
# by default flask will run app.py or run.py
# if we wont to run  different file
# Run for win set FLASK_APP=flaskblog.py
# Run for linex export  FLASK_APP=flaskblog.py
# OR
# python FileName.py
# =================================================================
# debug=True  to update page without restart server
# by default debug=false to change it
# Run for win set FLASK_DEBUG=1
# Run for linex export  FLASK_DEBUG=1
# or
if __name__ == "__main__":
    app.run(debug=True)
