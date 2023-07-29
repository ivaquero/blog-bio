from typing import List

import requests
from bs4 import BeautifulSoup


# get codes as a list
def getCodes(url, start=1, end=2) -> List:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    # flag = '</code></pre></div>.?<pre><code class="python language-python">'

    all_codes: List = []

    for _ in range(start, end):
        selector = "div[class='collapseomatic_content']"
        codes_raw = soup.select(selector)
        codes_clean = [fence.get_text().strip() for fence in codes_raw]
        all_codes.append(codes_clean)
    return all_codes


# save codes to file
def saveCodes(the_codes, file_path, method):
    with open(file_path, method) as file:
        for codes in the_codes:
            for code_true in codes:
                file.write("#%%\n")
                file.write(code_true)
                file.write("\n\n")


if __name__ == "__main__":
    base_url = "https://www.machinelearningplus.com"
    url = f"{base_url}/top-50-matplotlib-visualizations-the-master-plots-python/"
    # run
    all_codes = getCodes(url)
    saveCodes(all_codes, "mpl50.py", "a+")
