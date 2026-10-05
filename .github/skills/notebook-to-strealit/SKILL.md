---
name: notebook-to-streamlit
description: Turn the Rosa's Pizza notebook into a Streamlit decision app.
---

# Notebook to Streamlit

Read the Jupyter Notebook in this project and reuse its calculation logic.

## Calculation rules

- Import ZONES, TIME_BLOCKS, COSTS, PROMISE, and delivery_times from starter.
- Do not recreate or modify starter.py.
- Reuse late_lost and best_promise from the notebook.
- Cost per late order = refund + churn_orders × margin.
- Net profit = order count × margin − late order count × cost per late order.
- An order is late when its delivery time exceeds the tested promise.
- Use seed=1 and test promises in 1-minute steps.
- Initialize the highest profit with float("-inf").

## App requirements

- Use dropdown menus to select a zone and time block.
- Allow users to set the minimum and upper limit of candidate promises.
- Exclude the upper limit, matching the notebook's range function.
- Allow users to adjust margin, churn_orders, and refund.
- Use COSTS for the initial cost values.
- After clicking a button, show the recommended promise and net profit.
- Reject an empty search range with a clear message.
- Describe the result as the best promise within the tested range.

## Project files

- app.py: Streamlit interface.
- logic.py: Reusable calculation functions.
- requirements.txt: Include streamlit, numpy, and
  git+https://github.com/zhouy185/rosa-starter.git.