import re

pattern = re.compile(r'"([A-Z]+)\s+([^ ]+)\s+[^"]*"\s+(\d{3})\s+([0-9-]+)')

sum = 0

with open("log.txt", "r") as f:
    for linie in f:
        m = pattern.search(linie)

        method, path, status, size = m.group(1), m.group(2), m.group(3), m.group(4)

        if method == "GET" and path.startswith("/api/v1") and status == "200" and size != "-":
            sum = sum + int(size)

print(sum)
