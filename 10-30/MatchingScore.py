import re


def solution(word, pages):
    url_pattern = re.compile(r'<meta property="og:url" content="(\S+)"/>')
    anchor_pattern = re.compile(r'<a href="(\S+)">')
    sites = {}

    for idx, page in enumerate(pages):
        url = url_pattern.search(page).group(1)
        links = []
        default_score = 0

        for element in anchor_pattern.findall(page):
            links.append(element)

        words = re.split(r'[^A-Za-z_]+', page)
        for element in words:
            if word.upper() == element.upper():
                default_score += 1

        sites[url] = {"links": links, "default_score": default_score, "link_score": 0, "idx": idx}

    for key in sites.keys():
        for link in sites[key]["links"]:
            if link in sites and len(sites[link]["links"]) != 0:
                sites[link]["link_score"] += sites[key]["default_score"] / len(sites[key]["links"])

    for key in sites.keys():
        sites[key]["matching_score"] = sites[key]["link_score"] + sites[key]["default_score"]
    result = sorted(sites.items(), key=lambda x: (-x[1]["matching_score"], x[1]["idx"]))
    return result[0][1]["idx"]


print(solution('blind', [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
               ))
