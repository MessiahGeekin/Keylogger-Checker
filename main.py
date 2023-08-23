import os
import json
import psutil
import time

def load_json_file():
    with open("keywords.json", "r") as file:
        suspicious_keywords = json.load(file)
    return suspicious_keywords


def custom_wordlist(path):
    keywords = []
    if os.path.exists(path):
        if path.endswith((".txt", ".json")):
            if path.endswith(".json"):
                with open(path, "r") as file:
                    keywords = json.load(file)
            elif path.endswith(".txt"):
                with open(path, "r") as file:
                    keywords = [line.strip() for line in file.readlines()]
            return keywords
        else:
            print("Unsupported wordlist format. Please provide a JSON or TXT file.")
    else:
        print("Wordlist file not found.")
    return keywords
    

def checking(keywords):
    c = 0
    potential_keyloggers = []
    total_processes = sum(1 for _ in psutil.process_iter())
    
    print("Analyzing processes:")
    for idx, process in enumerate(psutil.process_iter(attrs=['name', 'pid'])):
        process_name = process.info['name'].lower()
        for keyword in keywords:
            if keyword in process_name:
                c += 1
                potential_keyloggers.append(f"{process.info['name']} | {process.info['pid']}")
        
        progress = (idx + 1) / total_processes * 100
        print(f"Progress: {progress:.2f}%\r", end="", flush=True)
    print("\nAnalysis complete.")

    pk = "\n".join(potential_keyloggers)
    return pk, f"\n{c} potential keyloggers!"


def main():
    print("Keylogger Detection Script\n")
    
    wordlist_choice = input("Would you like to use the (w)ordlist or (c)ustom wordlist: ")
    if wordlist_choice == "w":
        keywords = load_json_file()
    elif wordlist_choice == "c":
        custom_path = input("Enter the path to the custom wordlist (JSON or TXT): ")
        keywords = custom_wordlist(custom_path)
    else:
        print("Invalid choice.")
        return
    
    if keywords:
        start_time = time.time()
        potential_keyloggers, count_message = checking(keywords)
        end_time = time.time()
        
        print(potential_keyloggers)
        print(count_message)
        
        save_to_file = input("Would you like to save potential keyloggers (y/n): ")
        if save_to_file.lower() in ("y", "yes"):
            file_name = input("Enter the file name (without extension): ")
            with open(f"{file_name}.txt", "w") as file:
                file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Potential Keyloggers:\n{potential_keyloggers}\n\n{count_message}")
        
        print(f"Script execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
