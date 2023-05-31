import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

def monte_carlo_option_pricing(asset_price, strike_price, volatility, risk_free_rate, time_to_expiration, num_simulations):
    total_payoff = 0
    option_payoffs = []

    # Perform Monte Carlo simulation num_simulations times
    for _ in range(num_simulations):
        asset_price_path = generate_random_price_path(asset_price, volatility, risk_free_rate, time_to_expiration)
        option_payoff = calculate_payoff(asset_price_path, strike_price, is_call_option)
        discounted_payoff = discount_payoff(option_payoff, risk_free_rate, time_to_expiration)
        
        total_payoff += discounted_payoff
        option_payoffs.append(discounted_payoff)

    option_price = total_payoff/num_simulations
    return option_price, option_payoffs


def generate_random_price_path(asset_price, volatility, risk_free_rate, time_to_expiration):
    time_intervals = 100
    dt = time_to_expiration/time_intervals
    price_path = [asset_price]
    
    # Generate random price path using geometric Brownian motion
    for _ in range(time_intervals):
        # Generate a random number from a standard normal distribution
        random_value = np.random.normal(0, 1) 
        asset_price = price_path[-1]
        
        # Calculate the drift and diffusion components
        drift = (risk_free_rate - (volatility**2)/2) * dt
        diffusion = volatility * math.sqrt(dt) * random_value
        
        # Calculate the next asset price using the geometric Brownian motion equation
        next_price = asset_price * math.exp(drift + diffusion)
        
        price_path.append(next_price)
    
    return price_path


def calculate_payoff(asset_price_path, strike_price, is_call_option):
    final_asset_price = asset_price_path[-1]
    
    # Calculate the option payoff based on the type of option
    if is_call_option:
        option_payoff = max(final_asset_price - strike_price, 0)
    else:
        option_payoff = max(strike_price - final_asset_price, 0)
    
    return option_payoff

def black_scholes(asset_price, strike_price, volatility, risk_free_rate, time_to_expiration, is_call_option):
    d1 = (math.log(asset_price / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * time_to_expiration) / (volatility * math.sqrt(time_to_expiration))
    d2 = d1 - volatility * math.sqrt(time_to_expiration)
    
    if is_call_option:
        option_price = asset_price * norm.cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_expiration) * norm.cdf(d2)
    else:
        option_price = strike_price * math.exp(-risk_free_rate * time_to_expiration) * norm.cdf(-d2) - asset_price * norm.cdf(-d1)
    
    return option_price

def discount_payoff(payoff, risk_free_rate, time_to_expiration):
    discount_factor = math.exp(-risk_free_rate * time_to_expiration)
    discounted_payoff = payoff * discount_factor
    return discounted_payoff


def plot_option_payoffs(payoffs):
    plt.hist(payoffs, bins=30, edgecolor='black')
    plt.xlabel('Option Payoff')
    plt.ylabel('Frequency')
    plt.title('Distribution of Option Payoffs')
    plt.show()


if __name__ == "__main__":
    asset_price = 100  # Initial price of the underlying asset
    strike_price = 110  # Strike price of the option
    volatility = 0.1  # Volatility of the underlying asset's returns
    risk_free_rate = 0  # Risk-free interest rate
    time_to_expiration = 1  # Time to expiration of the option in years
    num_simulations = 10000  # Number of Monte Carlo simulations to perform
    is_call_option = True  # Set to True for call option, False for put option

    est_option_price, payoffs = monte_carlo_option_pricing(asset_price, strike_price, volatility, risk_free_rate, time_to_expiration, num_simulations)
    print("Estimated option price:", est_option_price)
    black_scholes = black_scholes(asset_price, strike_price, volatility, risk_free_rate, time_to_expiration, is_call_option)
    print("Black-Scholes option price", black_scholes)
    print("Difference:", est_option_price - black_scholes)
    plot_option_payoffs(payoffs)
