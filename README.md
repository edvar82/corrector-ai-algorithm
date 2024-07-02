# Algorithm Explanation

This algorithm processes an image to extract answers from a form. It compares the extracted answers with the correct answers to determine the number of correct and incorrect responses.

## How to Run
1. Ensure you have Python installed.
2. Install the required libraries using `pip install opencv-python numpy`.
3. Place the image file named `imagem.jpeg` in the same directory.
4. Run the `mainWebcan.py` script.

## Files
- `mainWebcan.py`: Contains the main algorithm for processing the image.
- `extrairGabarito.py`: Contains functions for extracting the main content from an image.

## Data Files
- `resp.pkl`: Contains saved options.
- `campos.pkl`: Contains field coordinates.

## Correct Answers
The correct answers are stored in the `respostasCorretas` list.

## Output
The algorithm displays the processed images with markings and the number of correct answers.