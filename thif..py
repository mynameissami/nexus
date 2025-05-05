import re

def main():
    """Main Function"""
    print(validate(input("ipv4 Address: ").strip()))
    
def validate(ip):
    """Validator"""
    # Correcting the regular expression pattern to match valid IP addresses
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        a, b, c, d = map(int, ip.split("."))  # Splitting using dot and converting to integers
        if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
            return "Valid"
        return "Invalid"
    return "Please enter in format of #.#.#.#, where 0<=#<=255"

if __name__ == "__main__":
    main()
