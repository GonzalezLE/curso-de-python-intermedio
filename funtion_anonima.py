from functools import reduce

def main():    
    #function anonymous One
    palindroma = lambda string: string == string[::-1]
    
    palabra = input('Dame una palabra: ')
    if palindroma(palabra):
        print('Is')
    else:
        print('Not is')
        
    #use the filter with anonymous function
    #get the number impar
    my_list = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x : x%2 !=0,my_list))
    print('list the number impar',odd)
    
    
    #use the map with anonymous funtion
    #get the squared number
    my_list2 =[1,2,3,4,5]        
    list_with_liscompre=[i**2 for i in my_list2]    
    list_with_map = list(map(lambda x:x**2,my_list2))
    
    print(list_with_liscompre,list_with_map)
    
    #reduce 
    #for use reduce you can import to model reduce
    #example from functools import reduce
    my_list_reduce = [2,2,2,2,2]
    
    all_multiplied = reduce(lambda a,b: a*b,my_list_reduce)
    print(all_multiplied)
    

if __name__ == '__main__':
    main()
    