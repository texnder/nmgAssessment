from flask import Blueprint, render_template, request, redirect, url_for, send_file, jsonify
from app.models.db import Upload
from app import db
import os


core = Blueprint(
    "core",
    __name__,
)


# Directory where videos will be stored (update as needed)
VIDEO_DIR = "app/static/videos/"



@core.route('/')
def home():
    # List all available videos
    vdos = db.session.execute(db.select(Upload.vdoname).order_by(Upload.id)).scalars()
    return render_template('home.html', videos=vdos)

@core.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        video = request.files['video']
        if video:
            try:
                video.save(VIDEO_DIR + video.filename)
                upload = Upload(vdoname = video.filename)
                db.session.add(upload)
                db.session.commit()
            except:
                return jsonify({'ERROR': 'Please check if file already uploaded.'})

    return redirect(url_for('core.home'))

@core.route('/watch/<video_name>')
def watch(video_name):
    return render_template('watch.html', video_name=video_name)

@core.route('/video/<video_name>')
def video(video_name):
    return send_file( "static/videos/"+ video_name, as_attachment=True)

