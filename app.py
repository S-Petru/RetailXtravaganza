import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("RetailX App")
    
    # Add your app code here
    
    # Example test dashboard
    st.subheader("Test Dashboard")
    
    # Generate random data
    data = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])
    
    # Display a line chart
    st.line_chart(data)
    
    # Display a bar chart
    st.bar_chart(data)
    
    # Display a scatter plot
    st.scatter_chart(data)
    
    # Display a table
    st.dataframe(data)
    
if __name__ == "__main__":
    main()
    