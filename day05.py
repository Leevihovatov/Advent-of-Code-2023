def main():
    with open("input05.txt", "r") as f:
        data = f.read().split('\n\n')
    
    seeds = data[0].split()[1:]
    del(data[0])

    silver = 0
    gold = 0

    min_location = 99999999999999999999999999999999999999999999 # :D
    for seed in seeds:
        new_source = seed
        for map in data:
            source = new_source
            map = map.splitlines()
            del(map[0])
            found = False
            for line in map:
                l = line.split()
                if int(source) >= int(l[1]) and int(source) <= int(l[1])+int(l[2])-1:
                    source_index = int(source)-int(l[1])
                    new_source = int(l[0])+source_index
                    found = True
            if not found:
                new_source = int(source)
        if new_source < min_location:
            min_location = new_source

    silver = min_location

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()