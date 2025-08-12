import torch
from src.config import MAX_LENGTH, DOC_STRIDE, load_components
from src.schemas import QARequest, QAResponse

# Load model/tokenizer once globally
model, tokenizer = load_components()
model.eval()

def answer_question(question: str, context: str) -> dict:
    """
    Runs inference on the given question and context using the trained QA model.
    Returns answer text, start and end positions (char-level), and confidence score.
    """
    # Tokenize inputs with offsets
    inputs = tokenizer(
        question,
        context,
        truncation="only_second",
        max_length=MAX_LENGTH,
        stride=DOC_STRIDE,
        return_tensors="pt",
        padding="max_length",
        return_offsets_mapping=True
    )

    offset_mapping = inputs.pop("offset_mapping")

    with torch.no_grad():
        outputs = model(**inputs)

    start_logits = outputs.start_logits
    end_logits = outputs.end_logits

    start_index = torch.argmax(start_logits).item()
    end_index = torch.argmax(end_logits).item() + 1

    # Decode predicted answer
    answer_tokens = inputs["input_ids"][0][start_index:end_index]
    answer = tokenizer.decode(answer_tokens, skip_special_tokens=True)

    # Convert token positions to character positions
    start_char = offset_mapping[0][start_index][0]
    end_char = offset_mapping[0][end_index - 1][1]

    # Confidence score (product of start and end probs at chosen positions)
    start_probs = torch.nn.functional.softmax(start_logits, dim=1)
    end_probs = torch.nn.functional.softmax(end_logits, dim=1)
    score = (start_probs[0, start_index] * end_probs[0, end_index - 1]).item()

    return {
        "answer": answer.strip(),
        "start": start_char,
        "end": end_char,
        "score": score
    }
