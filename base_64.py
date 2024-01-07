import base64

def url_to_base64_without_padding(url):
    url_bytes = url.encode('utf-8')
    base64_bytes = base64.b64encode(url_bytes)
    # Decode to a string and remove the padding
    base64_without_padding = base64_bytes.decode('utf-8').rstrip('=')
    return base64_without_padding

# Example usage
url = 'http://05yzb-upqs.us'
encoded_url = url_to_base64_without_padding(url)
print(f"Encoded URL: {encoded_url}")