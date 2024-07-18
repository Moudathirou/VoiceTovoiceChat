"""from flask import Flask, render_template, request, jsonify
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
    if 'voice' in request.form and request.form['voice'] == 'true':
        response = generate_response(user_text)
        file_path = TTS(response)
        return jsonify(response=response, audio_file=file_path)
    else:
        response = generate_response(user_text)
        return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)"""

"""from flask import Flask, render_template, request, jsonify
from groq_ai import generate_response
from TTS import TTS
from playsound import playsound
import os
from elevenlabs import play
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_text = request.form['msg']
    response = generate_response(user_text)
    file_path = TTS(response)
    
    
    if 'voice' in request.form and request.form['voice'] == 'true':
        # Play the audio file on the server side
        if file_path:
            playsound(file_path)  # This will play the audio file on Windows
        return jsonify(response=response)
    else:
        return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)"""

from flask import Flask, render_template, request, jsonify, url_for
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
        audio_url = url_for('static', filename=file_path)
    else:
        audio_url = None

    if 'voice' in request.form and request.form['voice'] == 'true':
        return jsonify(response=response, audio_file=audio_url)
    else:
        return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)





