from todo import app, curr_date, date, db, datetime
from flask import render_template, request, redirect, url_for
from .models import Task

@app.route("/")
@app.route("/pending")
def pending():
    return render_template("pending.html", curr_date=curr_date, date=date, tasks=Task.query.filter(Task.is_complete == False).all())
        
@app.route("/complete")
def complete():
    return render_template("complete.html", curr_date=curr_date, tasks=Task.query.filter(Task.is_complete == True).all())

@app.route("/add_task", methods=["POST"])
def add_task():
    t1 = Task(name=request.form["name"],
            details=request.form["details"],
            priority=request.form["priority"],
            due = datetime.strptime(request.form["due"], "%Y-%m-%d").date(),
            is_complete = False)
    db.session.add(t1)
    db.session.commit()
    return redirect(url_for("pending"))

@app.route("/clear_all", methods=["POST"])
def clear_all():
    db.drop_all()
    db.create_all()
    return redirect(url_for("pending"))