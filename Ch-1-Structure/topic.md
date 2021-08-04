### Topics covered:

- Basic imports
    - Flask
        - to create the app
    - make_response
        - to send responses
    - redirect
        - directs the user to the link specified
- App instance
    - To run a flask app, an app object of class Flask is created
- Routes
    - Function based views
        - decorator is used to define url
        - a function is used to return a response when a client reaches that url
    - Some urls are created by flask by default
    - url_map shows all the url made in app + those which are made by flask
- Server Setup
    - flask comes with a default dev server 
    - Using app.run(debug=True) inables reloader and debugger
