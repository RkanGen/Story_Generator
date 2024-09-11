# Story_Generator


```markdown
# Children's Story Generator with AI and Image Illustration

This project is an AI-powered children's story generator that creates a unique short story based on a user-provided theme and generates corresponding illustrations for each paragraph using the latest AI models.

## Features

- Generate short children's stories in 5 brief paragraphs based on a user input theme.
- Illustrate each paragraph using AI-generated images.
- Provides a visual and interactive interface for generating stories and viewing illustrations.
- Copy the entire story with a single click for easy sharing.

## Tech Stack

- **Streamlit**: Used to create the user interface.
- **Gemini Model**: Generates the text content (stories).
- **Hugging Face**: Uses Stable Diffusion to generate images for the story.
- **PIL (Python Imaging Library)**: Handles image processing and resizing.

## Setup and Installation

### Requirements

- Python 3.8+
- Create a virtual environment and install dependencies.

```bash
# Clone the repository
git clone https://github.com/RkanGen/Story-Generator.git

# Navigate to the project directory
cd Story-Generator

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory to store your API keys securely.

```bash
HF_API_TOKEN=your-huggingface-api-key
GEMINI_API_KEY=your-gemini-api-key
```

### Run the Application

Once the setup is complete, you can run the application with the following command:

```bash
streamlit run story.py
```

### Models Used

- **Gemini Model**  For generating text content based on the prompt.
- **Stable Diffusion XL** (Hugging Face): For generating high-quality illustrations from text prompts.

## How to Use

1. Enter a theme or name for the story.
2. Click the "Generate Story" button.
3. View the story and corresponding images in the interactive interface.
4. Copy the full story for sharing with the "Copy Story" button.

## Screenshots

### Story and Images Example
![1](https://github.com/user-attachments/assets/829026bd-103c-48c3-90f2-92d6e88a5789)
![2](https://github.com/user-attachments/assets/6e3ffeb4-2b1c-49d3-ad23-539ff074b22b)
![3](https://github.com/user-attachments/assets/ea48be41-68e0-4c35-b7d9-76fae2d9495a)


## Future Enhancements

- Add the ability to download the story as a PDF.
- Provide more customization for the story (e.g., select genres or specific styles).
- Allow users to choose different illustration styles for the images.
- Add memory for image generation model

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
and for The model  is licensed under the proprietary license of its owner.
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## Contact

For any questions or feedback, feel free to reach out:


- **GitHub**: [RkanGen](https://github.com/RkanGen)
```



