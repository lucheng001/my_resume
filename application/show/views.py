# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from . import bpShow

@bpShow.route('/home')
def home():
    return render_template('show/home.html')

@bpShow.route('/info')
def info():
    return render_template('show/info.html')

@bpShow.route('/gallery')
def gallery():
    return render_template('show/gallery.html')

@bpShow.route('/contact')
def contact():
    return render_template('show/contact.html')