name = "Client"
task = "Build automation"
print(name, task)

tasks = ["data cleaning", "API call", "report generation"]
for t in tasks:
    print(t)

def summarize(text):
    return text[:40]
print(summarize("Artificial Intelligence Systems are transforming businesses"))

with open("sample.txt") as f:
    data = f.read()
print(data)

import json
data = {
    "name": "client",
    "project": "AI assistant"
}
print(json.dumps(data, indent=2))