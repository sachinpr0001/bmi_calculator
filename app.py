"""flask app for BMI

Returns:
    float: bmi
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """routing method for bmi

    Returns:
        html: bmi_calc
    """
    bmi = ""
    if request.method == "POST" and "weight" in request.form:
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        bmi = calc_bmi(weight, height)
    return render_template("bmi_calc.html", bmi=bmi)


def calc_bmi(weight, height):
    """return bmi value

    Args:
        weight (float): input weight
        height (float): input height

    Returns:
        float: bmi
    """
    return round((weight / ((height / 100) ** 2)), 2)


app.run()
