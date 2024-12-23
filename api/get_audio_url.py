import yt_dlp
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/get_audio_url', methods=['POST'])
def get_audio_url():
    data = request.json
    cookies = data.get('cookies')
    video_url = data.get('url')

    if not cookies or not video_url:
        return jsonify({'error': 'No cookies or URL provided'}), 400

    try:
        # Сохраняем cookies во временный файл
        with open('cookies.txt', 'w') as f:
            f.write(cookies)

        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'cookiefile': 'cookies.txt'  # Используем файл cookies
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
            return jsonify({'audio_url': audio_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
