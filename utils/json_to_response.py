def json_to_response(headings_data):
    chunks = []
    current_chunk = ""

    for page_num, headings in headings_data.items():
        # Generate the page section
        page_section = f"\n=== Page {int(page_num) + 1} ===\n"

        if headings:
            for i, heading in enumerate(headings, start=1):
                page_section += f"{i}. {heading}\n"
        else:
            page_section += "(No headings found)\n"

        # Check if adding this page would exceed the safe limit
        if len(current_chunk) + len(page_section) > 3900:  # 3900 for buffer
            if current_chunk:  # Don't add empty chunks
                chunks.append(current_chunk)
            current_chunk = page_section
        else:
            current_chunk += page_section

    # Add the final chunk if it has content
    if current_chunk:
        chunks.append(current_chunk)

    return chunks
