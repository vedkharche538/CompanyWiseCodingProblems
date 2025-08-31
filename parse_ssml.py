import re

def parse_ssml(ssml_str):
    # Rule: First tag must be <speak>
    tag_pattern = re.compile(r'<\s*(\w+)([^>]*)>', re.DOTALL)
    tags = list(tag_pattern.finditer(ssml_str))
    if not tags or tags[0].group(1) != "speak":
        raise ValueError("First tag must be <speak>")
    
    # Accepts any tag and attribute
    result = []
    self_closing_pattern = re.compile(r'<\s*(\w+)([^>]*)/\s*>')
    for match in tag_pattern.finditer(ssml_str):
        tag_name = match.group(1)
        attrs = match.group(2)
        start, end = match.span()
        # Rule: Validate self-closing tags
        is_self_closing = bool(self_closing_pattern.match(ssml_str[start:end]))
        result.append({
            "tag": tag_name,
            "attrs": attrs,
            "self_closing": is_self_closing,
            "start": start,
            "end": end
        })
    return result

# Example usage
ssml = '''<speak><say-as interpret-as="digits">123</say-as/><break time="1s"/><voice name="Emma">Hello!</voice></speak>'''
tags = parse_ssml(ssml)
for tag in tags:
    print(tag)
