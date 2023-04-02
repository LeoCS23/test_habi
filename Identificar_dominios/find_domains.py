import re

def organize_list(lis):

    string = list(set(lis))
    string.sort()
    return ';'.join(string)


if __name__ == '__main__':

    domains = []

    with open('./documento.html', 'r') as f:
        lines_read = int(f.readline().strip())

        for i in range(lines_read):
            line = f.readline().strip()
            links = re.findall(r'(https?:\/\/(?:www\.)?[a-zA-Z0-9]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*)', line)
            for link in links:
                domains.append(re.search(r'https?://(?:www\.)?([a-zA-Z0-9]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*)', link).group(1))

    new_string = organize_list(domains)

    print(new_string)
    