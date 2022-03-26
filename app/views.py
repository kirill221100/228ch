from flask import session, redirect, request, url_for, render_template
from sqlalchemy import func
from app.config import Config as cfg
from app.forms import ThreadForm
from app.models import Thread, User
from app import app, db

@app.route('/', methods=['POST', 'GET'])
def board():
    page = request.args.get('page', 1, type=int)
    form = ThreadForm()
    images = []
    if form.validate_on_submit():
        if not session.get('id'):
            if not db.session.query(User).order_by(User.id_user).first():
                usr = User(id_user=1)
                db.session.add(usr)
                db.session.commit()
            else:
                usr = User(id_user=db.session.query(User).order_by(User.id_user.desc()).first().id_user + 1)
                db.session.add(usr)
                db.session.commit()
            session['id'] = usr.id_user
        else:
            usr = User(id_user=session.get('id'))
            db.session.add(usr)
            db.session.commit()

        if form.images.data[0]:
            for i in form.images.data:
                i.save(f'{cfg.UPLOAD_FOLDER}{i.filename}_{usr.id}')
                images.append(i.filename)
        db.session.add(Thread(id=db.session.query(User).order_by(User.id.desc()).first().id, text=form.text.data, images=str(images), creator=session.get('id')))
        db.session.commit()
        return redirect(url_for('thread', id=usr.id))
    res = db.session.query(Thread, func.count(User.id)).outerjoin(User).group_by(Thread.id).order_by(Thread.id.desc()).paginate(page, 10, False)
    next_url = url_for('board', page=res.next_num) if res.has_next else None
    prev_url = url_for('board', page=res.prev_num) if res.has_prev else None
    threads = sorted(list(res.items), key=lambda x: x[1])[::-1]
    return render_template('board.html', form=form, threads=threads, next_url=next_url, prev_url=prev_url)

@app.route('/thread/<int:id>', methods=["POST", "GET"])
def thread(id):
    form = ThreadForm()
    images = []
    if form.validate_on_submit():
        if not session.get('id'):
            usr = User(thread_id=id, id_user=db.session.query(User).order_by(User.id_user.desc()).first().id_user + 1, text=form.text.data)
            db.session.add(usr)
            db.session.commit()
            session['id'] = usr.id_user
        else:
            usr = User(thread_id=id, id_user=session.get('id'), text=form.text.data)
            db.session.add(usr)
            db.session.commit()

        if form.images.data[0]:
            for i in form.images.data:
                i.save(f'{cfg.UPLOAD_FOLDER}{i.filename}_{usr.id}')
                images.append(i.filename)
        usr.images = str(images)
        thread = db.session.query(Thread).filter(Thread.id == id).first()
        thread.answers.append(usr)
        db.session.commit()
        return redirect(url_for('thread', id=id))
    return render_template('thread.html', form=form, thread=db.session.query(Thread).filter(Thread.id==id).first(), id=id)



@app.route('/image/<string:img>')
def image(img):
    return render_template('image.html', img=img)