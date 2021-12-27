from logging import error
from flask import Blueprint, render_template, redirect, url_for
from flask_discord import Unauthorized

errors = Blueprint('errors', __name__)

@errors.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("login"))

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500