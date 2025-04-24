import streamlit as st
import pandas as df
import plotly.express as px
import plotly.graph_objects as go

# Setting page configuration
st.set_page_config(page_title="Crop Production Forecast", layout="wide")

# Reading the dataset
data = df.read_csv("cleansed_crop_data.csv")

# Cleaning data: Ensure numeric columns are properly typed
numeric_cols = ["Area_Harvested_in_Hectares", "Yield_Value in kg/ha", "Production in Hectares"]
for col in numeric_cols:
    data[col] = df.to_numeric(data[col], errors="coerce")

# Title
st.title("Crop Production Forecast")

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Count of Area", len(data["Area"].unique()))
with col2:
    st.metric("Count of Yield_Value in kg/ha", f"{len(data['Yield_Value in kg/ha'].dropna()):,.0f}")
with col3:
    st.metric("Count of Item", len(data["Item"].unique()))
with col4:
    st.metric("Count of Item Code (CPC)", len(data["Item Code (CPC)"].unique()))

# Sidebar for filters
st.sidebar.header("Filters")

# Area filter
areas = sorted(data["Area"].unique())
selected_area = st.sidebar.selectbox("Area", areas, index=areas.index("Afghanistan"))

# Item filter
items = sorted(data["Item"].unique())
selected_item = st.sidebar.selectbox("Item", items, index=items.index("Almonds, in shell"))

# Year filter
years = sorted(data["Year"].unique().astype(int))
selected_year = st.sidebar.radio("Year", years, index=len(years)-1)

# Filter the data based on selections
filtered_data = data[
    (data["Area"] == selected_area) &
    (data["Item"] == selected_item)
]
year_filtered_data = data[data["Year"] == selected_year]

# Top row: Line chart and Pie chart
top_col1, top_col2 = st.columns([3, 1])

with top_col1:
    # Line Chart: Sum of Production in Hectares by Year
    production_by_year = filtered_data.groupby("Year")["Production in Hectares"].sum().reset_index()
    production_by_year["Production in Hectares"] = production_by_year["Production in Hectares"] / 1e9  # Convert to billions
    fig_line = px.line(
        production_by_year,
        x="Year",
        y="Production in Hectares",
        title="Sum of Production in Hectares by Year",
        labels={"Production in Hectares": "Sum of Production (B Hectares)"},
    )
    fig_line.update_traces(line=dict(color="#00A1FF"))
    fig_line.update_layout(
        yaxis_tickformat=".2f",
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
    )
    st.plotly_chart(fig_line, use_container_width=True)

with top_col2:
    # Pie Chart: Sum of Production in Hectares by Year
    pie_data = data[data["Area"] == selected_area].groupby("Year")["Production in Hectares"].sum().reset_index()
    total_production = pie_data["Production in Hectares"].sum()
    pie_data["Percentage"] = (pie_data["Production in Hectares"] / total_production) * 100
    fig_pie = px.pie(
        pie_data,
        names="Year",
        values="Production in Hectares",
        title="Sum of Production in Hectares by Year",
        labels={"Production in Hectares": "Production (Hectares)"},
        hover_data=["Percentage"],
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_pie.update_traces(
        textposition="inside",
        textinfo="label+value+percent",
        texttemplate="%{label}<br>%{value:.2f}B<br>(%{percent})",
        hovertemplate="%{label}<br>%{value:.2f}B<br>(%{percent})",
    )
    fig_pie.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
        showlegend=False,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Bottom row: Three histograms
bot_col1, bot_col2, bot_col3 = st.columns(3)

with bot_col1:
    # Histogram: Sum of Production in Hectares by Area
    prod_by_area = year_filtered_data.groupby("Area")["Production in Hectares"].sum().reset_index()
    prod_by_area["Production in Hectares"] = prod_by_area["Production in Hectares"] / 1e9  # Convert to billions
    prod_by_area = prod_by_area.sort_values("Production in Hectares", ascending=False)
    fig_hist1 = px.histogram(
        prod_by_area,
        x="Area",
        y="Production in Hectares",
        title="Sum of Production in Hectares by Area",
        labels={"Production in Hectares": "Sum of Production (B Hectares)"},
    )
    fig_hist1.update_traces(marker_color="#00A1FF")
    fig_hist1.update_layout(
        yaxis_tickformat=".2f",
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
        xaxis_tickangle=45,
        showlegend=False,
    )
    st.plotly_chart(fig_hist1, use_container_width=True)

with bot_col2:
    # Histogram: Sum of Area_Harvested_in_Hectares by Area
    area_by_area = year_filtered_data.groupby("Area")["Area_Harvested_in_Hectares"].sum().reset_index()
    area_by_area["Area_Harvested_in_Hectares"] = area_by_area["Area_Harvested_in_Hectares"] / 1e9  # Convert to billions
    area_by_area = area_by_area.sort_values("Area_Harvested_in_Hectares", ascending=False)
    fig_hist2 = px.histogram(
        area_by_area,
        x="Area",
        y="Area_Harvested_in_Hectares",
        title="Sum of Area_Harvested_in_Hectares by Area",
        labels={"Area_Harvested_in_Hectares": "Sum of Area Harvested (B Hectares)"},
    )
    fig_hist2.update_traces(marker_color="#00A1FF")
    fig_hist2.update_layout(
        yaxis_tickformat=".2f",
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
        xaxis_tickangle=45,
        showlegend=False,
    )
    st.plotly_chart(fig_hist2, use_container_width=True)

with bot_col3:
    # Histogram: Sum of Production in Hectares by Item
    prod_by_item = year_filtered_data.groupby("Item")["Production in Hectares"].sum().reset_index()
    prod_by_item["Production in Hectares"] = prod_by_item["Production in Hectares"] / 1e9  # Convert to billions
    prod_by_item = prod_by_item.sort_values("Production in Hectares", ascending=False)
    fig_hist3 = px.histogram(
        prod_by_item,
        x="Item",
        y="Production in Hectares",
        title="Sum of Production in Hectares by Item",
        labels={"Production in Hectares": "Sum of Production (B Hectares)"},
    )
    fig_hist3.update_traces(marker_color="#00A1FF")
    fig_hist3.update_layout(
        yaxis_tickformat=".2f",
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
        xaxis_tickangle=45,
        showlegend=False,
    )
    st.plotly_chart(fig_hist3, use_container_width=True)