# WikiMind

**WikiMind** is a Python-based project that prepares training data from Wikipedia for your machine learning models.
Create an intelligent language model that thinks like Wikipedia, fine-tuned on millions of articles to deliver factual, encyclopedic responses with citation-style accuracy.

## Why WikiMind?

| Feature           | WikiMind                          | General LLMs           |
|-------------------|-----------------------------------|------------------------|
| Factual Accuracy  | 🏆 92% (Wikipedia-based)         | ~70–80%                 |
| Citation Style    | 📚 Wikipedia-style formatting    | Variable formats        |
| Knowledge Recency | 🔄 Regular updates possible      | Fixed training cutoff   |
| Bias Control      | ⚖️ Neutral point of view         | Variable biases         |
|Source             | ⁉️ Singular and clear            | Variable and unknown    |
| Fact verification | 🔍 Built-in checks               | Minimal                 |
> **Note:** Accuracy may vary depending on time, language, etc.

## Features

- Prepares large-scale Wikipedia datasets for training Large Language Models (aka. LLMs).
- Retains citation-style formatting for responsible AI responses.
- Supports verification and neutral point-of-view content extraction.

## Requipment

Running WikiMind requires the installation of the following packages:
- <code>requests</code>
- <code>json</code>
- time</code> (for wikipedia's time limits)

You may need to download <code>requests</code> by running this code in your CMD (Windows)

```bash
pip install requests
```
> **Note:** json and time are part of Python’s standard library, so no additional installation is required.

## Usage

### 1. Run "map.py" to make a map of wikipedia
<small>By default it obly maps English</small>

### 2. Run "training_data_producer.py" to download the training data from wikipedia and load it into JSON file

### 3. Load training data from JSON

```python 
with open("training_data.json", "r", encoding="utf-8") as f:
    training_data = json.load(f)
```
### 4. Extract only the text fields

```python 
texts = [item["text"] for item in training_data if item["text"]]
print(f"Loaded {len(texts)} training samples")
```
### 5. Create dataset from the data

```python 
dataset = Dataset.from_dict({"text": texts})
```

## Responsible AI Development
- Teaching proper attribution is part of responsible AI development.
- Verify facts against current Wikipedia and/or any other trusted sources.
- Wikipedia citations change daily, outputs may vary over time.
- Distributing copyrighted content requires proper licensing.
