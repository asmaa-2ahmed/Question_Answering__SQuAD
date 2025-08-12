# src/config.py
import os
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"

MAX_LENGTH = 384
DOC_STRIDE = 128


# Paths relative to project root
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
MODEL_PATH = os.path.join(ASSETS_DIR, "qa_model")
TOKENIZER_PATH = os.path.join(ASSETS_DIR, "qa_model_tokenizer")

def load_components():
    """Load model and tokenizer from local files"""
    try:
        tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
        model = AutoModelForQuestionAnswering.from_pretrained(MODEL_PATH)
        return model, tokenizer
    except Exception as e:
        raise RuntimeError(f"Failed to load model/tokenizer: {str(e)}")