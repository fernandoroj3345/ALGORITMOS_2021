def Usarlafuerza(arr,x,indice):
        if arr[indice] == x:
            print(x)
            print('se sacaron ',indice,'objetos')
        else:
            print(arr[indice])
            Usarlafuerza(arr,x,indice+1)
mochila = ['enano','ryzen9','piedra','sable de luz','papel']
Usarlafuerza(mochila,'sable de luz',0)