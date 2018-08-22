def dict2table(dict, label):
    print("{:<15} {:<10}".format(*label))
    
    for k, v in dict.items():
        print("{:<15} {:<10}".format(k, v))