#Isabell Mora

#Lab Section- 11

#11-12-24

#Sources, help given to/received from

with open('prompt.txt', 'r') as infile, open('out.txt', 'w') as outfile:
    for line in infile:
        line = line.strip()

        if not line:
            continue
        
        pairs = line.split("\t")
        result = ""

        for pair in pairs:
            pair = pair.strip()
            if ":" not in pair:
                print(f"Skipping pair: {pair}")
                continue 
            
            key, value = pair.split(":")
            try:
                value = int(value)
            except ValueError:
                print(f"Skipping pair: {pair}")
                continue

            if key == "w":
                result += " " * value 
            elif key == "*":
                result += "*" * value 
        outfile.write(result + "\n")

                
                    