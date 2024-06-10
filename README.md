# AI YouTube Video Summarizer
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![last commit](https://img.shields.io/github/last-commit/davidyoo912/youtube_summarizer?color=orange)
![pull requests](https://img.shields.io/github/issues-pr/davidyoo912/youtube_summarizer)
![forks](https://img.shields.io/github/forks/DavidYoo912/youtube_summarizer?style=social)

Simple application to generate transcript summaries from YouTube Videos 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

### Using pip

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DavidYoo912/youtube_summarizer.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd youtube_summarizer
   ```

3. **Install dependencies with pip:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installing requirements.txt, paste and export your OpenAI API key

```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

then, run the following command to start the app 

```bash
   streamlit run app.py
   ```

Paste a YouTube link to summarize its content (must have a transcript available)

![Example Usage](usage_screenshot.png)
