from flask import Blueprint, render_template, request

bp = Blueprint("power", __name__, url_prefix='/power')

@bp.route("/")
def power():
    
    return render_template('power.html')