#Read a CSV file in Streamlit
import streamlit as st
import pandas as pd

def main():
    st.title("CSV File Reader")

    # File upload widget
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display the data
        st.write("### Displaying Data from CSV file")
        st.write(df)

        # You can perform additional operations on the DataFrame if needed
        # For example, plot a chart
        st.write("### Data Visualization")
        st.bar_chart(df)

if __name__ == "__main__":
    main()
