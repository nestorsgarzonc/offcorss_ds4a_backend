from flask import Flask, request, send_file
from motion_heatmap import heatmap_video
import shutil
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_route():
    return 'Hello DS4A :)'


@app.route('/uploadHeatmapVideo', methods=['POST'])
def upload_heatmap_video():
    file = request.files['file']
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file, buffer)
    result_path = f'{file.filename}.jpg'
    heatmap_video(file.filename, result_path,
                  frames_sec=1, thresh=4, maxValue=2)
    os.remove(file.filename)
    return send_file(result_path)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
