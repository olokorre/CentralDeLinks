from flask import render_template, make_response
import helper

def log_out():
    return make_response(render_template('login.html', dar = helper.dar()))

def create_user():
    return make_response({
        "message": "ok"
    }, 201)

def log_in():
    return make_response({
        "message": "nice"
    }, 200)

def get_profile(view_user):
    return render_template(
        'profile.html',
        dar = helper.dar(),
        user = 'user[1]',
        user_profile = view_user[1],
        bio_user = view_user[3]
    )

def save_bio():
    return { "messange": "ok" }

def get_select_data():
    return {
        "items": []
    }
