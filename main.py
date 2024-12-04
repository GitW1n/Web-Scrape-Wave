import requests
from scraper.scraper import start_scraping, check_website_status
from scraper.parser import parse_page
from scraper.utils import display_objects, save_data

def main():
    while True:
        print(r"""                         ___                                                                                                                                    
                        (   )                                                                                                                                   
 ___  ___  ___   .--.    | |.-.         .--.      .--.     ___ .-.      .---.     .-..     .--.    ___ .-.         
(   )(   )(   ) /    \   | /   \      /  _  \    /    \   (   )   \    / .-, \   /    \   /    \  (   )   \       
 | |  | |  | | |  .-. ;  |  .-. |    . .' `. ;  |  .-. ;   | ' .-. ;  (__) ; |  ' .-,  ; |  .-. ;  | ' .-. ;     
 | |  | |  | | |  | | |  | |  | |    | '   | |  |  |(___)  |  / (___)   .'`  |  | |  . | |  | | |  |  / (___)    
 | |  | |  | | |  |/  |  | |  | |    _\_`.(___) |  |       | |         / .'| |  | |  | | |  |/  |  | |            
 | |  | |  | | |  ' _.'  | |  | |   (   ). '.   |  | ___   | |        | /  | |  | |  | | |  ' _.'  | |            
 | |  ; '  | | |  .'.-.  | '  | |    | |  `\ |  |  '(   )  | |        ; |  ; |  | |  ' | |  .'.-.  | |           
 ' `-'   `-' ' '  `-' /  ' `-' ;     ; '._,' '  '  `-' |   | |        ' `-'  |  | `-'  ' '  `-' /  | |             
  '.__.'.__.'   `.__.'    `.__.       '.___.'    `.__,'   (___)       `.__.'_.  | \__.'   `.__.'  (___)             
                                                                                | |                                                                             
                                                                               (___)                                                                            
""")

        print("""
=== Main Menu ===
1. Links for parsing
2. Exit
""")
        
        choice = input("Your choice(1/2):  ")

        if choice == '1':
            urls = input("Enter links (separated by commas):  ").split(',')
            urls = [url.strip() for url in urls]
            for url in urls:
                status = check_website_status(url)
                print(f"Connection status for {url}: {status}")
            
            object_type = input("Object type for parsing (eg. Header): ")

            for url in urls:
                try:
                    page_content = requests.get(url).text
                    print(f"\nParsing content from: {url}")
                    
                    results = parse_page(page_content, object_type)
                    
                    if results:
                        print(f"Extracted {object_type}:")
                        for item in results:
                            print(f"- {item}")
                    else:
                        print(f"No {object_type} found on this page.")
                except Exception as e:
                    print(f"Error processing {url}: {e}")

        elif choice == '2':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
