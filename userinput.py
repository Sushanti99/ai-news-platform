# app.py
import requests
import time
from exapi import exa_response
from summarizer import return_summary


def search_news(query):
    """
    Search the news data for matching articles based on the user query.
    """
    response = exa_response(query)
    return response


def main():
    """
    The main CLI loop that handles user input and news data updates.
    """
    while True:
        query = input("Enter a query ('q' to quit): ")

        if query.lower() == 'q':
            print("Stopping cron job and exiting...")
            break

        results = search_news(query)
        if results:
            print(f"Results for query '{query}':")
            print("Results: ", results)
        else:
            print(f"No results found for query '{query}'.")

        time.sleep(1)


if __name__ == "__main__":
    main()