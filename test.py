import streamlit as st
#import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

st.write("Streamlit")

range_type = st.selectbox(
    label="Select Date Range Type:",
    options=["Last", "Next", "Range"],
    key="range_type"
)

if range_type == "Last":
    placeholder = st.empty()
    with placeholder.container():
        st.write("Last")
        #3 columns
        col1, col2, col3 = st.columns(3)
        lastx = col1.number_input(label="Number of Days", min_value=1, max_value=100, value=1, key="last_days")
        last_type = col2.selectbox(label="Select Date Range Type:", options=["Days", "Weeks", "Months"], key="last_days_type")
        if last_type == "Days":
            include_label = "Include Today"
        elif last_type == "Weeks":
            include_label = "Include This Week"
        elif last_type == "Months":
            include_label = "Include This Month"
        
        include = col3.checkbox(label=include_label, value=True, key="include")

        if last_type == "Days":
            st.write("Days")
            if include:
                begin_date = dt.date.today() - dt.timedelta(days=lastx)
                end_date = dt.date.today()
            else:
                begin_date = dt.date.today() - dt.timedelta(days=lastx+1)
                end_date = dt.date.today() - dt.timedelta(days=1)
        elif last_type == "Weeks":
            st.write("Weeks")
            if include:
                begin_date = dt.date.today() - dt.timedelta(weeks=lastx)
                end_date = dt.date.today()
            else:
                #set end_date to last day of previous week
                end_date = dt.date.today() - dt.timedelta(days=dt.date.today().weekday()+1)
                begin_date = end_date - dt.timedelta(weeks=lastx) + dt.timedelta(days=1)
        elif last_type == "Months":
            st.write("Months")
            if include:
                begin_date = dt.date.today() - relativedelta(months=lastx)
                end_date = dt.date.today()
            else:
                #set end_date to last day of previous month
                end_date = dt.date.today().replace(day=1) - dt.timedelta(days=1)
                begin_date = end_date - relativedelta(months=lastx) + dt.timedelta(days=1)
elif range_type == "Next":
    placeholder = st.empty()
    with placeholder.container():
        st.write("Next")
        #3 columns
        col1, col2, col3 = st.columns(3)
        nextx = col1.number_input(label="Number of Days", min_value=1, max_value=100, value=1, key="next_days")
        next_type = col2.selectbox(label="Select Date Range Type:", options=["Days", "Weeks", "Months"], key="next_days_type")
        if next_type == "Days":
            include_label = "Include Today"
        elif next_type == "Weeks":
            include_label = "Include This Week"
        elif next_type == "Months":
            include_label = "Include This Month"

        include = col3.checkbox(label=include_label, value=True, key="include")

        if next_type == "Days":
            st.write("Days")
            if include:
                begin_date = dt.date.today()
                end_date = dt.date.today() + dt.timedelta(days=nextx)
            else:
                begin_date = dt.date.today() + dt.timedelta(days=1)
                end_date = dt.date.today() + dt.timedelta(days=nextx+1)
        elif next_type == "Weeks":
            st.write("Weeks")
            if include:
                begin_date = dt.date.today()
                end_date = dt.date.today() + dt.timedelta(weeks=nextx) - dt.timedelta(days=1)
            else:
                #set begin_date to first day of next week
                begin_date = dt.date.today() + dt.timedelta(days=7-dt.date.today().weekday())
                end_date = begin_date + dt.timedelta(weeks=nextx) - dt.timedelta(days=1)
        elif next_type == "Months":
            st.write("Months")
            if include:
                begin_date = dt.date.today()
                end_date = dt.date.today() + relativedelta(months=nextx) - dt.timedelta(days=1)
            else:
                #set begin_date to first day of next month
                begin_date = dt.date.today().replace(day=1) + relativedelta(months=1)
                end_date = begin_date + relativedelta(months=nextx) - dt.timedelta(days=1)
elif range_type == "Range":
    placeholder = st.empty()
    with placeholder.container():
        st.write("Range")
        col1, col2 = st.columns(2)
        begin_date = col1.date_input(label="Begin Date", value=dt.date.today() - dt.timedelta(days=1), key="begin_date")
        end_date = col2.date_input(label="End Date", value=dt.date.today(), key="end_date")
        if begin_date > end_date:
            st.error("Begin Date must be before End Date")

begin_date = dt.datetime.combine(begin_date, dt.datetime.min.time())
end_date = dt.datetime.combine(end_date, dt.datetime.max.time())
st.write(begin_date)
st.write(end_date)