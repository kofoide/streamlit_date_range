# Streamlit Date Range Selector

The basic date range selection capability is lacking in features.

This project allows for creating a date range in 3 ways:

- Last X number of days/weeks/months
- Next X number of days/weeks/months
- 2 date picker for real range

The checkbox "Include" means:

- For "Last" type, today will be the end date of the range
- For "Next" type, today will be the begin date of the range

If you uncheck "Include" means:

- For "Last" type:
-- Days means yesterday will be the end date
-- Weeks, finds the last of previous week as end date
-- Months, finds the last day of the previous month as end date
-- Begin date is computed from the end date
- For "Next" type:
-- Days means tomorrow with the begin date
-- Weeks, finds the first day of the next week as begin date
-- Months, finds the first day of the next month as begin date
-- End date is computed from the begin date
