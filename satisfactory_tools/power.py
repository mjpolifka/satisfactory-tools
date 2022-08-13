from flask import Blueprint, render_template, request

bp = Blueprint("power", __name__, url_prefix='/power')

@bp.route("/")
def power():
    power_type = request.args.get("power_type")
    oil_incoming = request.args.get("oil_incoming")

    data = {
        "power_type": power_type,
        "oil_incoming": oil_incoming
    }
    
    return render_template('power.html', data=data)