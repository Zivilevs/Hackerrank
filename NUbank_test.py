
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY pontuacao
#  2. INTEGER tamanho_do_time
#  3. INTEGER k

import time
import random

def formacaoDeTime(pontuacao, tamanho_do_time, k):
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



def formacaoDeTime2(pontuacao, tamanho_do_time, k):

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


def formacaoDeTimeNU(pontuacao, tamanho_do_time, k):
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
                    i += 1
                return sum(selecao)
            else:
                return sum(pontuacao)
    return sum(selecao)




randomlist = []
for i in range(0, 500):
    n = random.randint(1, 1000)
    randomlist.append(n)

randomlist2 = randomlist[:]
randomlistNU = randomlist[:]

print("Recursive")
start_time = time.time()
print("Sum:", formacaoDeTime2(randomlist, 4, 6))
end_time = time.time()
print("Time:",end_time - start_time, "\n")

print("Sliced")
start_time = time.time()
print("Sum:", formacaoDeTime(randomlist2, 4, 6))
end_time = time.time()
print("Time:", end_time - start_time, "\n")

print("Submitted")
start_time = time.time()
print("Sum:", formacaoDeTimeNU(randomlistNU, 4, 6))
end_time = time.time()
print("Time:", end_time - start_time)



