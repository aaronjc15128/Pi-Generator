def main():
    from os import system
    import time
    
    system("cls")
    print("PI GENERATOR\n------------\n")
    accuracy = int(input("Accuracy: "))
    printing = input("Printing: ")
    
    stime = time.time()

    evens, dms, Npi, Dpi = [], [], 3, 1

    i = 2
    while i < accuracy:
        evens.append(i)
        i += 2

    for n in evens:
        dms.append((n, n+1, n+2))

    evens.insert(0, 0)

    for n in evens:    
        try:
            ta = dms[n]
            tb = dms[n+1]
        except IndexError:
            break
        
        da = ta[0] * ta[1] * ta[2]
        db = tb[0] * tb[1] * tb[2]
       
        Npi = (Npi*da)+(Dpi*4)
        Dpi = Dpi*da

        Npi = (Npi*db)-(Dpi*4)
        Dpi = Dpi*db

    etime = time.time()
    if printing.lower() == "true":
        print(f"\n{Npi}\n\n{Dpi}\n\n{Npi/Dpi}\n\n{len(str(Npi))}\n\n{len(str(Dpi))}\n\n{etime-stime}")

    eetime = time.time()
    print(f"\n{eetime-stime}")
    

if __name__ == "__main__":
    main()