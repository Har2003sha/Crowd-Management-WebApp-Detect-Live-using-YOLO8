# from flask import Flask, render_template, Response, request, redirect, url_for, session, jsonify
# import cv2
# from ultralytics import YOLO
# import numpy as np
# import matplotlib
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io
# import threading
# import time

# app = Flask(__name__)
# app.secret_key = 'crowd_secret_key'

# # Load YOLOv8 model
# model = YOLO('yolov8n.pt')

# cap = cv2.VideoCapture(0)
# lock = threading.Lock()

# last_person_count = 0
# last_update_ts = 0.0

# # Thresholds
# SAFE_LIMIT = 10
# INTERMEDIATE_LIMIT = 20
# HIGH_LIMIT = 30


# def person_count_from_results(results):
#     if not results:
#         return 0
#     res0 = results[0]
#     if getattr(res0, 'boxes', None) is None:
#         return 0
#     return int(len(res0.boxes))


# def generate_heatmap(frame, results):
#     height, width, _ = frame.shape
#     data = np.zeros((height, width), dtype=np.float32)

#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

#             data[max(0, cy - 25):min(height, cy + 25),
#                  max(0, cx - 25):min(width, cx + 25)] += 3

#     plt.figure(figsize=(6, 4))
#     sns.heatmap(data, cmap='jet', cbar=False, xticklabels=False, yticklabels=False)

#     buf = io.BytesIO()
#     plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
#     plt.close()
#     return buf.getvalue()


# def frame_loop(is_heatmap: bool):
#     global last_person_count, last_update_ts

#     while True:
#         success, frame = cap.read()
#         if not success:
#             time.sleep(0.05)
#             continue

#         with lock:
#             results = model(frame, classes=0, verbose=False)
#             count = person_count_from_results(results)
#             last_person_count = count
#             last_update_ts = time.time()

#         if is_heatmap:
#             frame_bytes = generate_heatmap(frame, results)
#             content_type = b"image/png"
#         else:
#             annotated_frame = results[0].plot()
#             ok, buffer = cv2.imencode('.jpg', annotated_frame)
#             if not ok:
#                 continue
#             frame_bytes = buffer.tobytes()
#             content_type = b"image/jpeg"

#         yield (
#             b'--frame\r\n'
#             b'Content-Type: ' + content_type + b'\r\n\r\n' + frame_bytes + b'\r\n'
#         )


# @app.route('/')
# def index():
#     if 'user' in session:
#         return redirect(url_for('dashboard'))
#     return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     if username == 'admin' and password == 'password123':
#         session['user'] = username
#         return redirect(url_for('dashboard'))

#     return "Invalid Credentials"


# @app.route('/dashboard')
# def dashboard():
#     if 'user' not in session:
#         return redirect(url_for('index'))
#     return render_template('dashboard.html')


# @app.route('/video_feed')
# def video_feed():
#     return Response(frame_loop(is_heatmap=False),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/heatmap_feed')
# def heatmap_feed():
#     return Response(frame_loop(is_heatmap=True),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/get_stats')
# def get_stats():
#     with lock:
#         count = int(last_person_count)
#         ts = float(last_update_ts)

#     # Risk logic
#     if count <= SAFE_LIMIT:
#         risk = "SAFE"
#         color = "green"
#     elif count <= INTERMEDIATE_LIMIT:
#         risk = "INTERMEDIATE"
#         color = "yellow"
#     else:
#         risk = "HIGH RISK"
#         color = "red"

#     return jsonify({
#         "count": count,
#         "updated_at": ts,
#         "risk": risk,
#         "color": color
#     })


# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, Response, request, redirect, url_for, session, jsonify
# import cv2
# from ultralytics import YOLO
# import numpy as np
# import matplotlib
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io
# import threading
# import time
# from playsound import playsound
# import os


# app = Flask(__name__)
# app.secret_key = 'crowd_secret_key'

# # Load YOLOv8 model
# model = YOLO('yolov8n.pt')

# cap = cv2.VideoCapture(0)
# lock = threading.Lock()

# last_person_count = 0
# last_update_ts = 0.0

# # Thresholds
# SAFE_LIMIT = 0
# INTERMEDIATE_LIMIT = 0
# HIGH_LIMIT = 1


# def person_count_from_results(results):
#     if not results:
#         return 0
#     res0 = results[0]
#     if getattr(res0, 'boxes', None) is None:
#         return 0
#     return int(len(res0.boxes))


# def generate_heatmap(frame, results):
#     height, width, _ = frame.shape
#     data = np.zeros((height, width), dtype=np.float32)

#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

#             data[max(0, cy - 25):min(height, cy + 25),
#                  max(0, cx - 25):min(width, cx + 25)] += 3

#     plt.figure(figsize=(6, 4))
#     sns.heatmap(data, cmap='jet', cbar=False, xticklabels=False, yticklabels=False)

#     buf = io.BytesIO()
#     plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
#     plt.close()
#     return buf.getvalue()


# def frame_loop(is_heatmap: bool):
#     global last_person_count, last_update_ts

#     while True:
#         success, frame = cap.read()
#         if not success:
#             time.sleep(0.05)
#             continue

#         with lock:
#             results = model(frame, classes=0, verbose=False)
#             count = person_count_from_results(results)
#             last_person_count = count
#             last_update_ts = time.time()

#         if is_heatmap:
#             frame_bytes = generate_heatmap(frame, results)
#             content_type = b"image/png"
#         else:
#             annotated_frame = results[0].plot()
#             ok, buffer = cv2.imencode('.jpg', annotated_frame)
#             if not ok:
#                 continue
#             frame_bytes = buffer.tobytes()
#             content_type = b"image/jpeg"

#         yield (
#             b'--frame\r\n'
#             b'Content-Type: ' + content_type + b'\r\n\r\n' + frame_bytes + b'\r\n'
#         )


# # -------------------- ROUTES -------------------- #

# @app.route('/')
# def index():
#     # Agar user already login hai, direct dashboard
#     if 'user' in session:
#         return redirect(url_for('dashboard'))
#     return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     # Accept ANY username/password (Demo mode)
#     if username and password:
#         session['user'] = username
#         return redirect(url_for('dashboard'))

#     return "Please enter username and password!"


# @app.route('/dashboard')
# def dashboard():
#     if 'user' not in session:
#         return redirect(url_for('index'))

#     return render_template('dashboard.html', user=session['user'])


# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('index'))


# @app.route('/video_feed')
# def video_feed():
#     return Response(frame_loop(is_heatmap=False),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/heatmap_feed')
# def heatmap_feed():
#     return Response(frame_loop(is_heatmap=True),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/get_stats')
# def get_stats():
#     with lock:
#         count = int(last_person_count)
#         ts = float(last_update_ts)

#     # Risk logic
#     if count <= SAFE_LIMIT:
#         risk = "SAFE"
#         color = "green"
#     elif count <= INTERMEDIATE_LIMIT:
#         risk = "INTERMEDIATE"
#         color = "yellow"
#     else:
#         risk = "HIGH RISK"
#         color = "red"

#     return jsonify({
#         "count": count,
#         "updated_at": ts,
#         "risk": risk,
#         "color": color
#     })


# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, Response, request, redirect, url_for, session, jsonify
# import cv2
# from ultralytics import YOLO
# import numpy as np
# import matplotlib
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io
# import threading
# import time
# from playsound import playsound
# import os

# app = Flask(__name__)
# app.secret_key = 'crowd_secret_key'

# # Load YOLOv8 model
# model = YOLO('yolov8n.pt')

# cap = cv2.VideoCapture(0)
# lock = threading.Lock()

# last_person_count = 0
# last_update_ts = 0.0

# # Thresholds
# SAFE_LIMIT = 0
# INTERMEDIATE_LIMIT = 0
# HIGH_LIMIT = 1  # HIGH RISK start here

# # Alarm variables
# alarm_thread_running = False
# alarm_stop_flag = False


# def person_count_from_results(results):
#     if not results:
#         return 0
#     res0 = results[0]
#     if getattr(res0, 'boxes', None) is None:
#         return 0
#     return int(len(res0.boxes))


# def generate_heatmap(frame, results):
#     height, width, _ = frame.shape
#     data = np.zeros((height, width), dtype=np.float32)

#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

#             data[max(0, cy - 25):min(height, cy + 25),
#                  max(0, cx - 25):min(width, cx + 25)] += 3

#     plt.figure(figsize=(6, 4))
#     sns.heatmap(data, cmap='jet', cbar=False, xticklabels=False, yticklabels=False)

#     buf = io.BytesIO()
#     plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
#     plt.close()
#     return buf.getvalue()


# def play_alarm_loop():
#     """Alarm continuously bajega jab tak stop flag true nahi hota"""
#     global alarm_thread_running, alarm_stop_flag

#     alarm_thread_running = True

#     alarm_path = os.path.join("static", "mixkit-emergency-alert-alarm-1007.wav")

#     while not alarm_stop_flag:
#         try:
#             playsound(alarm_path)
#         except:
#             pass

#     alarm_thread_running = False


# def frame_loop(is_heatmap: bool):
#     global last_person_count, last_update_ts

#     while True:
#         success, frame = cap.read()
#         if not success:
#             time.sleep(0.05)
#             continue

#         with lock:
#             results = model(frame, classes=0, verbose=False)
#             count = person_count_from_results(results)
#             last_person_count = count
#             last_update_ts = time.time()

#         if is_heatmap:
#             frame_bytes = generate_heatmap(frame, results)
#             content_type = b"image/png"
#         else:
#             annotated_frame = results[0].plot()
#             ok, buffer = cv2.imencode('.jpg', annotated_frame)
#             if not ok:
#                 continue
#             frame_bytes = buffer.tobytes()
#             content_type = b"image/jpeg"

#         yield (
#             b'--frame\r\n'
#             b'Content-Type: ' + content_type + b'\r\n\r\n' + frame_bytes + b'\r\n'
#         )


# # -------------------- ROUTES -------------------- #

# @app.route('/')
# def index():
#     if 'user' in session:
#         return redirect(url_for('dashboard'))
#     return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     # Accept ANY username/password (Demo mode)
#     if username and password:
#         session['user'] = username
#         return redirect(url_for('dashboard'))

#     return "Please enter username and password!"


# @app.route('/dashboard')
# def dashboard():
#     if 'user' not in session:
#         return redirect(url_for('index'))

#     return render_template('dashboard.html', user=session['user'])


# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('index'))


# @app.route('/video_feed')
# def video_feed():
#     return Response(frame_loop(is_heatmap=False),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/heatmap_feed')
# def heatmap_feed():
#     return Response(frame_loop(is_heatmap=True),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/get_stats')
# def get_stats():
#     global alarm_stop_flag, alarm_thread_running

#     with lock:
#         count = int(last_person_count)
#         ts = float(last_update_ts)

#     # Risk logic
#     if count <= SAFE_LIMIT:
#         risk = "SAFE"
#         color = "green"

#         # STOP alarm
#         alarm_stop_flag = True

#     elif count <= INTERMEDIATE_LIMIT:
#         risk = "INTERMEDIATE"
#         color = "yellow"

#         # STOP alarm
#         alarm_stop_flag = True

#     else:
#         risk = "HIGH RISK"
#         color = "red"

#         # START alarm
#         if not alarm_thread_running:
#             alarm_stop_flag = False
#             threading.Thread(target=play_alarm_loop, daemon=True).start()

#     return jsonify({
#         "count": count,
#         "updated_at": ts,
#         "risk": risk,
#         "color": color
#     })


# if __name__ == '__main__':
#     app.run(debug=True)







from flask import Flask, render_template, Response, request, redirect, url_for, session, jsonify
import cv2
from ultralytics import YOLO
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import io
import threading
import time
from playsound import playsound
import os

app = Flask(__name__)
app.secret_key = 'crowd_secret_key'

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)
lock = threading.Lock()

last_person_count = 0
last_update_ts = 0.0

SAFE_LIMIT = 10
INTERMEDIATE_LIMIT = 20
HIGH_LIMIT = 30

alarm_thread_running = False
alarm_stop_flag = False

# ✅ NEW FLAG (important)
manual_mute = False


def person_count_from_results(results):
    if not results:
        return 0
    res0 = results[0]
    if getattr(res0, 'boxes', None) is None:
        return 0
    return int(len(res0.boxes))


def generate_heatmap(frame, results):
    height, width, _ = frame.shape
    data = np.zeros((height, width), dtype=np.float32)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            data[max(0, cy - 25):min(height, cy + 25),
                 max(0, cx - 25):min(width, cx + 25)] += 3

    plt.figure(figsize=(6, 4))
    sns.heatmap(data, cmap='jet', cbar=False, xticklabels=False, yticklabels=False)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    return buf.getvalue()


def play_alarm_loop():
    global alarm_thread_running, alarm_stop_flag

    alarm_thread_running = True
    alarm_path = os.path.join("static", "mixkit-emergency-alert-alarm-1007.wav")

    while not alarm_stop_flag:
        try:
            playsound(alarm_path)
        except:
            pass

    alarm_thread_running = False


def frame_loop(is_heatmap: bool):
    global last_person_count, last_update_ts

    while True:
        success, frame = cap.read()
        if not success:
            time.sleep(0.05)
            continue

        with lock:
            results = model(frame, classes=0, verbose=False)
            count = person_count_from_results(results)
            last_person_count = count
            last_update_ts = time.time()

        if is_heatmap:
            frame_bytes = generate_heatmap(frame, results)
            content_type = b"image/png"
        else:
            annotated_frame = results[0].plot()
            ok, buffer = cv2.imencode('.jpg', annotated_frame)
            if not ok:
                continue
            frame_bytes = buffer.tobytes()
            content_type = b"image/jpeg"

        yield (
            b'--frame\r\n'
            b'Content-Type: ' + content_type + b'\r\n\r\n' + frame_bytes + b'\r\n'
        )


@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        session['user'] = username
        return redirect(url_for('dashboard'))

    return "Please enter username and password!"


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', user=session['user'])


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/video_feed')
def video_feed():
    return Response(frame_loop(is_heatmap=False),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/heatmap_feed')
def heatmap_feed():
    return Response(frame_loop(is_heatmap=True),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ✅ STOP ALARM (manual mute true)
@app.route('/stop_alarm', methods=['POST'])
def stop_alarm():
    global alarm_stop_flag, manual_mute
    alarm_stop_flag = True
    manual_mute = True
    return jsonify({"status": "Alarm Stopped"})


@app.route('/get_stats')
def get_stats():
    global alarm_stop_flag, alarm_thread_running, manual_mute

    with lock:
        count = int(last_person_count)
        ts = float(last_update_ts)

    if count <= SAFE_LIMIT:
        risk = "SAFE"
        color = "green"
        alarm_stop_flag = True
        manual_mute = False  # ✅ reset mute when safe

    elif count <= INTERMEDIATE_LIMIT:
        risk = "INTERMEDIATE"
        color = "yellow"
        alarm_stop_flag = True
        manual_mute = False  # ✅ reset mute when intermediate

    else:
        risk = "HIGH RISK"
        color = "red"

        # ✅ alarm will start only if not muted
        if not manual_mute:
            if not alarm_thread_running:
                alarm_stop_flag = False
                threading.Thread(target=play_alarm_loop, daemon=True).start()

    return jsonify({
        "count": count,
        "updated_at": ts,
        "risk": risk,
        "color": color
    })


if __name__ == '__main__':
    app.run(debug=True)