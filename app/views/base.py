from datetime import datetime

from flask import Blueprint, render_template

from app.models import db
from app.models.db_models import Name

base = Blueprint("base", __name__)


@base.route("/", methods=["GET", "POST"])
def index():
    # team_names = [row]
    team_name_today = "Node Package Manager"
    return render_template("index.html", name=team_name_today)
