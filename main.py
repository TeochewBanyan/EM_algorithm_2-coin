import requests
import numpy as np
from scipy import stats

def get_coins(nums):
    coins = []
    url = "https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta"
    for i in range(nums):
        r = requests.get(url)
        content = r.json()
        coin = ((content['body'].lstrip('[')).rstrip(']')).split(', ')
        coin = [int(x) for x in coin]
        coins.append(coin)
    return coins

def EM(observations, theta_a, theta_b):
    """
    params:
    counts[0-3]: ah, at, bh, bt
    """
    counts = np.zeros(4)
    for observation in observations:
        num_heads = observation.sum()
        num_tails = len(observation)-num_heads
        # e-step
        #estimate hidden variable z
        z_a = stats.binom.pmf(num_heads, len(observation), theta_a)
        z_b = stats.binom.pmf(num_heads, len(observation), theta_b)
    
        z_a /= (z_a+z_b)
        z_b /= (z_a+z_b)
        #compute the expectation
        counts[0]+=z_a*num_heads
        counts[1]+=z_a*num_tails
        counts[2]+=z_b*num_heads
        counts[3]+=z_b*num_tails
    
    # m-step
    new_theta_a = counts[0]/(counts[0]+counts[1])
    new_theta_b = counts[2]/(counts[2]+counts[3])
    return new_theta_a, new_theta_b

def estimate_theta():
    nums = 30
    coins = np.array(get_coins(nums))
    #random initialization
    theta_a = np.random.rand(1)
    theta_b = np.random.rand(1)
    threshold = 1e-9
    max_iterations = 1000
    for iteration in range(max_iterations):
        new_theta_a, new_theta_b = EM(coins, theta_a, theta_b)
        if abs(new_theta_a-theta_a)<threshold and abs(new_theta_b-theta_b)<threshold:
            print(f'iterations:{iteration}')
            break
        else:
            theta_a = new_theta_a
            theta_b = new_theta_b
        
    print(f'theta_a:{new_theta_a}, theta_b:{new_theta_b}')
    return new_theta_a, new_theta_b
    
# estimate theta for multiple times, and use the average as the answer    
estimate_iterations = 10
theta_list_a = []
theta_list_b = []
for iteration in range(estimate_iterations):
    theta_a, theta_b = estimate_theta()
    theta_list_a.append(max(theta_a, theta_b))
    theta_list_b.append(min(theta_a, theta_b))
theta_list_a = np.array(theta_list_a)
theta_list_b = np.array(theta_list_b)
estimate_theta_a = theta_list_a.mean()
estimate_theta_b = theta_list_b.mean()
print(f"theta_a: {estimate_theta_a}, theta_b: {estimate_theta_b}")