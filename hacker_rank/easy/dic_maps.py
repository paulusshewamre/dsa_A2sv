def display_contacts(n):
    contact = dict()
    for i in range(n):
        name, phone = input().split()
        contact[name] = phone
    
    try:
        while True:
            name = input().strip()
            if len(name) > 0:
                if name in contact:
                    print(f"{name}={contact[name]}")
                else:
                    print("Not found")
    except EOFError:
        pass


if __name__ == '__main__':
    n = int(input())
    display_contacts(n)
    
        
     
