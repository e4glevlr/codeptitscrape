# CodePTIT Scrape Tool

## 1. Description
CodePTIT Scrape Tool is a tool that helps to collect all exercise data from the website [https://code.ptit.edu.vn/](https://code.ptit.edu.vn/). The tool uses Scrapy to automatically gather data.

## 2. Requirements
- Python
- Scrapy

## 3. Usage Instructions

### Step 1: Prepare Logged-in Cookies
The tool requires logged-in cookies from the website [code.ptit.edu.vn](https://code.ptit.edu.vn/) to access the exercise data. You can use browser tools to obtain the logged-in cookies.

### Step 2: Set Up the Environment
Make sure you have Python and Scrapy installed. If not, you can install Scrapy with the following command:

```bash
pip install scrapy
```

### Step 3: Run Scrapy
To run the tool, use the following command in the terminal:
```bash
scrapy crawl ptitspider
```
This command will start the data collection process from the website.

### Step 4: Export Data to a File
To export the collected data to a CSV file, use the command:
```bash
scrapy crawl ptitspider -O dsa.csv
```
You can change the export file name and format (CSV or JSON) as desired. For example, to export to a JSON file:
```bash
scrapy crawl ptitspider -O dsa.json
```

## 4. Configuration and Customization

### Configuring Cookies
The tool requires cookies logged in to [code.ptit.edu.vn](https://code.ptit.edu.vn/). To configure cookies, add the cookies to Scrapy's settings, which can be edited in the `settings.py` file or managed using the `COOKIES_ENABLED` and `COOKIES_DEBUG` parameters.

### Customizing the Spider
You can customize the data collection process by editing the spider code `ptitspider.py`. To change the URL, request methods, or other data processing tasks, check the `start_requests()`, `parse()`, and `pipeline` functions to fit the goals of your project.

## 5. Notes for Usage
- **Cookies**: Ensure the cookies you use are still valid; otherwise, update the cookies to avoid access errors.


