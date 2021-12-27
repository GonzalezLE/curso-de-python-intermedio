def main():
    """
    list = [ ]
    for i in range(1,101):
        if i%3 != 0:            
            list.append(i**2)
    """
    
    list = [i**2 for i in range(1,101) if i%3!=0]
    
    """Crear list comprehension de todos los multiplos de 4
    que a su vez igual son multiplos de 6 y de 9 
    
    1 a 100000
    """
    
    list = [i for i in range(1,100000) if i%4==0 and i%6==0 and i%9==0 ]
    
    list = [i for i in range(1,100000) if i%36==0 and len(str(i)) <= 5]
    
    print(list)
        



if __name__ == '__main__':
    main()
    