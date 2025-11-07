# streamlit_app.py
import streamlit as st
import random
import pandas as pd

# -----------------------------
# Data
# -----------------------------
FUND_THEMES = [
    "AI-enabled SaaS",
    "Digital health",
    "Climate tech",
    "Vertical enterprise software",
    "Fintech infrastructure",
    "Future of work",
    "Cybersecurity",
]

DOMICILE = ["New York, USA"]

GEOGRAPHIES = [
    "North America",
    "Europe",
]

INVESTMENT_STAGES = [
    "Seed",
    "Series A",
    "Series B",
    "Growth equity",
]

SECTORS = [
    "Healthcare IT",
    "Financial Services",
    "Enterprise SaaS",
    "Sustainability",
    "Cybersecurity",
    "Logistics",
    "Consumer marketplaces",
]

DEGREES = [
    "MBA, Stanford GSB",
    "MBA, Harvard Business School",
    "MBA, Wharton School",
]

PAST_EMPLOYERS = [
    "Amazon",
    "Goldman Sachs",
    "McKinsey & Company",
]

SERVICE_PROVIDERS = {
    "legal": ["Cooley LLP", "Wilson Sonsini", "Fenwick & West", "Goodwin Procter"],
    "audit": ["KPMG", "Deloitte", "PwC", "EY"],
    "tax": ["BDO", "Grant Thornton", "RSM"],
    "fund_administration": ["Apex Fund Services", "Standish Management", "Juniper Square"],
}

FIRST_NAMES = ["Alex", "Jordan", "Taylor"]
LAST_NAMES = ["Chen", "Gonzalez", "Patel"]

COMPANY_DESCRIPTIONS = [
    {
        "CarbonPath": "AI-driven carbon accounting SaaS for manufacturers",
        "MedAI": "Digital therapeutics for chronic disease",
        "NovaGrid": "Energy optimization for distributed solar networks",
    }
]

# -----------------------------
# Helper functions
# -----------------------------
def generate_profile():
    """Generate a mock VC profile"""
    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    theme = random.choice(FUND_THEMES)
    geography = random.choice(GEOGRAPHIES)
    stage = random.choice(INVESTMENT_STAGES)
    sector = random.choice(SECTORS)
    degree = random.choice(DEGREES)
    employer = random.choice(PAST_EMPLOYERS)
    domicile = random.choice(DOMICILE)
    companies = random.choice(COMPANY_DESCRIPTIONS)
    company, description = random.choice(list(companies.items()))

    return {
        "Name": name,
        "Fund Theme": theme,
        "Geography": geography,
        "Investment Stage": stage,
        "Sector": sector,
        "Degree": degree,
        "Past Employer": employer,
        "Domicile": domicile,
        "Portfolio Company": company,
        "Company Description": description,
    }

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Venture Partner Profiles", layout="wide")
st.title("💼 Venture Partner Data Explorer")

st.sidebar.header("🔍 Filters")

# Filters
selected_theme = st.sidebar.multiselect("Fund Themes", FUND_THEMES)
selected_stage = st.sidebar.multiselect("Investment Stages", INVESTMENT_STAGES)
selected_sector = st.sidebar.multiselect("Sectors", SECTORS)
selected_geo = st.sidebar.multiselect("Geographies", GEOGRAPHIES)

# Generate sample data
num_profiles = st.sidebar.slider("Number of Profiles", 3, 20, 5)
profiles = [generate_profile() for _ in range(num_profiles)]
df = pd.DataFrame(profiles)

# Apply filters
if selected_theme:
    df = df[df["Fund Theme"].isin(selected_theme)]
if selected_stage:
    df = df[df["Investment Stage"].isin(selected_stage)]
if selected_sector:
    df = df[df["Sector"].isin(selected_sector)]
if selected_geo:
    df = df[df["Geography"].isin(selected_geo)]

# -----------------------------
# Main Dashboard
# -----------------------------
st.subheader("🧠 Generated Venture Profiles")
st.dataframe(df, use_container_width=True)

# Stats
st.markdown("### 📊 Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Profiles", len(df))
col2.metric("Unique Sectors", df['Sector'].nunique())
col3.metric("Themes Covered", df['Fund Theme'].nunique())

# Service Providers
st.markdown("### ⚙️ Service Providers")
for service, providers in SERVICE_PROVIDERS.items():
    st.markdown(f"**{service.title()}**: {', '.join(providers)}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("Built with ❤️ in Streamlit | Example venture partner data dashboard")
