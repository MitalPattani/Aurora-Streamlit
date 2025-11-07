import streamlit as st
import random

# -----------------------------
# Data
# -----------------------------
FUND_THEMES = [
    "AI-enabled SaaS", "Digital health", "Climate tech",
    "Vertical enterprise software", "Fintech infrastructure",
    "Future of work", "Cybersecurity"
]

DOMICILE = ["New York, USA"]

GEOGRAPHIES = ["North America", "Europe"]

INVESTMENT_STAGES = ["Seed", "Series A", "Series B", "Growth equity"]

SECTORS = [
    "Healthcare IT", "Financial Services", "Enterprise SaaS",
    "Sustainability", "Cybersecurity", "Logistics", "Consumer marketplaces"
]

DEGREES = [
    "MBA, Stanford GSB", "MBA, Harvard Business School", "MBA, Wharton School"
]

PAST_EMPLOYERS = ["Amazon", "Goldman Sachs", "McKinsey & Company"]

SERVICE_PROVIDERS = {
    "legal": ["Cooley LLP", "Wilson Sonsini", "Fenwick & West", "Goodwin Procter"],
    "audit": ["KPMG", "Deloitte", "PwC", "EY"],
    "tax": ["BDO", "Grant Thornton", "RSM"],
    "fund_administration": ["Apex Fund Services", "Standish Management", "Juniper Square"],
}

FIRST_NAMES = ["Alex", "Jordan", "Taylor"]
LAST_NAMES = ["Chen", "Gonzalez", "Patel"]

COMPANY_DESCRIPTIONS = [{
    "CarbonPath": "AI-driven carbon accounting SaaS for manufacturers",
    "MedAI": "Digital therapeutics for chronic disease",
    "NovaGrid": "Energy optimization for distributed solar networks"
}]

# -----------------------------
# Helper
# -----------------------------
def generate_team_member():
    return {
        "name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
        "degree": random.choice(DEGREES),
        "employer": random.choice(PAST_EMPLOYERS)
    }

# -----------------------------
# Layout
# -----------------------------
st.set_page_config(page_title="Aurora Capital", layout="wide")

# Hero section
st.title("🌍 Aurora Capital")
st.subheader("Backing category-defining founders across AI, Climate, and Digital Transformation.")
st.markdown("**Domicile:** New York, USA  \n**Geographies:** North America · Europe")

st.markdown("---")

# About section
st.header("🏢 About Us")
st.write(
    """Aurora Capital is a venture capital firm investing at the intersection of technology and impact.
    We partner with exceptional founders from Seed to Growth stages, building scalable solutions
    in software, sustainability, and digital infrastructure."""
)

# Fund focus
st.header("🎯 Investment Focus")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Fund Themes:**")
    st.write(", ".join(FUND_THEMES))
    st.markdown("**Investment Stages:**")
    st.write(", ".join(INVESTMENT_STAGES))
with col2:
    st.markdown("**Sectors:**")
    st.write(", ".join(SECTORS))
    st.markdown("**Geographies:**")
    st.write(", ".join(GEOGRAPHIES))

# Portfolio
st.header("🚀 Portfolio Highlights")
companies = random.choice(COMPANY_DESCRIPTIONS)
for name, desc in companies.items():
    st.markdown(f"**{name}** — {desc}")

# Team
st.header("👥 Our Team")
cols = st.columns(3)
for i, col in enumerate(cols):
    member = generate_team_member()
    with col:
        st.subheader(member["name"])
        st.write(member["degree"])
        st.write(f"Previously at {member['employer']}")

# Service Providers
st.header("⚙️ Service Providers")
for category, providers in SERVICE_PROVIDERS.items():
    st.markdown(f"**{category.title()}**: {', '.join(providers)}")

# Footer
st.markdown("---")
st.caption("© 2025 Aurora Capital — All rights reserved.")
