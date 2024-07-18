from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from groq_ai import generate_response
from TTS import TTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_text = request.form['msg']
    response = generate_response(user_text)
    file_path = TTS(response)
    
    if file_path:
        audio_url = url_for('get_audio', filename=file_path)
    else:
        audio_url = None

    return jsonify(response=response,audio_file=audio_url)

@app.route('/get_audio/output.wav')
def get_audio():
    return send_from_directory('static', 'output.wav')

if __name__ == "__main__":
    app.run(debug=True)
