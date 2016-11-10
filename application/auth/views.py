# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash
from . import bpAuth

@bpAuth.route('/login')
def login():
    pass