from functools import wraps
from flask import Response, request, g
from flask_login import login_user as login_flask, current_user, logout_user, login_required


def adminMiddleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        if current_user.role_id == 1: 
            return func(*args, **kwargs)

        if current_user.role_id == 2: 
            return func(*args, **kwargs)

        return Response('No esta autozizado para ver esta Ruta', mimetype='text/plain', status=401)

    return decorated_function



def userMiddleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        if current_user.role_id == 1: 
            return func(*args, **kwargs)

        if current_user.role_id == 3: 
            return func(*args, **kwargs)

        return Response('No esta autozizado para ver esta Ruta', mimetype='text/plain', status=401)

    return decorated_function

