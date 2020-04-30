from app import app
from flask import Flask ,render_template, request, redirect, url_for, flash
import datetime
import time

from flask_socketio import SocketIO,emit,join_room

socketio=SocketIO(app )

###
# Routing for your application.
###

@app.route('/first')
def first():
    """Render website's home page."""
    date = format_date_joined()
    return render_template('first.html',date=date)

@app.route('/')
def chat2():
    date = format_date_joined()
    return render_template('chat2.html',date=date)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


# @app.route('/')
# def home():
#     """Render website's home page."""
    
#     return render_template('index.html')






def format_date_joined():
    datetime.datetime.now()
    date_joined = datetime.datetime.now()
    return "Today is "     + date_joined.strftime("%A,%B,%d ,%Y") 


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




if __name__ == '__main__':
    socketio.run(app)
    app.run(debug=True, host="0.0.0.0", port="8080")
