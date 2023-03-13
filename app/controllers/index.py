from flask import render_template, redirect
import helper

def create_link():
    return redirect('/')

def get_liks():
    return render_template(
        'index.html',
        dar = helper.dar(),
        user = 'teste'
    )
