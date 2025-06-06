from bs4 import BeautifulSoup


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content


def extract_info_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    company_info = {}

    try:
        location_elements = soup.select(
            'span.component--field-formatter.field-type-identifier-multi a.accent.ng-star-inserted')
        location_parts = [elem.get_text(strip=True) for elem in
                          location_elements[:3]]
        location = ", ".join(location_parts)
        company_info['Location'] = location
    except AttributeError:
        company_info['Location'] = 'N/A'

    try:
        employees = soup.select_one('a[href*="/search/people/field/organizations/num_employees_enum/"]').get_text(
            strip=True)
        company_info['Employees'] = employees
    except AttributeError:
        company_info['Employees'] = 'N/A'

    try:
        website_element = soup.select_one('a[title="www.openai.com"]')
        if website_element:
            website = website_element['href']
        else:
            website = 'N/A'
        company_info['Website'] = website
    except (AttributeError, TypeError):
        company_info['Website'] = 'N/A'

    try:
        funding = soup.select_one('a[href*="/search/funding_rounds/field/organizations/last_funding_type/"]').get_text(
            strip=True)
        company_info['Last Funding Type'] = funding
    except AttributeError:
        company_info['Last Funding Type'] = 'N/A'

    try:
        status = soup.select_one('span[title="Private"]').get_text(strip=True)
        company_info['Status'] = status
    except AttributeError:
        company_info['Status'] = 'N/A'

    try:
        rank = soup.select_one(
            'a[href*="/search/organization.companies/field/organizations/rank_org_company/"]').get_text(strip=True)
        company_info['Rank'] = rank
    except AttributeError:
        company_info['Rank'] = 'N/A'

    try:
        founders_elements = soup.select(
            'span.component--field-formatter.field-type-identifier-multi a.accent.ng-star-inserted[title]')
        founders_list = [founder.get_text(strip=True) for founder in founders_elements]
        company_info['Founders'] = ", ".join(founders_list)
    except AttributeError:
        company_info['Founders'] = 'N/A'

    return company_info


def main():
    file_path = 'C:\\Users\\dobos\\PycharmProjects\\WebMiningProject\\exam\\openai.html'
    html_content = read_html_file(file_path)

    company_info = extract_info_from_html(html_content)


    for key, value in company_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
