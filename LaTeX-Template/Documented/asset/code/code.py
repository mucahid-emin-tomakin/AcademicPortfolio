import os

def print_directory(path):
    HLINE = chr(9472)
    VERT = chr(9474)
    LAST = chr(9492)
    NODE = chr(9500)
    
    with os.scandir(path) as entries:
        entries = sorted(entries, key=lambda f: f.name.lower())
        total = len(entries)
        
        for i, entry in enumerate(entries):
            if i == total - 1:
                symbol = LAST + HLINE + HLINE
            else:
                symbol = NODE + HLINE + HLINE
            print(symbol, entry.name)

if __name__ == "__main__":
    print_directory(".")