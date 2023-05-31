# Basic-Monte-Carlo-Options
>Description:
Uses Monte Carlo simulations and geometric Brownian motion to simulate estimated option price and payoffs given asset price, strike price, expiration date, and volatility

# Options
Options are like financial contracts that give the holder the right, but not the obligation, to buy or sell an  asset at a predetermined price (strike price) during a specified period. There are two types of options: call options and put options. Call options give the holder the right to buy the asset, while put options give the holder the right to sell the asset. You can buy or sell an option, but the price of the option must be determined. The price of an option depends on a multitude of factors, but overall boils down to the risk of the option and potential upside. I determine the price of an option with this information using two methodologies, equation and simulation, to see the difference in their results.

## Black-Scholes
The Black-Scholes model is a mathematical model used to calculate the theoretical price of options. It is defined as the following:
![Black Scholes](https://www.wallstreetmojo.com/wp-content/uploads/2022/12/Black-Scholes-Model.jpg)

## Monte Carlo Simulation
The idea behind Monte Carlo simulation is to repeatedly use random sampling to come to an approximate answer via the law of large numbers. In this scenario, to estimate option prices we use the current asset price, strike price, volatility, and time to expiration to simulate the asset's price paths based on the Geometric Brownian Motion mathematical model. Once we get the path the asset's price takes we can calculate the option's payoff for each simulated path. These payoffs are then discounted back to the present value using the risk-free rate. We can then average the discounted payoffs across all simulations to obtain an estimate of the option price.

# Resources
https://www.youtube.com/watch?v=MiybniIIvx0&ab_channel=SkyViewTrading

https://www.youtube.com/watch?v=VJgHkAqohbU&ab_channel=ThePlainBagel
