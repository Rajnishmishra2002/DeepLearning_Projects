# Integer Encoding in Recurrent Neural Networks

This project demonstrates text preprocessing techniques, particularly integer encoding, as part of building Recurrent Neural Network (RNN) models for natural language processing tasks. The code includes steps for tokenizing text data, creating an integer index of words, and handling out-of-vocabulary words using TensorFlow's `Tokenizer`.

## Project Structure

- `data/`: Stores raw and processed data files.
- `notebooks/`: Contains Jupyter notebooks, including the main notebook for integer encoding in RNN (`IntegerEncodinginRNN.ipynb`).
- `src/`: Holds scripts for data preprocessing (`data_preprocessing.py`) and model training (`model_training.py`).
- `models/`: Contains saved models for reuse and evaluation.
- `requirements.txt`: Lists dependencies needed to run the project.
- `.gitignore`: Specifies files to exclude from version control.

## Requirements

To set up the project environment, install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Preprocessing**: The `data_preprocessing.py` script handles text tokenization, integer encoding, and vocabulary management.

   ```python
   from src.data_preprocessing import preprocess_text
   ```

2. **Model Training**: Run `model_training.py` to build and train an RNN model on the preprocessed text data.

3. **Notebook**: You can explore the preprocessing steps and model in detail in `notebooks/IntegerEncodinginRNN.ipynb`.

## Acknowledgments

This project uses TensorFlow's `Tokenizer` for text processing and is intended as an introductory guide to integer encoding for NLP applications.
