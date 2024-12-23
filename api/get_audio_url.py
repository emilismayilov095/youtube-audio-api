import yt_dlp
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/get_audio_url', methods=['GET'])
def get_audio_url():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': 'URL видео не предоставлен'}), 400

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
            return jsonify({'audio_url': audio_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
