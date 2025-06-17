# Save Aline Scraper

A Python-based web scraper that collects and aggregates content from various technical interview preparation resources.

## Features

- Scrapes content from multiple sources:
  - Interviewing.io Blog
  - Company-specific Interview Guides
  - Interview Preparation Guides
  - Nil Mamano's DSA Blogs
  - Nil's Book

## Prerequisites

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/save-aline-scapper.git
cd save-aline-scapper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python main.py
```

The script will:
1. Scrape content from all configured sources
2. Combine the results
3. Save the output to `output.json`

## Output

The script generates an `output.json` file containing:
- Team ID
- Aggregated items from all sourcess

## Project Structure

```
save-aline-scapper/
├── main.py              # Main script
├── scrapers/           # Scraper modules
│   ├── interviewing_io_blog.py
│   ├── interviewing_io_guides.py
│   ├── interviewing_io_interview_guides.py
│   ├── nilmamano_dsa.py
│   └── nil_book.py
├── requirements.txt    # Project dependencies
└── README.md          # This file
```





