import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


def create_app():
    @app.route("/", methods=["POST", "GET"])
    def home():
        age = None
        months = None
        weeks = None
        days = None
        seconds = None
        hours = None
        if request.method == "POST":
            user_input = request.form.get('content')
            date_of_birth = datetime.datetime.strptime(user_input, "%Y-%m-%d")

            today = datetime.datetime.today()
            user_age = today.year - date_of_birth.year - (
                    (today.month, today.day) < (date_of_birth.month, date_of_birth.day))

            # Age in months
            age_in_months = (today.year - date_of_birth.year) * 12 + (today.month - date_of_birth.month)

            # Age in weeks
            age_in_weeks = abs((date_of_birth - today).days // 7)

            # Age in days
            age_in_days = abs((date_of_birth - today).days)

            # Age in hours
            age_in_hours = age_in_days * 24

            # Age in seconds
            age_in_seconds = age_in_hours * 60 * 60

            if age is None:
                age = user_age

            if months is None:
                months = age_in_months

            if weeks is None:
                weeks = age_in_weeks

            if days is None:
                days = age_in_days

            if hours is None:
                hours = age_in_hours

            if seconds is None:
                seconds = age_in_seconds
        return render_template("home.html", age=age, months=months, weeks=weeks, days=days, hours=hours, seconds=seconds)
    return app


