import math

K_FACTOR = 32
"""
    get_estimated_outcome -> calculates what outcome should be
    update elo -> given how many points were earned and how many should be earner it returns gains    
"""

def get_estimated_outcome(elo_a,elo_b):
    Qa = math.pow(10, elo_a / 400)
    Qb = math.pow(10, elo_b / 400)

    estimated_a = Qa / (Qa + Qb)

    return estimated_a

"""
given outcome returns how much player should get new elo
"""
def get_elo_change(estimated_earn, actual_earn, k_factor=K_FACTOR):

    return k_factor * (actual_earn - estimated_earn)

def update_elo(elo,elo_change):
    # idk why it is here but sure
    return elo + elo_change
