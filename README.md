# AI-Driven News Platform
A personalized news aggregation and summarization platform that uses AI to process and summarize news articles based on user queries.

## Prerequisites

Before running this application, make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
mkdir ai-news-platform
cd ai-news-platform
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install requests beautifulsoup4 nltk
```

4. Install NLTK data:
```python
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> exit()
```

## Configuration

1. Open `exapi.py` and replace the API key with your own Exa API key:
```python
api_key = "your-api-key-here"
```

## Running the Application

1. Run the main script:
```bash
python userinput.py
```

2. Enter your news query when prompted. The application will:
   - Search for relevant news articles
   - Fetch the content
   - Generate a summary
   - Display the results

3. To exit the application, type 'q' when prompted for a query.

## Project Structure

- `userinput.py`: Main script that handles user interaction
- `exapi.py`: Handles communication with the Exa API
- `summarizer.py`: Contains text processing and summarization logic

## Example Usage

```bash
Enter a query ('q' to quit): AI developments in 2023
Results for query 'AI developments in 2023':
[Summary of relevant articles will appear here]

Enter a query ('q' to quit): q
Stopping cron job and exiting...
```

## Error Handling

- If the API key is invalid, you'll receive an authentication error
- If no articles are found for your query, you'll receive a "No results found" message
- If there are connection issues, the application will display an appropriate error message

## Limitations

- API rate limits may apply depending on your Exa API plan
- Summarization is limited to text content; images and videos are not processed
- Articles must be accessible via public URLs

## Troubleshooting

1. If you encounter NLTK errors:
   - Ensure you've downloaded the required NLTK data
   - Try running `python -m nltk.downloader all`

2. If you get API errors:
   - Verify your API key is correctly set
   - Check your internet connection
   - Ensure you're not exceeding API rate limits

## Contributing

Feel free to submit issues and pull requests for any improvements you'd like to suggest.