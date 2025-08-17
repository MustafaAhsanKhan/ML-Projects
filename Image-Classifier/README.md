# Image Classifier

Streamlit web app wrapping a pre‑trained MobileNetV2 (ImageNet) model to produce top‑3 class predictions for uploaded images (JPG/PNG). Lightweight demo with cached model load and simple probability display.

## Features
- Pretrained MobileNetV2 (1000 ImageNet classes)
- Top‑3 predictions with confidence percentages
- Streamlit UI (drag‑and‑drop upload)
- Model caching via `@st.cache_resource`
- Basic OpenCV + Pillow preprocessing (resize to 224x224, normalization)

## How It Works
1. User uploads an image (jpg/png).
2. Image is resized to 224×224, converted to NumPy, preprocessed (`preprocess_input`).
3. Model predicts logits; `decode_predictions` maps to human labels.
4. Top 3 (label, probability) pairs rendered.

## Requirements
### Prerequisites
- Python 3.13+
- (Recommended) Virtual environment (`uv venv`)

### Key Dependencies
- tensorflow / tensorflow-cpu
- streamlit
- opencv-python
- pillow
- numpy

## Installation
```bash
cd Image-Classifier
uv venv
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate
uv pip install -r requirements.txt   # or: uv pip install .
```

(If you want CPU-only: `uv pip install tensorflow-cpu` instead of full tensorflow.)

## Usage
```bash
streamlit run main.py
```
1. Upload an image.
2. Click "Classify Image".
3. View top‑3 labels with confidence.

## Project Structure
```
Image-Classifier/
├── main.py
├── pyproject.toml
├── README.md
└── (optional) uv.lock
```

## Code Overview (main points)
- `load_model()` loads MobileNetV2 with ImageNet weights.
- `preprocess_image()` handles resize + normalization + batch dimension.
- `classify_image()` runs prediction and decodes top‑3.
- Streamlit caches the model (`@st.cache_resource`) to avoid reloads.

## Extending
- Add drag‑and‑drop multiple image batch processing.
- Display raw probabilities as a horizontal bar chart.
- Support additional architectures (EfficientNet, ResNet50) via a selector.
- Add Grad-CAM / saliency visualization for interpretability.

## Limitations
- Restricted to 1000 ImageNet classes (may mislabel domain‑specific objects).
- No GPU configuration flags (TensorFlow will auto-detect).
- Minimal error handling (basic exception wrapper).

## Example Output
```
Predictions
golden_retriever: 87.12%
Labrador_retriever: 7.45%
cocker_spaniel: 2.11%
```

## License
MIT (see repository root).

## Contributions
PRs / issues welcome.

## Acknowledgements
- TensorFlow / Keras pretrained models
- Streamlit for rapid UI
- ImageNet label set