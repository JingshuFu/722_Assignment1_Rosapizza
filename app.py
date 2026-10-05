"""Streamlit interface for choosing Rosa's Pizza delivery promise."""

import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE

from logic import best_promise, late_lost

st.title("Rosa's Pizza: Best Delivery Promise")
st.caption(
    f"Current promise: {PROMISE} minutes. Candidate promises are tested in "
    "1-minute steps with seed=1."
)

zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

st.subheader("Candidate promises (minutes)")
col1, col2 = st.columns(2)
min_promise = col1.number_input("Minimum promise", min_value=1, value=13, step=1)
upper_limit = col2.number_input(
    "Upper limit (excluded)", min_value=1, value=65, step=1,
    help="Like Python's range(), the upper limit itself is not tested.",
)

st.subheader("Costs")
col1, col2, col3 = st.columns(3)
margin = col1.number_input("Margin per order ($)", value=float(COSTS["margin"]), step=0.5)
churn_orders = col2.number_input("Churn orders per late order", value=float(COSTS["churn_orders"]), step=0.1)
refund = col3.number_input("Refund per late order ($)", value=float(COSTS["refund"]), step=0.5)

costs = {"margin": margin, "churn_orders": churn_orders, "refund": refund}
st.write(f"Cost per late order: ${late_lost(costs):.2f}")

if st.button("Find best promise"):
    promises = range(int(min_promise), int(upper_limit))
    if len(promises) == 0:
        st.error(
            "The search range is empty. Set the upper limit higher than the "
            "minimum promise."
        )
    else:
        best_time, best_profit = best_promise(zone, time_block, promises, costs)
        st.success(
            f"Best promise within the tested range ({promises[0]}–{promises[-1]} "
            f"minutes) for {zone} | {time_block}:"
        )
        col1, col2 = st.columns(2)
        col1.metric("Recommended promise", f"{best_time} minutes")
        col2.metric("Net profit", f"${best_profit:,.2f}")
        if best_time == promises[0] or best_time == promises[-1]:
            st.warning("The best promise is at the edge of the search range. Try widening it.")
