import pandas as pd
import requests
from bs4 import BeautifulSoup

# --- Fetch and parse the webpage ---
url = "https://footyindustry.com/html/AFL_Members.htm"
response = requests.get(url)
response.encoding = 'utf-8'

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

# Extract all rows
all_rows = table.find_all('tr')

# Extract year headers from row 2 (index 2, after Title and empty rows)
header_row = all_rows[2]
headers = []
header_cells = header_row.find_all(['th', 'td'])
for cell in header_cells[1:]:  # Skip first cell which is "Year"
    text = cell.get_text(strip=True)
    try:
        headers.append(int(text))
    except ValueError:
        pass

# Extract data rows
data_rows = []
clubs_to_keep = [
    'Adelaide', 'Brisbane', 'Carlton', 'Collingwood', 'Essendon', 
    'Fremantle', 'Geelong', 'Gold Coast', 'G.Western Sydney', 'Hawthorn',
    'Melbourne', 'North Melbourne', 'Port Adelaide', 'Richmond', 
    'St Kilda', 'Sydney', 'West Coast', 'Western Bulldogs'
]

# Process data rows (starting from row 3 onwards)
for tr in all_rows[3:]:
    cells = tr.find_all(['td', 'th'])
    if cells:
        club = cells[0].get_text(strip=True)
        
        # Only keep valid clubs
        if club not in clubs_to_keep:
            continue
            
        row_data = {'Club': club}
        for i, cell in enumerate(cells[1:]):
            text = cell.get_text(strip=True)
            if i < len(headers):
                year = headers[i]
                try:
                    value = int(text.replace(',', '')) if text else None
                except ValueError:
                    value = None
                row_data[year] = value
        
        data_rows.append(row_data)

# Create dataframe
df = pd.DataFrame(data_rows)
df.set_index('Club', inplace=True)

# Sort columns by year
df = df.reindex(sorted(df.columns, key=lambda x: int(x) if isinstance(x, int) else 0), axis=1)

# --- Save ---
df.to_csv("data/raw/membership_afl_website.csv")
print("Data imported and saved to data/raw/membership_afl_website.csv")
print(f"\nShape: {df.shape}")
print(f"\nFirst few rows:")
print(df.iloc[:5, :5])
print(f"\nYears covered: {df.columns[0]} to {df.columns[-1]}")
