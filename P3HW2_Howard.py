# Hadrien Howard
# 10/6/2026
# Use if/else statements to determine overtime pay

# python -m streamlit run P3HW2_HowardHadrien.py

import streamlit as st

st.title("PayCheck Calculator")

# Get name
name = st.text_input("Enter employee name: ")

# Get hours worked
hours_worked = st.number_input("Enter hours worked: ")

# Get pay rate
pay_rate = st.number_input("Enter hourly pay rate: $")


if hours_worked > 40:
    print("You had some overtime")
    overtime_hours = hours_worked - 40
    reg_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = reg_hours * pay_rate
    total_pay = regular_pay + overtime_pay
    
else: # worked 40 hours or less
    print("You did not have any overtime")
    overtime_hours = 0
    reg_hours = hours_worked
    overtime_pay = 0
    regular_pay = reg_hours * pay_rate
    total_pay = regular_pay + overtime_pay
    
# Display results
st.write(f"hours worked: {hours_worked:.1f}")
st.write(f"pay rate: ${pay_rate:.2f}")
st.write(f"overtime hours: {overtime_hours:.1f}")
st.write(f"regular pay: ${regular_pay:.1f}")
st.write(f"overtime pay: ${overtime_pay:.2f}")
st.write(f"-----------------------------------------------------")
st.write(f"Total pay: ${total_pay:.2f}")
