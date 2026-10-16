
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Amazon Customer Feedback Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL THEME
# =========================================================
st.markdown("""
<style>
    .stApp {
        background-color: #F5F7FB;
        color: #172B4D;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
    }

    h1 {
        color: #142D4E;
        font-weight: 750;
        letter-spacing: -0.5px;
    }

    h2, h3 {
        color: #1C3D63;
        font-weight: 650;
    }

    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E1E8F0;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 3px 12px rgba(20, 45, 78, 0.05);
    }

    div[data-testid="stMetricLabel"] {
        color: #5C6F85;
        font-size: 14px;
    }

    div[data-testid="stMetricValue"] {
        color: #142D4E;
        font-weight: 700;
    }

    div[data-testid="stSidebar"] {
        background-color: #EAF0F8;
    }

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    hr {
        border-color: #DCE5F0;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# CATEGORY DATA
# Counts and ratings from MySQL validation.
# =========================================================
ratings = pd.DataFrame({
    "Category": [
        "Books", "Grocery", "Ebook", "Beauty", "Electronics"
    ],
    "Reviews": [
        100100, 180018, 100100, 127483, 153672
    ],
    "Rated Reviews": [
        100084, 180001, 100082, 127483, 153672
    ],
    "Average Rating": [
        4.34, 4.17, 4.11, 3.96, 3.59
    ]
})

# Sentiment percentages from the latest SQL result.
# Grocery has 17 records with missing sentiment.
sentiment = pd.DataFrame({
    "Category": [
        "Books", "Grocery", "Ebook", "Beauty", "Electronics"
    ],
    "Positive": [83.56, 77.63, 76.98, 71.23, 60.41],
    "Neutral": [10.00, 7.77, 13.79, 8.07, 10.07],
    "Negative": [6.45, 14.59, 9.23, 20.71, 29.52]
})

negative_counts = pd.DataFrame({
    "Category": [
        "Books", "Grocery", "Ebook", "Beauty", "Electronics"
    ],
    "Negative Reviews": [
        6455, 26269, 9239, 26397, 45362
    ]
})

# Keyword mention counts from earlier SQL analysis.
# These are not unique complaint counts.
issue_data = pd.DataFrame({
    "Category": ["Beauty", "Books", "Ebook", "Electronics"],
    "Quality Mentions": [1368, 218, 121, 5964],
    "Product Condition Mentions": [1308, 59, 88, 4787],
    "Authenticity Mentions": [355, 42, 47, 543],
    "Price Issue Mentions": [1329, 332, 356, 6339]
})

# Verified overall database metrics.
TOTAL_REVIEWS = 661373
UNIQUE_PRODUCTS = 255229
UNIQUE_CUSTOMERS = 423006
OVERALL_AVERAGE_RATING = 4.01

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================
st.sidebar.title("Amazon Feedback")
st.sidebar.caption("Customer Intelligence Platform")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "Sentiment Intelligence",
        "Product Issues",
        "Business Insights"
    ],
    key="dashboard_page"
)

st.sidebar.divider()

selected_categories = st.sidebar.multiselect(
    "Filter by category",
    options=ratings["Category"].tolist(),
    default=ratings["Category"].tolist(),
    key="category_filter"
)

st.sidebar.caption(
    "Dataset: 661,373 customer reviews across 5 categories"
)

if not selected_categories:
    st.warning("Select at least one category in the sidebar.")
    st.stop()

filtered_ratings = ratings[
    ratings["Category"].isin(selected_categories)
].copy()

filtered_sentiment = sentiment[
    sentiment["Category"].isin(selected_categories)
].copy()

filtered_negative = negative_counts[
    negative_counts["Category"].isin(selected_categories)
].copy()

filtered_issues = issue_data[
    issue_data["Category"].isin(selected_categories)
].copy()

# =========================================================
# DYNAMIC SELECTED-CATEGORY METRICS
# =========================================================
selected_reviews = int(filtered_ratings["Reviews"].sum())
selected_rated_reviews = int(filtered_ratings["Rated Reviews"].sum())

# Weighted average based on category averages and rated review counts.
# Category averages are rounded in the supplied SQL results.
if selected_rated_reviews > 0:
    selected_average_rating = (
        filtered_ratings["Average Rating"]
        * filtered_ratings["Rated Reviews"]
    ).sum() / selected_rated_reviews
else:
    selected_average_rating = 0

# =========================================================
# SHARED HEADER
# =========================================================
st.title("Amazon Customer Feedback Intelligence")
st.caption(
    "Customer Review Analytics | Business Intelligence Dashboard"
)

# =========================================================
# PAGE 1: EXECUTIVE OVERVIEW
# =========================================================
if page == "Executive Overview":

    st.subheader("Executive Overview")
    st.write(
        "Explore customer feedback and category performance using "
        "the category filter in the sidebar."
    )

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Selected Reviews", f"{selected_reviews:,}")
    k2.metric(
        "Selected Average Rating",
        f"{selected_average_rating:.2f} / 5"
    )
    k3.metric("Unique Products", f"{UNIQUE_PRODUCTS:,}")
    k4.metric("Unique Customers", f"{UNIQUE_CUSTOMERS:,}")

    st.caption(
        "Review count and average rating respond to the category filter. "
        "Unique products and customers show overall-dataset totals."
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.markdown("### Average Rating by Category")

        rating_plot = filtered_ratings.sort_values(
            "Average Rating", ascending=True
        )

        fig_rating = px.bar(
            rating_plot,
            x="Average Rating",
            y="Category",
            orientation="h",
            text="Average Rating",
            color="Average Rating",
            color_continuous_scale=["#C8DDF3", "#174A7E"],
            range_x=[0, 5],
            hover_data=["Reviews"]
        )

        fig_rating.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_rating.update_layout(
            coloraxis_showscale=False,
            xaxis_title="Average Rating (out of 5)",
            yaxis_title="",
            margin=dict(l=5, r=35, t=20, b=10)
        )

        st.plotly_chart(
            fig_rating,
            width="stretch",
            key="overview_rating"
        )

    with right:
        st.markdown("### Review Volume by Category")

        volume_plot = filtered_ratings.sort_values(
            "Reviews", ascending=False
        )

        fig_volume = px.bar(
            volume_plot,
            x="Category",
            y="Reviews",
            text="Reviews",
            color="Reviews",
            color_continuous_scale=["#B9D8F5", "#174A7E"]
        )

        fig_volume.update_traces(
            texttemplate="%{text:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_volume.update_layout(
            coloraxis_showscale=False,
            xaxis_title="Category",
            yaxis_title="Total Reviews",
            margin=dict(l=5, r=15, t=20, b=10)
        )

        st.plotly_chart(
            fig_volume,
            width="stretch",
            key="overview_volume"
        )

    st.divider()
    st.markdown("### Category Summary")

    summary = filtered_ratings.merge(
        filtered_sentiment,
        on="Category",
        how="left"
    )

    st.dataframe(
        summary,
        hide_index=True,
        width="stretch"
    )

# =========================================================
# PAGE 2: SENTIMENT INTELLIGENCE
# =========================================================
elif page == "Sentiment Intelligence":

    st.subheader("Sentiment Intelligence")
    st.write(
        "Compare positive, neutral, and negative sentiment "
        "across the selected product categories."
    )

    st.info(
        "Percentages use total reviews as the denominator. "
        "Grocery has 17 missing sentiment labels, so its percentages "
        "sum to slightly less than 100%."
    )

    sentiment_long = filtered_sentiment.melt(
        id_vars="Category",
        var_name="Sentiment",
        value_name="Percentage"
    )

    sentiment_colors = {
        "Positive": "#1976D2",
        "Neutral": "#90CAF9",
        "Negative": "#E53935"
    }

    fig_sentiment = px.bar(
        sentiment_long,
        x="Category",
        y="Percentage",
        color="Sentiment",
        barmode="stack",
        text="Percentage",
        color_discrete_map=sentiment_colors,
        category_orders={
            "Sentiment": ["Positive", "Neutral", "Negative"]
        }
    )

    fig_sentiment.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="inside",
        insidetextanchor="middle",
        textfont_size=11
    )

    fig_sentiment.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Percentage (%)",
        yaxis=dict(range=[0, 100]),
        legend_title="Sentiment",
        uniformtext_minsize=9,
        uniformtext_mode="hide",
        margin=dict(l=10, r=10, t=30, b=10)
    )

    st.plotly_chart(
        fig_sentiment,
        width="stretch",
        key="sentiment_distribution"
    )

    st.markdown("### Negative Review Comparison")

    fig_negative = px.bar(
        filtered_negative.sort_values(
            "Negative Reviews", ascending=False
        ),
        x="Category",
        y="Negative Reviews",
        text="Negative Reviews",
        color="Negative Reviews",
        color_continuous_scale=["#F7B8B8", "#C62828"]
    )

    fig_negative.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside",
        cliponaxis=False
    )

    fig_negative.update_layout(
        coloraxis_showscale=False,
        xaxis_title="Product Category",
        yaxis_title="Negative Review Count",
        margin=dict(l=10, r=20, t=25, b=10)
    )

    st.plotly_chart(
        fig_negative,
        width="stretch",
        key="sentiment_negative_count"
    )

    st.markdown("### Sentiment Data")

    st.dataframe(
        filtered_sentiment.round(2),
        hide_index=True,
        width="stretch"
    )

# =========================================================
# PAGE 3: PRODUCT ISSUES
# =========================================================
elif page == "Product Issues":

    st.subheader("Product Issue Analysis")

    st.write(
        "Explore keyword-based indicators of customer complaints "
        "from the previous SQL analysis."
    )

    st.warning(
        "Keyword counts are mention counts, not confirmed root causes "
        "or necessarily unique reviews. Grocery issue counts are not "
        "included because they were not available in the earlier results."
    )

    if filtered_issues.empty:
        st.info(
            "No keyword issue counts are available for the selected "
            "categories in this prototype."
        )
    else:
        issue_long = filtered_issues.melt(
            id_vars="Category",
            var_name="Issue Type",
            value_name="Keyword Mentions"
        )

        fig_issues = px.bar(
            issue_long,
            x="Category",
            y="Keyword Mentions",
            color="Issue Type",
            barmode="group",
            color_discrete_sequence=[
                "#174A7E", "#E76F51", "#2A9D8F", "#E9C46A"
            ]
        )

        fig_issues.update_layout(
            xaxis_title="Product Category",
            yaxis_title="Keyword Mentions",
            legend_title="Issue Type",
            margin=dict(l=10, r=10, t=25, b=10)
        )

        st.plotly_chart(
            fig_issues,
            width="stretch",
            key="product_issue_keywords"
        )

        st.markdown("### Keyword Mention Details")

        st.dataframe(
            filtered_issues,
            hide_index=True,
            width="stretch"
        )

    st.markdown("### Negative Review Volume")

    st.dataframe(
        filtered_negative.sort_values(
            "Negative Reviews", ascending=False
        ),
        hide_index=True,
        width="stretch"
    )

    st.caption(
        "Connect this page to detailed negative-review SQL results "
        "to support verified product-level recommendations."
    )

# =========================================================
# PAGE 4: BUSINESS INSIGHTS
# =========================================================
elif page == "Business Insights":

    st.subheader("Business Insights & Recommendations")

    best_category = filtered_ratings.loc[
        filtered_ratings["Average Rating"].idxmax()
    ]

    lowest_category = filtered_ratings.loc[
        filtered_ratings["Average Rating"].idxmin()
    ]

    highest_negative = filtered_sentiment.loc[
        filtered_sentiment["Negative"].idxmax()
    ]

    a, b, c = st.columns(3)

    a.metric(
        "Highest Average Rating",
        best_category["Category"],
        f'{best_category["Average Rating"]:.2f} / 5'
    )

    b.metric(
        "Lowest Average Rating",
        lowest_category["Category"],
        f'{lowest_category["Average Rating"]:.2f} / 5'
    )

    c.metric(
        "Highest Negative Percentage",
        highest_negative["Category"],
        f'{highest_negative["Negative"]:.2f}%'
    )

    st.divider()
    st.markdown("### Key Findings")

    st.markdown(f"""
    **1. Strongest-rated category**

    {best_category['Category']} has the highest average rating among
    the selected categories at {best_category['Average Rating']:.2f}/5.

    **2. Category requiring attention**

    {lowest_category['Category']} has the lowest average rating among
    the selected categories at {lowest_category['Average Rating']:.2f}/5.
    Detailed negative reviews should be investigated to understand the
    underlying reasons before choosing corrective actions.

    **3. Negative sentiment priority**

    {highest_negative['Category']} has the highest negative sentiment
    percentage among the selected categories at
    {highest_negative['Negative']:.2f}%. Review complaint themes and
    highly helpful negative reviews to identify potential priorities.
    """)

    st.markdown("### Recommended Actions")

    st.markdown("""
    - **Product quality:** Investigate repeated quality complaints
      and distinguish isolated incidents from recurring patterns.
    - **Product condition:** Examine reports of damaged or defective
      products and determine where further investigation is needed.
    - **Authenticity:** Review authenticity-related complaints
      carefully before drawing conclusions.
    - **Customer experience:** Examine highly helpful negative reviews
      to understand issues other customers also found relevant.
    - **Continuous monitoring:** Track category ratings and sentiment
      consistently as new feedback becomes available.
    """)

    st.caption(
        "Recommendations are based on category-level indicators. "
        "Validate specific root causes using detailed review data."
    )

# =========================================================
# FOOTER
# =========================================================
st.divider()

st.caption(
    "Amazon Customer Feedback Intelligence | "
    "Analytics prototype | Source: completed SQL analysis"
)
