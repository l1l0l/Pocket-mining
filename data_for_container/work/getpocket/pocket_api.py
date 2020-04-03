def do_post_request(url, data):
    request = Request(url=url, data=data)
    try:
        http_response = urlopen(request)
    except HTTPError as e:
        print(e.headers.as_string())
    if http_response:
        text_response = http_response.read()
        return text_response