def main():
    my_list = [1,'Hello',True,4.5]
    my_dick = {'firsname':'luis','lastname':'gonzalez'}
    
    super_list = [
        {'firsname':'Facundo','lastname':'García'},
        {'firsname':'Miguel','lastname':'Torres'},
        {'firsname':'Pepe','lastname':'Rodelo'},
        {'firsname':'susana','lastname':'Martinez'},
        {'firsname':'josé','lastname':'García'}    
    ]
    
    super_dict = {
        'natural_nums':[1,2,3,4,5],
        'integers_nums':[-1,-2,0,1,2],
        'floatings':[1.1,4.5,6.43]
    }
    
    
    for key,value in super_dict.items():
        print(key, '-',value)


if __name__ == '__main__':
    main()
    