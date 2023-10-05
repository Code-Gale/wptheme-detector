import requests
import re

def get_theme_info(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error

        # Extract the HTML content of the page
        html_content = response.text

        # Use regular expressions to find theme information
        theme_name_match = re.search(r'wp-content/themes/([^/]+)/', html_content)
        theme_author_match = re.search(r'<meta\s+name=["\']author["\']\s+content=["\']([^"\']+)["\']', html_content, re.I)
        theme_version_match = re.search(r'<meta\s+name=["\']version["\']\s+content=["\']([^"\']+)["\']', html_content, re.I)

        # Extract and print the theme information
        theme_name = theme_name_match.group(1) if theme_name_match else "Not found"
        theme_author = theme_author_match.group(1) if theme_author_match else "Not found"
        theme_version = theme_version_match.group(1) if theme_version_match else "Not found"

        print(f"Theme Name: {theme_name}")
        print(f"Author: {theme_author}")
        print(f"Version: {theme_version}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Input URL from the command line
    url = input("Enter the URL of the WordPress website: ")
    get_theme_info(url)
