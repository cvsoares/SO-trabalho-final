mat = [['r','u','n','k','f','f','x','s','c','s','l','v','q','w','v','t','v','f','o','l','w','y','m','m','x','p','r','o','c','e','s','s','o','s','l','k','q','o','i','f','h','e','u','r','j','z','q','b','d','l','p','y','b','n','t','w','i','b','l','v'],['x','j','h','j','g','u','v','y','k','d','f','r','j','z','l','t','b','b','w','e','o','l','d','p','y','i','y','m','i','z','z','d','y','i','n','j','q','j','f','o','r','k','v','l','u','u','y','p','v','a','n','c','o','z','h','g','z','f','u','k'],['h','t','p','h','d','c','t','t','o','y','j','i','k','e','t','g','y','s','v','w','u','j','a','k','k','p','h','s','l','o','m','v','x','h','l','f','m','p','y','f','d','y','q','n','i','u','h','p','v','b','m','t','x','v','t','j','h','a','c','t'],['q','q','o','o','a','t','b','v','m','t','t','s','w','t','k','k','d','f','t','s','c','w','h','v','v','e','e','o','e','m','q','i','f','g','z','t','u','z','x','p','l','q','k','f','o','f','q','y','j','x','t','d','z','r','k','u','m','p','k','t'],['b','c','b','g','k','h','a','b','f','b','y','w','n','o','j','s','d','o','k','d','x','h','z','b','g','q','n','c','f','c','o','y','f','q','b','l','b','c','p','i','d','n','g','s','e','r','l','h','g','x','m','f','f','l','i','l','e','y','q','l'],['a','e','j','i','v','r','k','v','y','o','k','g','u','y','o','m','s','i','n','a','i','s','e','g','z','n','o','x','z','v','c','n','e','p','t','c','f','e','e','k','n','m','h','z','i','f','q','u','n','k','u','p','y','y','j','y','l','x','x','n'],['t','b','a','z','q','e','t','d','y','x','h','k','m','w','r','o','n','g','s','d','a','n','p','v','q','o','t','c','o','h','b','l','u','w','m','u','v','c','p','a','c','o','k','m','a','g','f','p','o','f','t','i','u','k','j','l','y','f','p','o'],['m','q','z','i','n','a','l','c','k','q','t','l','s','h','v','v','h','j','d','o','y','r','u','t','h','o','g','r','b','e','y','q','t','m','j','u','u','w','g','y','i','y','r','v','s','a','s','z','j','v','q','p','o','k','f','w','a','l','p','c'],['r','p','u','m','b','d','d','h','v','b','p','v','m','i','n','m','h','h','a','a','h','z','v','z','i','m','j','p','i','l','a','z','p','s','o','k','e','p','p','n','m','t','c','h','f','r','v','m','z','j','o','e','k','m','h','x','s','y','q','k'],['i','b','k','h','t','s','e','v','d','l','k','u','u','y','y','n','d','f','e','u','a','j','t','l','x','b','v','j','i','p','h','a','z','p','e','m','y','x','s','t','c','d','f','w','e','d','m','h','k','g','b','m','p','v','z','e','p','w','u','y'],['h','m','i','j','n','z','n','z','y','k','u','q','t','o','x','z','l','b','r','z','i','r','h','m','d','x','h','d','m','f','z','m','o','l','u','y','b','u','l','a','u','y','w','n','m','u','m','z','x','t','y','i','k','i','u','t','p','f','b','s'],['t','i','u','h','x','h','e','v','i','y','r','g','l','u','g','h','h','v','h','w','u','b','p','v','j','b','d','d','q','k','g','l','f','o','f','m','n','m','q','i','v','q','r','g','k','x','p','u','u','t','q','p','u','h','m','u','d','i','r','i'],['y','d','o','j','i','e','q','w','s','a','d','p','c','a','h','t','i','s','t','x','o','n','q','e','e','m','n','s','r','v','j','z','v','m','p','h','w','u','x','t','o','c','i','q','c','p','k','m','j','f','m','z','s','e','d','m','z','r','s','r'],['i','n','d','k','l','r','z','s','o','t','p','h','h','u','r','a','y','i','k','l','u','r','x','t','j','d','z','k','u','r','e','f','h','h','p','s','y','o','k','m','k','b','v','t','v','o','t','u','z','f','h','t','w','e','o','i','h','p','s','e'],['h','w','l','q','d','a','a','i','e','q','u','s','a','v','o','u','t','e','n','p','d','v','w','y','r','c','n','z','j','e','s','p','n','q','a','d','w','c','n','a','t','h','s','t','f','i','p','a','n','f','p','q','a','l','r','r','n','g','r','y'],['t','h','r','x','f','d','s','k','l','q','y','b','q','d','x','v','r','z','o','a','s','j','f','a','b','f','p','g','w','i','i','h','z','b','u','f','u','v','r','f','l','p','j','b','t','g','y','k','i','m','m','a','y','s','c','z','z','s','f','w']]


def busca_multi(x):

    tam = len(x) - 1
    comp = 0
    cont = 0
    busca = 0
    palavra = x
    palavra_inversa = x[::-1]

    while (busca <= 1):
        for i in range(16): #percorrer as linhas da matriz
            for j in range(60): #percorrer as colunas da matriz
                try:
                    #HORIZONTAL
                    if (mat[i][j] == x[0] and mat[i][j+tam] == x[tam]): #buscar a posição da palavra inicial e final 
                        posj = j    
                    
                        while (cont <= tam):
                    
                            if (mat[i][posj] == x[cont]):
                                comp = comp + 1
                                cont = cont + 1
                                posj = posj + 1
                    
                            else:
                                comp = 0
                                cont = 0
                                posj = 0
                                break
                    
                    if (int(comp) == len(x)):
                        comp = 0
                        cont = 0
                        posj = 0
                        
                        if (x==palavra):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i],[j],'da matriz')  
                            print('Sentido: esquerda p/ direita\n') 
                        if (x==palavra_inversa):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i],[j+tam],'da matriz')  
                            print('Sentido: direita p/ esquerda\n') 

                    if (mat[i][j] == x[0] and mat[i][j-tam] == x[tam]): #buscar a posição da palavra inicial e final 
                        posj = j    
                    
                        while (cont >= 1):
                    
                            if (mat[i][posj] == x[cont]):
                                x = x [::-1]
                                comp = comp + 1
                                cont = cont + 1
                                posj = posj - 1
                    
                            else:
                                comp = 0
                                cont = 0
                                posj = 0
                                break
                       
                    if (int(comp) == len(x)):
                        comp = 0
                        cont = 0
                        posj = 0
                        if (x == palavra):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i],[j],'da matriz')  
                            print('Sentido: direita p/ esquerda\n')
                        if (x == palavra_inversa):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i],[j-tam],'da matriz')  
                            print('Sentido: esquerda p/ direita\n') 
    

                    #VERTICAL
                    if (mat[i][j] == x[0] and mat[i+tam][j] == x[tam]): #buscar a posição da letra inicial e final 
                        posi = i    
                    
                        while (cont <= tam):
                    
                            if (mat[posi][j] == x[cont]):
                                comp = comp + 1
                                cont = cont + 1
                                posi = posi + 1
                    
                            else:
                                comp = 0
                                cont = 0
                                posi = 0
                                break
                    
                    if (int(comp) == len(x)):
                        comp = 0
                        cont = 0
                        posi = 0
                        if (x == palavra):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i],[j],'da matriz')  
                            print('Sentido: cima p/ baixo\n')
                        if (x == palavra_inversa):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i+tam],[j],'da matriz')  
                            print('Sentido: baixo p/ cima\n') 


                    if (mat[i][j] == x[0] and mat[i-tam][j] == x[tam]): #buscar a posição da palavra inicial e final 
                        posi = i    
                    
                        while (cont >= 1):
                    
                            if (mat[posi][j] == x[cont]):
                                
                                comp = comp + 1
                                cont = cont + 1
                                posi = posi - 1

                            else:
                                comp = 0
                                cont = 0
                                posi = 0
                                break
                        
                    if (int(comp) == len(x)):
                        comp = 0
                        cont = 0
                        posj = 0
                        if(x == palavra):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i],[j],'da matriz')  
                            print('Sentido: baixo p/ cima\n')
                        if (x==palavra_inversa):
                            print('Palavra encontrada:',palavra)     
                            print('Posição',[i-tam],[j],'da matriz')  
                            print('Sentido: cima p/ baixo\n') 

                except:
                    continue
        x = palavra_inversa
        busca = busca + 1        
            
busca_multi('threads')
busca_multi('arquivos')
busca_multi('pipe')
busca_multi('sinais')
busca_multi('processos')
busca_multi('mutex')
busca_multi('fork')