from pytube import YouTube
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/get_audio_url', methods=['GET'])
def get_audio_url():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': 'URL видео не предоставлен'}), 400

    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        return jsonify({'audio_url': audio_stream.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
