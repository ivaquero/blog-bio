import itertools
import pandas as pd


def assign_matrix(*cols):
    '''
    Assigns a 0-1 matrix for each cols
    '''
    list_0_1 = [*product([0, 1], repeat=len(cols))]
    assign_df = pd.DataFrame(list_0_1, columns=cols)
    
    return assign_df 
