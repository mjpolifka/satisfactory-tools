from flask import Blueprint, render_template, request

bp = Blueprint("handcraft", __name__, url_prefix='/handcraft')

@bp.route("/")
def handcraft():
    single_input = request.args.get("single_input")
    if not single_input:
        single_input = 1
    single_output = request.args.get("single_output")
    if not single_output:
        single_output = 1
    number_of_ticks = request.args.get("number_of_ticks")
    if not number_of_ticks:
        number_of_ticks = 1
    
    cycles_remaining = float(int(single_input) / int(single_output))
    time_remaining = (0.25 * int(number_of_ticks) * cycles_remaining) / 60

    data = {
        "single_input": single_input,
        "single_output": single_output,
        "number_of_ticks": number_of_ticks,
        "cycles_remaining": cycles_remaining,
        "time_remaining": time_remaining
    }
    return render_template('handcraft.html', data=data)