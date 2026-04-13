import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="AiDash Customer Health Dashboard",
    page_icon="🌿",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv('customer_data_scored.csv')
    return df

df = load_data()

st.title("🌿 AiDash Customer Health Dashboard")
st.markdown(
    "Real-time view of customer engagement, health scores, "
    "and CSM action recommendations."
)
st.divider()

total       = len(df)
at_risk     = len(df[df['risk_level'] == 'At Risk'])
needs_attn  = len(df[df['risk_level'] == 'Needs Attention'])
healthy     = len(df[df['risk_level'] == 'Healthy'])
avg_health  = round(df['health_score'].mean(), 1)
revenue_at_risk = df[df['risk_level'] == 'At Risk']['contract_value'].sum()

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Total Customers",    total)
col2.metric("Healthy",            healthy)
col3.metric("Needs Attention",    needs_attn)
col4.metric("At Risk",            at_risk)
col5.metric("Avg Health Score",   avg_health)
col6.metric("Revenue at Risk",    f"${revenue_at_risk:,}")

st.divider()

st.sidebar.header("Filters")

selected_industry = st.sidebar.multiselect(
    "Industry",
    options=df['industry'].unique(),
    default=df['industry'].unique()
)

selected_risk = st.sidebar.multiselect(
    "Risk Level",
    options=['Healthy', 'Needs Attention', 'At Risk'],
    default=['Healthy', 'Needs Attention', 'At Risk']
)

min_contract, max_contract = st.sidebar.slider(
    "Contract Value (USD)",
    min_value=int(df['contract_value'].min()),
    max_value=int(df['contract_value'].max()),
    value=(int(df['contract_value'].min()), 
           int(df['contract_value'].max())),
    step=5000
)

filtered_df = df[
    (df['industry'].isin(selected_industry)) &
    (df['risk_level'].isin(selected_risk)) &
    (df['contract_value'] >= min_contract) &
    (df['contract_value'] <= max_contract)
]

st.sidebar.markdown(f"Showing **{len(filtered_df)}** of **{total}** customers")

st.subheader("Portfolio Overview")

col1, col2 = st.columns(2)

with col1:
    risk_counts = filtered_df['risk_level'].value_counts().reset_index()
    risk_counts.columns = ['risk_level', 'count']

    fig_pie = px.pie(
        risk_counts,
        names='risk_level',
        values='count',
        title='Risk Level Distribution',
        color='risk_level',
        color_discrete_map={
            'Healthy'         : '#2ecc71',
            'Needs Attention' : '#f39c12',
            'At Risk'         : '#e74c3c'
        }
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    fig_hist = px.histogram(
        filtered_df,
        x='health_score',
        color='risk_level',
        nbins=20,
        title='Health Score Distribution',
        color_discrete_map={
            'Healthy'         : '#2ecc71',
            'Needs Attention' : '#f39c12',
            'At Risk'         : '#e74c3c'
        }
    )
    st.plotly_chart(fig_hist, use_container_width=True)

st.divider()

st.subheader("Engagement Analysis")

col1, col2 = st.columns(2)

with col1:
    fig_scatter = px.scatter(
        filtered_df,
        x='logins_last_30_days',
        y='health_score',
        color='risk_level',
        size='contract_value',
        hover_data=['customer_name', 'recommended_action'],
        title='Login Frequency vs Health Score',
        color_discrete_map={
            'Healthy'         : '#2ecc71',
            'Needs Attention' : '#f39c12',
            'At Risk'         : '#e74c3c'
        }
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    industry_risk = filtered_df.groupby(
        ['industry', 'risk_level']).size().reset_index(name='count')

    fig_industry = px.bar(
        industry_risk,
        x='industry',
        y='count',
        color='risk_level',
        barmode='group',
        title='Risk Breakdown by Industry',
        color_discrete_map={
            'Healthy'         : '#2ecc71',
            'Needs Attention' : '#f39c12',
            'At Risk'         : '#e74c3c'
        }
    )
    st.plotly_chart(fig_industry, use_container_width=True)

st.divider()

st.subheader("Priority At-Risk Accounts")
st.markdown("Sorted by contract value — highest revenue risk first.")

at_risk_df = filtered_df[
    filtered_df['risk_level'] == 'At Risk'
].sort_values('contract_value', ascending=False)

if len(at_risk_df) == 0:
    st.success("No at-risk accounts in current filter selection.")
else:
    fig_bar = px.bar(
        at_risk_df,
        x='customer_name',
        y='contract_value',
        color='health_score',
        color_continuous_scale='Reds_r',
        title='At-Risk Accounts by Contract Value',
        labels={
            'customer_name'  : 'Customer',
            'contract_value' : 'Contract Value (USD)',
            'health_score'   : 'Health Score'
        }
    )
    fig_bar.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

st.subheader("Full Customer Health Table")

def color_risk(val):
    if val == 'At Risk':
        return 'background-color: #fde8e8; color: #c0392b'
    elif val == 'Needs Attention':
        return 'background-color: #fef3e2; color: #d35400'
    else:
        return 'background-color: #e8f8f0; color: #1e8449'

display_cols = [
    'customer_id',
    'customer_name',
    'industry',
    'contract_value',
    'health_score',
    'risk_level',
    'logins_last_30_days',
    'feature_adoption_rate',
    'open_tickets',
    'contract_renewal_days',
    'recommended_action'
]

styled_df = filtered_df[display_cols].sort_values(
    'health_score'
).style.map(color_risk, subset=['risk_level'])

st.dataframe(styled_df, use_container_width=True, height=400)

st.divider()

st.subheader("Customer Deep Dive")
st.markdown("Select a customer to see their full health breakdown.")

selected_customer = st.selectbox(
    "Choose a customer",
    options=filtered_df['customer_name'].sort_values()
)

customer = filtered_df[
    filtered_df['customer_name'] == selected_customer
].iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Health Score",        customer['health_score'])
col2.metric("Risk Level",          customer['risk_level'])
col3.metric("Contract Value",      f"${customer['contract_value']:,}")

col4, col5, col6 = st.columns(3)
col4.metric("Logins (30 days)",    customer['logins_last_30_days'])
col5.metric("Open Tickets",        customer['open_tickets'])
col6.metric("Renewal in (days)",   customer['contract_renewal_days'])

st.markdown("**Recommended Action:**")
st.info(customer['recommended_action'])

score_data = pd.DataFrame({
    'Signal': [
        'Login Score',
        'Adoption Score',
        'Ticket Score',
        'Recency Score',
        'AI Acceptance Score'
    ],
    'Score': [
        customer['login_score'],
        customer['adoption_score'],
        customer['ticket_score'],
        customer['recency_score'],
        customer['ai_score']
    ]
})

fig_radar = px.bar_polar(
    score_data,
    r='Score',
    theta='Signal',
    color='Score',
    color_continuous_scale='RdYlGn',
    title=f'Health Signal Breakdown — {selected_customer}',
    range_r=[0, 100]
)
st.plotly_chart(fig_radar, use_container_width=True)

st.divider()

st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 13px;'>
    AiDash Customer Health Dashboard — Built for Customer Success Team<br>
    Data refreshes weekly | Scores weighted across 5 engagement signals
    </div>
    """,
    unsafe_allow_html=True
)

