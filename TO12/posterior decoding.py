### VIRKER IKKE SOM DEN SKAL!

import math

class hmm:
    def __init__(self, init_probs, trans_probs, emission_probs):
        self.init_probs = init_probs
        self.trans_probs = trans_probs
        self.emission_probs = emission_probs
        
def translate_path_to_indices(path):
    return list(map(lambda x: int(x), path))

def translate_observations_to_indices(obs):
    mapping = {'a': 0, 'c': 1, 'g': 2, 't': 3}
    return [mapping[symbol.lower()] for symbol in obs]

def translate_indices_to_path(indices):
    return ''.join([str(i) for i in indices])

def log(x):
    if x == 0:
        return float('-inf')
    return math.log(x)

def make_table(m, n):
    """Make a table with `m` rows and `n` columns filled with zeros."""
    return [[0] * n for _ in range(m)]

def forward_algorithm(model, X, i):
    # model is the hmm model object
    # X is the observable sequence 
    # i is the index of the column/observable sequence being processed
    # Zj is the index of the row/hidden state being processed
    
    k_count = len(model.init_probs)
    a_i = [0]*k_count
    
    # Base case
    
    if i == 0:
        for Zj in range(k_count):
            ip = model.init_probs[Zj] # P(Z1)
            ep = model.emission_probs[Zj][X[i]] # P(X1|Z1)
            a_i[Zj] = log(ip) + log(ep)
        return a_i
    
    else:
        # k is the hidden state of the column before (i-1)
        a_i_minus1 = forward_algorithm(model, X, i-1)
        
        for Zj in range(k_count):
            prob_sum = 0
            
            for k in range(k_count):
                a_l_k = a_i_minus1[k]
                tp = model.trans_probs[k][Zj] # P(Zi|Zi-1) = P(Zi|Zk)
                ep = model.emission_probs[Zj][X[i]] # P(Xi|Zi)
                
                if a_l_k + log(tp) + log(ep) != float('-inf'):
                    prob_sum += a_l_k + log(tp) + log(ep)
            a_i[Zj] = prob_sum
        return a_i

def backward_algorithm(model, X, i):
    # model is the hmm model object
    # X is the observable sequence
    # i is the index of the column/observable sequence being processed
    # Zj is the index of the row/hidden state being processed
    
    k_count = len(model.init_probs)
    # Base case
    
    if i == len(X):
        b_i = [0]*k_count
        return b_i
    
    else:
        prob_sum = 0
        b_i = [0]*k_count
        
        # k is the hidden state of the column after (i+1)
        b_i_plus1 = backward_algorithm(model, X, i+1)
        
        for Zj in range(k_count):
            prob_sum = 0
            
            for k in range(k_count):
                b_l_k = b_i_plus1[k]
                tp = model.trans_probs[k][Zj] # P(Zi|Zi-1) = P(Zi|Zk)
                ep = model.emission_probs[Zj][X[i]] # P(Xi|Zi)
                
                if b_l_k + log(tp) + log(ep) != float('-inf'):
                    prob_sum += b_l_k + log(tp) + log(ep)
            b_i[Zj] = prob_sum
        return b_i


def posterior_decode(model, X, i):
    
    a_i_minus1 = forward_algorithm(model, X, i-1)
    b_i_plus1 = backward_algorithm(model, X, i+1)
    
    k_count = len(model.init_probs)
    
    c_i = [0]*k_count
    
    for Zj in range(k_count):
        forward_prob_sum = 0
        backward_prob_sum = 0
        
        for k in range(k_count):
            a_l_k = a_i_minus1[k]
            tp = model.trans_probs[k][Zj] # P(Zi|Zi-1) = P(Zi|Zk)
            ep = model.emission_probs[Zj][X[i]] # P(Xi|Zi)
            
            if a_l_k + log(tp) + log(ep) != float('-inf'):
                forward_prob_sum += a_l_k + log(tp) + log(ep)
    
            b_l_k = b_i_plus1[k]
            tp = model.trans_probs[k][Zj] # P(Zi|Zi-1) = P(Zi|Zk)
            ep = model.emission_probs[Zj][X[i]] # P(Xi|Zi)
            
            if b_l_k + log(tp) + log(ep) != float('-inf'):
                backward_prob_sum += b_l_k + log(tp) + log(ep)
            
            c_i[Zj] = forward_prob_sum + backward_prob_sum
            
    return c_i

def fill_posterior_decode_table(model, X):
    k_count = len(model.init_probs)
    n = len(x)
    
    table = make_table(k_count, n)
    
    for i in range(n):
        if i == 0:
            column = backward_algorithm(model, X, i)
            column_sum = sum(column)
        else:
            column = posterior_decode(model, X, i)
            column_sum = sum(column)
        
        for k in range(k_count):
            table[k][i] = column[k]/column_sum
    return table

def find_opt_path(table):
    
    k_count = len(table)
    n = len(table[0])
    path = []
    
    for i in range(n):
        max_k_prob = 0
        max_k = None
        for k in range(k_count):
            if max_k_prob < table[k][i]:
                max_k_prob = table[k][i]
                max_k = k
        path.append(max_k)
    
    return translate_indices_to_path(path)

init_probs_3_state = [0.10, 0.80, 0.10]

trans_probs_3_state = [
    [0.90, 0.10, 0.00],
    [0.05, 0.90, 0.05],
    [0.00, 0.10, 0.90],
]

emission_probs_3_state = [
    #   A     C     G     T
    [0.40, 0.15, 0.20, 0.25],
    [0.25, 0.25, 0.25, 0.25],
    [0.20, 0.40, 0.30, 0.10],
]

hmm_3_state = hmm(init_probs_3_state, trans_probs_3_state, emission_probs_3_state)

x_short = 'GTTTCCCAGTGTATATCGAGGGATACTACGTGCATAGTAACATCGGCCAA'
z_short = '33333333333321021021021021021021021021021021021021'

x = translate_observations_to_indices(x_short)
z = translate_path_to_indices(z_short)

# x_short = 'GTTT'
# x = translate_observations_to_indices(x_short)

print(find_opt_path(fill_posterior_decode_table(hmm_3_state, x)))