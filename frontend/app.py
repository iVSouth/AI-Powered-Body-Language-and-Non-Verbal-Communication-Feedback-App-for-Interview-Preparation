import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def main():
    st.title('Visualize Emotions Data')
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.write("### Dataset Overview")
        st.write(df.head())
        
        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram", "Box Plot"]
        )
        
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        if chart_type == "Bar Chart":
            x_col = st.sidebar.selectbox("X-axis", numeric_columns)
            y_col = st.sidebar.selectbox("Y-axis", numeric_columns)
            
            fig = px.bar(df, x=x_col, y=y_col, 
                         title=f"Bar Chart: {x_col} vs {y_col}")
            st.plotly_chart(fig)
        
        elif chart_type == "Line Chart":
            x_col = st.sidebar.selectbox("X-axis", numeric_columns)
            y_col = st.sidebar.selectbox("Y-axis", numeric_columns)
            
            fig = px.line(df, x=x_col, y=y_col, 
                          title=f"Line Chart: {x_col} vs {y_col}")
            st.plotly_chart(fig)
        
        elif chart_type == "Scatter Plot":
            x_col = st.sidebar.selectbox("X-axis", numeric_columns)
            y_col = st.sidebar.selectbox("Y-axis", numeric_columns)
            
            fig = px.scatter(df, x=x_col, y=y_col, 
                             title=f"Scatter Plot: {x_col} vs {y_col}")
            st.plotly_chart(fig)
        
        elif chart_type == "Histogram":
            col_to_plot = st.sidebar.selectbox("Column", numeric_columns)
            
            fig = px.histogram(df, x=col_to_plot, 
                               title=f"Histogram of {col_to_plot}")
            st.plotly_chart(fig)
        
        elif chart_type == "Box Plot":
            x_col = st.sidebar.selectbox("X-axis (Categorical)", 
                                         df.select_dtypes(include=['object']).columns.tolist())
            y_col = st.sidebar.selectbox("Y-axis (Numeric)", numeric_columns)
            
            fig = px.box(df, x=x_col, y=y_col, 
                         title=f"Box Plot: {x_col} vs {y_col}")
            st.plotly_chart(fig)
        
        st.write("### Dataset Statistics")
        st.write(df.describe())

if __name__ == "__main__":
    main()