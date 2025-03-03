from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # ✅ Import CORS
import os
from datetime import datetime
from diffusers import StableDiffusionPipeline
import torch

app = Flask(__name__)
CORS(app)  # ✅ Enable COR

# Folder to save generated images
IMAGE_FOLDER = "static/images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Load Stable Diffusion Model
MODEL_PATH = "F:/ai models/stable-diffusion-webui/models/Stable-diffusion-diffusers"
pipe = StableDiffusionPipeline.from_pretrained(MODEL_PATH, torch_dtype=torch.float16)
pipe.to("cuda")  # Use GPU

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate Image
    image_filename = f"generated_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    image_path = os.path.join(IMAGE_FOLDER, image_filename)

    with torch.no_grad():
        image = pipe(prompt).images[0]  # Generate image
        image.save(image_path)  # Save image

    return jsonify({"image_url": f"/static/images/{image_filename}"})

# Serve generated images
@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
