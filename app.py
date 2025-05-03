import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("Combined_Staff_updated.xlsx")

# Remove rows with missing barcodes or product names
df = df.dropna(subset=["Product", "Bar Code"])

st.title("Retail SKU Lookup")

# Input for search
search_barcode = st.text_input("Search by Barcode")
search_name = st.text_input("Search by Product Name")

# Filter the data
filtered_df = df
if search_barcode:
    filtered_df = filtered_df[df["Bar Code"].astype(str).str.contains(search_barcode)]
if search_name:
    filtered_df = filtered_df[df["Product"].str.contains(search_name, case=False)]

# Display results
if not filtered_df.empty:
    st.write(filtered_df[["Product", "Bar Code", "Cost Price", "Sell Price", "Parcel"]])
else:
    st.info("No results found.")