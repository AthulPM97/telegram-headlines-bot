def json_to_response(headings_data):
    response_text = ""
    for page_num, headings in headings_data.items():
        if headings:
            response_text += f"\n=== Page {int(page_num) + 1} ===\n"
            for i, heading in enumerate(headings, start=1):
                response_text += f"{i}. {heading}\n"
        else:
            response_text += f"\n=== Page {int(page_num) + 1} === (No headings found)\n"
    return response_text
