from website import create_app #We can do this because website has become a python package (due to the init.py)

app = create_app()

if __name__ == '__main__': # now only if you run *this* file then only will the webiste appear
    app.run(debug=True)# (you will probably turn this off in production so you don't have to keep manually run this file for the website)
    