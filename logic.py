"""Reusable calculation logic from the Rosa's Pizza notebook (Part 2)."""

import numpy as np
from starter import delivery_times

SEED = 1  # fixed seed so every tested promise sees the same simulated orders


def late_lost(costs):  # get to know how much lost when a late delivery happened
    return costs["refund"] + costs["churn_orders"] * costs["margin"]  # Total cost = refund + lost future orders × profit per order


def best_promise(zones, time_blocks, promise_time_range, costs):  # Start below any possible profit, including negative profits
    biggest_profit = float("-inf")
    best_time = promise_time_range[0]
    for p in promise_time_range:  # Use a fixed seed to simulate delivery times
        all_times = delivery_times(zones, time_blocks, p, SEED)
        order_numbers = len(all_times)

        all_income = order_numbers * costs["margin"]  # Calculate profit before deducting the cost of late order
        all_lost = np.sum(all_times > p) * late_lost(costs)  # Total late cost = late orders × cost per late order
        net_profit = all_income - all_lost

        if net_profit > biggest_profit:  # Save the promise with the highest net profit so far
            biggest_profit = net_profit
            best_time = p

    return best_time, float(biggest_profit)  # Return the best tested promise and its net profit
