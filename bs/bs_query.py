import requests
from bs4 import BeautifulSoup

def search_google(query):
    """Search Google for the given query and return the HTML content."""
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return None
    
    return response.content

def extract_topic_and_bullet_points(html_content):
    """Extract the topic name, subheadings, and bullet points from the HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the main topic name (using <h1>)
    topic_name = soup.find('h1').text if soup.find('h1') else "Unknown Topic"
    
    # Extract h2 and h3 headings
    subheadings = []
    for h2 in soup.find_all('h2'):
        subheadings.append(h2.text.strip())
    for h3 in soup.find_all('h3'):
        subheadings.append(h3.text.strip())

    # Extract bullet points (assuming they are in <li> tags)
    bullet_points = []
    for item in soup.find_all('li'):
        bullet_points.append(item.text.strip())
        if len(bullet_points) == 5:  # Get only the first 5 bullet points
            break

    return topic_name, subheadings, bullet_points

def google_query(queries):
    """Main processing function to search and extract information based on the queries."""
    results = []

    # Convert single string to a list if not already a list
    if type(queries) == str:
        queries = [queries]  # Convert to list if a single string is provided

    for query in queries:
        html_content = search_google(query)  # Step 1: Search for information

        if html_content:
            topic_name, subheadings, bullet_points = extract_topic_and_bullet_points(html_content)  # Step 2: Extract topic, subheadings, and bullet points
            data_list = [topic_name] + subheadings + bullet_points  # Step 3: Store data in a list
            results.append(data_list)
        else:
            results.append(["Failed to retrieve data from the search engine."])
    
    return results

# Example usage
queries = ["Your first topic here", "Your second topic here"]  # Replace with your desired search queries
results = google_query(queries)
print("Retrieved Data:")
print(results)  # Returning the results as a list of lists
