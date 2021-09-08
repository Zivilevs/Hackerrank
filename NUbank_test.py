
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY pontuacao
#  2. INTEGER tamanho_do_time
#  3. INTEGER k

import time
import random

def formacaoDeTimeSliced(pontuacao, tamanho_do_time, k):
    # Write your code here
    selecao = []

    while len(selecao) < tamanho_do_time:
        while k <= len(pontuacao):
            if (len(selecao) < tamanho_do_time):

                preselecaoA = pontuacao[:k]
                preselecaoB = pontuacao[-k:]

                maxiA = max(preselecaoA)
                maxiA_index = pontuacao.index(maxiA)
                maxiB = max(preselecaoB)
                maxiB_index = pontuacao.index(maxiB,-k)

                if maxiA > maxiB:
                    selecao.append(maxiA)
                    pontuacao.pop(maxiA_index)
                else:
                    selecao.append(maxiB)
                    pontuacao.pop(maxiB_index)

            if len(selecao) == tamanho_do_time:
                return sum(selecao)
                break
        
        
        if k > len(pontuacao):
            if len(pontuacao) != 0:
                while (len(selecao) < tamanho_do_time):
                    maxi = max(pontuacao)
                    selecao.append(maxi)
                    maxi_index = pontuacao.index(maxi)
                    pontuacao.pop(maxi_index)
                return sum(selecao)
            else:
                return sum(pontuacao)
    return sum(selecao)


def formacaoDeTimeRecursive(pontuacao, tamanho_do_time, k):

    if len(pontuacao) == tamanho_do_time:
        return sum(pontuacao)
    else:
        def recursiveFormacaoTime(pontuacao, k, selecao=[]):

            if len(pontuacao) == 1:
                maxi = 0
            else:
                preselecaoA = pontuacao[:k]
                preselecaoB = pontuacao[-k:]
                maxiA = max(preselecaoA)
                maxiA_index = pontuacao.index(maxiA)
                maxiB = max(preselecaoB)
                maxiB_index = pontuacao.index(maxiB,-k)

                if maxiA > maxiB:
                    selecao.append(maxiA)
                    pontuacao.pop(maxiA_index)
                else:
                    selecao.append(maxiB)
                    pontuacao.pop(maxiB_index)
                recursiveFormacaoTime(pontuacao, k, selecao)
            return selecao
    return sum((recursiveFormacaoTime(pontuacao, k))[:tamanho_do_time])


def formacaoDeTimeSubmitted(pontuacao, tamanho_do_time, k):
    selecao = []
    while len(selecao) < tamanho_do_time:
        while k <= len(pontuacao):
            if (len(selecao) < tamanho_do_time):
                preselecaoA = []
                preselecaoB = []
                i = 0
                while i < k:
                    preselecaoA.append(pontuacao[i])
                    preselecaoB.append(pontuacao[len(pontuacao) - 1 - i])
                    i += 1
                maxiA = max(preselecaoA)
                maxiA_index = pontuacao.index(maxiA)
                maxiB = max(preselecaoB)
                maxiB_index = pontuacao.index(maxiB,-k)

                if maxiA > maxiB:
                    selecao.append(maxiA)
                    pontuacao.pop(maxiA_index)
                else:
                    selecao.append(maxiB)
                    pontuacao.pop(maxiB_index)
            if len(selecao) == tamanho_do_time:
                return sum(selecao)
                break
        
        
        if k >= len(pontuacao):
            if len(pontuacao) != 0:
                while (len(selecao) < tamanho_do_time):
                    maxi = max(pontuacao)
                    selecao.append(maxi)
                    maxi_index = pontuacao.index(maxi)
                    pontuacao.pop(maxi_index)
                return sum(selecao)
            else:
                return sum(pontuacao)
    return sum(selecao)

def formacaoDeTimeOptimized(pontuacao, tamanho_do_time, k):

    selecao = []

    if k < len(pontuacao):
        j = k
        i = 0
    
        for member in range(tamanho_do_time):
            maior = 0
        
            for num in range(k):
                if pontuacao[i+num] >= pontuacao[-j + num]:
                    if pontuacao[i + num] >= maior:
                        maior = pontuacao[i + num]
                        inx_maior = i + num
                else:
                    if pontuacao[-j+num] > maior:
                        maior = pontuacao[-j+num]
                        inx_maior = (-j+num)

            selecao.append(maior)

            if inx_maior >= 0:
                temp = pontuacao[i]
                pontuacao[i] = maior
                pontuacao[inx_maior] = temp
                i += 1
            else:
                temp = pontuacao[-j+k-1]
                pontuacao[-j+k-1] = maior
                pontuacao[inx_maior] = temp
                j += 1
        return sum(selecao)        
    
    else:
    
        if len(pontuacao) != 0:
            pontuacao.sort()
            return sum(pontuacao[-tamanho_do_time])
        else:
            return 0

# Results. Sum and time efficiency.

formacoes = [formacaoDeTimeSubmitted, formacaoDeTimeSliced, formacaoDeTimeRecursive, formacaoDeTimeOptimized]

def timeTest(tamanho_list, tamanho_team, k, funcs=formacoes):
    randomlist = []
    time_list = []
    sums = []
    names = []

    for i in range(0, tamanho_list):
        n = random.randint(1, 1000)
        randomlist.append(n)

    print("Time eficiency compared with submitted function results.\n")
    for f in funcs:
        rand_list = randomlist[:]
        
        try:
            start_time = time.time()
            suma = f(rand_list, tamanho_team, k)
            end_time = time.time()
        except RecursionError:
            print(f.__name__, "\nMaximum recursion depth exceeded in comparison\n")
            continue
        except :
            print("Some bug :)")
        
        elapsed_time = end_time - start_time
        time_list.append(elapsed_time)
        sums.append(suma)
        names.append(f.__name__,)
            
    base_submitted = time_list[0]
    i = 0
    for t , n in zip(time_list, names):
        compare = ((base_submitted/t)*100)
        print("{}: {:.1f}%".format(n, compare))
        print("Sum:", sums[i])
        print("Time:", time_list[i], "\n")
        i += 1


        

# With small list and small team the difference is not interesting.
timeTest(2000, 5, 3)

# with large list and bigger team the difference is important!

timeTest(1000000, 30, 3)



    