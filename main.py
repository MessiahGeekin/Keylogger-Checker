import json
import psutil

def load_json_file():
    with open("keywords.json", "r") as file:
        suspicious_keywords = json.load(file)
    return suspicious_keywords

def checking(keywords):
    c = 0
    potential_keyloggers = []
    for process in psutil.process_iter(attrs=['name', 'pid']):
        process_name = process.info['name'].lower()
        for keyword in keywords:
            if keyword in process_name:
                c += 1
                potential_keyloggers.append(f"{process.info['name']} | {process.info['pid']}")
    pk = "\n".join(potential_keyloggers)
    return pk, f"{c} potential keyloggers!"

def main():
    keywords = load_json_file()
    if keywords:
        potential_keyloggers, count_message = checking(keywords)
        print(potential_keyloggers)
        print(count_message)

if __name__ == "__main__":
    main()
