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

def search_wikipedia(query):
    """Search Wikipedia for the given query and return the HTML content."""
    search_url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
    response = requests.get(search_url)

    if response.status_code != 200:
        return None
    
    return response.content

def convert_to_latex(formula):
    """Convert mathematical formula to LaTeX format."""
    # Example of simple conversion, you can expand this based on other formula structures
    latex_formula = formula.replace('^', '**')  # Handle exponents
    latex_formula = latex_formula.replace('*', '\\cdot ')  # Handle multiplication
    latex_formula = latex_formula.replace('=', '\\equiv ')  # Handle equality
    return f"${latex_formula}$"  # Encapsulate in LaTeX math mode

def extract_wikipedia_info(html_content):
    """Extract definitions, headings, formulas, and summaries from the Wikipedia page."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Definition of topic (first paragraph)
    definition = soup.find('p').text if soup.find('p') else "No definition found."

    # 2. Definitions of all headings
    headings_definitions = {}
    for heading in soup.find_all(['h2', 'h3']):
        heading_text = heading.text.strip()
        next_para = heading.find_next_sibling()
        if next_para and next_para.name == 'p':
            headings_definitions[heading_text] = next_para.text.strip()

    # 3. Definitions of all subheadings
    subheadings_definitions = {}
    for subheading in soup.find_all('h3'):
        subheading_text = subheading.text.strip()
        next_para = subheading.find_next_sibling()
        if next_para and next_para.name == 'p':
            subheadings_definitions[subheading_text] = next_para.text.strip()

    # 4. List of all mathematical formulae on page and convert to LaTeX
    formulas = []
    for math in soup.find_all('math'):
        raw_formula = math.text.strip()
        latex_formula = convert_to_latex(raw_formula)  # Convert to LaTeX format
        formulas.append(latex_formula)

    # 5. Summary of all paragraphs (first 5 points)
    paragraphs = soup.find_all('p')
    summary = []
    for para in paragraphs[:5]:  # Get first 5 paragraphs
        summary.append(para.text.strip())
    
    return definition, headings_definitions, subheadings_definitions, formulas, summary

def wikipedia_query(queries):
    """Main processing function to search and extract information from Wikipedia."""
    results = []

    for query in queries:
        html_content = search_wikipedia(query)  # Step 1: Search for Wikipedia information

        if html_content:
            definition, headings, subheadings, formulas, summary = extract_wikipedia_info(html_content)  # Step 2: Extract information
            data_list = [query, definition, headings, subheadings, formulas, summary]  # Step 3: Store data in a list
            results.append(data_list)
        else:
            results.append([query, "Failed to retrieve data from Wikipedia."])
    
    return results

