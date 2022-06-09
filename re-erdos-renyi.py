import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

#For non sparse graph; faster algorithm exists for sparse(small p) graphs
G = nx.gnp_random_graph(200, 0.5, seed=247, directed=False)
#nx.draw(G, with_labels=True)

beta = 4
x=np.zeros(81)
y=np.zeros(81)
i=0

while (beta >= -4.1):

    L = nx.laplacian_matrix(G)
    #The above generates a scipy sparse array and not a matrix(Better for comutational purposes?);

    #Converting the sparse array to matrix 
    L = L.todense()

    pho_tmp = expm(-10**(beta)*L)
    Z = pho_tmp.trace()
    pho = expm(-10**(beta)*L)/Z
    Lp = np.matmul(L,pho)
    Tr = Lp.trace()

    S = np.log2(Z) + (10**(beta)/(np.log(2)) * Tr)
    print(S/(np.log2(200)))
   
    x[i] = -beta
    y[i] = S/(np.log2(200))
    
    i=i+1
    beta = beta - 0.1

print(x)
print(y)
plt.plot(x,y)
plt.show()
