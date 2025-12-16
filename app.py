import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="BPOHub – Client Onboarding",
    page_icon="📊",
    layout="wide",
)

# -------------------- OPTIONS ------------------------
OPTIONS = {
    "firm_size": [
        "Solo CPA",
        "Small Firm (1–10 staff)",
        "Mid-size Firm (11–50 staff)",
        "Large Firm (50+ staff)",
    ],
    "acct_systems": [
        "QuickBooks",
        "Xero",
        "NetSuite",
        "SAP",
        "Sage",
        "Excel",
        "Other / Mixed",
    ],
    "challenges": [
        "High operational costs",
        "Staff shortage",
        "Delayed month-end close",
        "Accuracy issues",
        "Outdated software / tools",
        "Compliance burden",
        "Seasonal workload spikes",
        "Other",
    ],
    "cost_pressure": ["Yes", "No", "Not sure"],
    "books_status": [
        "Fully up to date",
        "1–2 months behind",
        "3–6 months behind",
        "More than 6 months behind (cleanup required)",
    ],
    "busy_season": [
        "Yes — high impact",
        "Yes — moderate impact",
        "No",
    ],
    "close_time": [
        "Less than 10 days",
        "10–20 days",
        "More than 20 days",
    ],
    "delay_areas": [
        "AP (Vendor Bills & Payments)",
        "AR (Invoicing & Collections)",
        "Bookkeeping & Data Entry",
        "Bank Reconciliations",
        "Payroll",
        "Month-End Close",
        "Tax Preparation",
        "Reporting & Dashboards",
        "Compliance / Internal Controls",
        "Other",
    ],
    "capacity": ["Yes", "Partially", "No"],
    "sop_needs": [
        "AP",
        "AR",
        "GL",
        "Payroll",
        "Month-End Close",
        "Reporting",
        "Compliance",
        "All of the above",
        "Not sure",
    ],
    "erp_status": [
        "Yes, ongoing",
        "Planned in next 3–6 months",
        "Yes but delayed",
        "No",
    ],
    "compliance_issues": [
        "Yes — recurring issues",
        "Occasionally",
        "No",
        "No, but we need better documentation",
    ],
    "reporting_confidence": [
        "Very confident",
        "Somewhat confident",
        "Not confident",
        "Reporting delays are impacting decision-making",
    ],
    "constraint": [
        "Lack of skilled staff",
        "High operational costs",
        "Manual processes",
        "Inconsistent turnaround times",
        "Limited FP&A / advisory bandwidth",
        "Other",
    ],
    "growth_plan": [
        "Maintain current size",
        "Moderate growth",
        "Rapid scaling",
    ],
    "urgency": [
        "Immediate",
        "Within 1–3 months",
        "3–6 months",
        "Just exploring",
    ],
    "automation_targets": [
        "AP automation",
        "AR automation",
        "Bank feeds & reconciliation automation",
        "Financial dashboards",
        "Reporting packs / consolidations",
        "All of the above",
        "Not sure",
    ],
    "risk_areas": [
        "Intercompany accounting",
        "Revenue recognition",
        "Reconciliations",
        "Audit preparation",
        "Tax schedules",
        "Financial reporting",
        "Other",
    ],
    "support_type": [
        "Full finance back-office outsourcing",
        "Specific process support (AP/AR/Payroll/Reporting)",
        "Cleanup & catch-up accounting",
        "ERP migration & data transfer",
        "BI / Dashboarding",
        "Seasonal / tax season staffing",
        "CFO / FP&A advisory",
        "Not sure — need guidance",
    ],
}

# -------------------- CSS ---------------------------
CUSTOM_CSS = """
<style>
html, body, [class*="css"]  {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
body {
    background: radial-gradient(circle at top left, #eef2ff, #f9fafb 35%, #f5f7fb);
}
.main-container {
    max-width: 980px;
    margin: 24px auto 48px auto;
}
.app-card {
    background: #ffffff;
    border-radius: 24px;
    padding: 22px 26px 24px 26px;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.10);
    border: 1px solid rgba(148, 163, 184, 0.35);
}
.brand-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}
.brand-left {
    display: flex;
    align-items: center;
    gap: 10px;
}
.brand-logo {
    width: 32px;
    height: 32px;
    border-radius: 12px;
    background: linear-gradient(135deg, #1d4ed8, #4f46e5);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #e5e7eb;
    font-weight: 700;
    font-size: 18px;
}
.brand-text-title {
    font-size: 20px;
    font-weight: 600;
    color: #0f172a;
}
.brand-text-sub {
    font-size: 12px;
    color: #6b7280;
}
.step-pills {
    display: flex;
    gap: 6px;
    font-size: 11px;
    margin: 8px 0 4px 0;
    flex-wrap: wrap;
}
.step-pill {
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid #e5e7eb;
    background: #f9fafb;
    color: #6b7280;
}
.step-pill.active {
    border-color: rgba(59, 130, 246, 0.6);
    background: rgba(37, 99, 235, 0.07);
    color: #1d4ed8;
    font-weight: 600;
}
.section-title {
    font-size: 16px;
    font-weight: 600;
    color: #111827;
    margin: 8px 0 2px 0;
}
.section-caption {
    font-size: 12px;
    color: #6b7280;
    margin-bottom: 14px;
}
.question-label {
    font-weight: 500;
    margin: 10px 0 4px 0;
    color: #111827;
    font-size: 13px;
}
.checkbox-wrap {
    padding: 8px 12px 4px 12px;
    border-radius: 14px;
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    margin-bottom: 10px;
}
.block-container {
    padding-top: 10px !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: visible;}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -------------------- HELPERS ------------------------
def checkbox_group(label: str, options: list[str], key_prefix: str):
    """Render a labelled group of checkboxes (multi-select)."""
    st.markdown(f'<div class="question-label">{label}</div>', unsafe_allow_html=True)
    st.markdown('<div class="checkbox-wrap">', unsafe_allow_html=True)
    for i, opt in enumerate(options):
        st.checkbox(opt, key=f"{key_prefix}_{i}")
    st.markdown("</div>", unsafe_allow_html=True)

def get_selected(prefix: str, options: list[str]):
    """Read which checkboxes are selected for a given group."""
    selected = []
    for i, opt in enumerate(options):
        if st.session_state.get(f"{prefix}_{i}", False):
            selected.append(opt)
    return selected

# -------------------- STEP STATE ---------------------
if "step" not in st.session_state:
    st.session_state.step = 1

TOTAL_STEPS = 6

def set_step(new_step: int):
    if 1 <= new_step <= TOTAL_STEPS:
        st.session_state.step = new_step

# -------------------- MAIN LAYOUT --------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="app-card">', unsafe_allow_html=True)

# Header
col_header_left, col_header_right = st.columns([3, 1.6])
with col_header_left:
    st.markdown(
        """
        <div class="brand-header">
          <div class="brand-left">
            <div class="brand-logo">B</div>
            <div>
              <div class="brand-text-title">BPOHub – Client Diagnostic</div>
              <div class="brand-text-sub">
                A guided intake so we understand your finance & accounting needs before our call.
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_header_right:
    pill_html = '<div class="step-pills">'
    step_names = [
        "1 · Profile",
        "2 · Overview",
        "3 · Processes",
        "4 · Scalability",
        "5 · Advanced",
        "6 · Review",
    ]
    for idx, name in enumerate(step_names, start=1):
        cls = "step-pill active" if st.session_state.step == idx else "step-pill"
        pill_html += f'<div class="{cls}">{name}</div>'
    pill_html += "</div>"
    st.markdown(pill_html, unsafe_allow_html=True)

st.progress(st.session_state.step / TOTAL_STEPS)

step = st.session_state.step

# -------------------- STEP CONTENT -------------------

# STEP 1 – PROFILE
if step == 1:
    st.markdown('<div class="section-title">Step 1 · Basic Business Information</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Tell us who you are so we can tailor our proposal to your firm.</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Your Name", key="name")
        st.text_input("Email Address", key="email")
        st.text_input("Country of Operation", key="country")
    with c2:
        st.text_input("Company / Firm Name", key="company")
        st.text_input("Primary Industry / Client Sector", key="sector")

    checkbox_group(
        "Size of your firm (select all that apply if you operate multiple entities):",
        OPTIONS["firm_size"],
        key_prefix="firm_size",
    )

    checkbox_group(
        "Which accounting systems do you currently use?",
        OPTIONS["acct_systems"],
        key_prefix="acct_systems",
    )

# STEP 2 – OVERVIEW
elif step == 2:
    st.markdown('<div class="section-title">Step 2 · High-Level Accounting & Operations</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A quick snapshot of how your finance function is running today.</div>',
        unsafe_allow_html=True,
    )

    checkbox_group(
        "What are the biggest challenges you currently face in your finance function?",
        OPTIONS["challenges"],
        key_prefix="challenges",
    )

    checkbox_group(
        "Are your current bookkeeping and accounting costs higher than expected?",
        OPTIONS["cost_pressure"],
        key_prefix="cost_pressure",
    )

    checkbox_group(
        "How current are your books and reconciliations? (you can select more than one across entities)",
        OPTIONS["books_status"],
        key_prefix="books_status",
    )

    checkbox_group(
        "Do you experience seasonal workload spikes (e.g., tax season)?",
        OPTIONS["busy_season"],
        key_prefix="busy_season",
    )

    checkbox_group(
        "How long does your month-end close usually take across your entities?",
        OPTIONS["close_time"],
        key_prefix="close_time",
    )

# STEP 3 – PROCESSES
elif step == 3:
    st.markdown('<div class="section-title">Step 3 · Processes, Controls & Compliance</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Help us identify where processes slow you down or create risk.</div>',
        unsafe_allow_html=True,
    )

    checkbox_group(
        "Which areas currently cause the most delays or rework?",
        OPTIONS["delay_areas"],
        key_prefix="delay_areas",
    )

    checkbox_group(
        "Do you have sufficient internal capacity for audits, tax deadlines, and regulatory compliance?",
        OPTIONS["capacity"],
        key_prefix="capacity",
    )

    checkbox_group(
        "Which processes require SOPs or standardisation?",
        OPTIONS["sop_needs"],
        key_prefix="sop_needs",
    )

    checkbox_group(
        "Are you planning or currently undergoing an ERP or accounting system migration?",
        OPTIONS["erp_status"],
        key_prefix="erp_status",
    )

    checkbox_group(
        "Do you face challenges with audit readiness, compliance, or internal controls?",
        OPTIONS["compliance_issues"],
        key_prefix="compliance_issues",
    )

    checkbox_group(
        "How confident are you in your reporting accuracy, dashboards, and analytics?",
        OPTIONS["reporting_confidence"],
        key_prefix="reporting_confidence",
    )

# STEP 4 – SCALABILITY
elif step == 4:
    st.markdown('<div class="section-title">Step 4 · Scalability & Strategic Needs</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">This helps us match the engagement model with your growth plans.</div>',
        unsafe_allow_html=True,
    )

    checkbox_group(
        "What is the biggest constraint limiting your ability to scale?",
        OPTIONS["constraint"],
        key_prefix="constraint",
    )

    checkbox_group(
        "What are your growth plans for the next 12 months?",
        OPTIONS["growth_plan"],
        key_prefix="growth_plan",
    )

    checkbox_group(
        "How urgent is your need for additional finance or back-office support?",
        OPTIONS["urgency"],
        key_prefix="urgency",
    )

# STEP 5 – ADVANCED
elif step == 5:
    st.markdown('<div class="section-title">Step 5 · Advanced Diagnostic & Additional Context</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Final details so we can come prepared to our first working session.</div>',
        unsafe_allow_html=True,
    )

    checkbox_group(
        "Which processes would benefit most from automation or tech enablement?",
        OPTIONS["automation_targets"],
        key_prefix="automation_targets",
    )

    checkbox_group(
        "Where do you see the highest risk of errors or compliance issues?",
        OPTIONS["risk_areas"],
        key_prefix="risk_areas",
    )

    checkbox_group(
        "What type of support are you seeking from BPOHub?",
        OPTIONS["support_type"],
        key_prefix="support_type",
    )

    st.text_area(
        "Please share any additional context, pain points, or goals you want us to consider.",
        height=150,
        key="notes",
    )

# STEP 6 – REVIEW
elif step == 6:
    st.markdown('<div class="section-title">Step 6 · Review & Confirm</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Review all answers below. You can go back to previous steps to edit.</div>',
        unsafe_allow_html=True,
    )

    st.subheader("Basic Information")
    st.write(f"**Name:** {st.session_state.get('name', '')}")
    st.write(f"**Email:** {st.session_state.get('email', '')}")
    st.write(f"**Company:** {st.session_state.get('company', '')}")
    st.write(f"**Country:** {st.session_state.get('country', '')}")
    st.write(f"**Sector:** {st.session_state.get('sector', '')}")

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Firm Profile & Systems")
        st.write("**Firm size:**")
        st.write(", ".join(get_selected("firm_size", OPTIONS["firm_size"])) or "Not specified")

        st.write("**Accounting systems:**")
        st.write(", ".join(get_selected("acct_systems", OPTIONS["acct_systems"])) or "Not specified")

        st.subheader("Challenges & Status")
        st.write("**Key challenges:**")
        st.write(", ".join(get_selected("challenges", OPTIONS["challenges"])) or "Not specified")

        st.write("**Cost pressure:**")
        st.write(", ".join(get_selected("cost_pressure", OPTIONS["cost_pressure"])) or "Not specified")

        st.write("**Books & reconciliations status:**")
        st.write(", ".join(get_selected("books_status", OPTIONS["books_status"])) or "Not specified")

        st.write("**Busy season impact:**")
        st.write(", ".join(get_selected("busy_season", OPTIONS["busy_season"])) or "Not specified")

        st.write("**Month-end close duration:**")
        st.write(", ".join(get_selected("close_time", OPTIONS["close_time"])) or "Not specified")

    with col_b:
        st.subheader("Processes & Controls")
        st.write("**Delay / rework areas:**")
        st.write(", ".join(get_selected("delay_areas", OPTIONS["delay_areas"])) or "Not specified")

        st.write("**Capacity for audits & compliance:**")
        st.write(", ".join(get_selected("capacity", OPTIONS["capacity"])) or "Not specified")

        st.write("**SOP / standardisation needs:**")
        st.write(", ".join(get_selected("sop_needs", OPTIONS["sop_needs"])) or "Not specified")

        st.write("**ERP / system migration status:**")
        st.write(", ".join(get_selected("erp_status", OPTIONS["erp_status"])) or "Not specified")

        st.write("**Audit & compliance challenges:**")
        st.write(", ".join(get_selected("compliance_issues", OPTIONS["compliance_issues"])) or "Not specified")

        st.write("**Reporting confidence:**")
        st.write(", ".join(get_selected("reporting_confidence", OPTIONS["reporting_confidence"])) or "Not specified")

    st.markdown("---")

    st.subheader("Scalability & Strategic")
    st.write("**Scaling constraints:**")
    st.write(", ".join(get_selected("constraint", OPTIONS["constraint"])) or "Not specified")

    st.write("**Growth plan (12 months):**")
    st.write(", ".join(get_selected("growth_plan", OPTIONS["growth_plan"])) or "Not specified")

    st.write("**Urgency for support:**")
    st.write(", ".join(get_selected("urgency", OPTIONS["urgency"])) or "Not specified")

    st.markdown("---")

    st.subheader("Advanced Signals")
    st.write("**Automation targets:**")
    st.write(", ".join(get_selected("automation_targets", OPTIONS["automation_targets"])) or "Not specified")

    st.write("**Risk areas:**")
    st.write(", ".join(get_selected("risk_areas", OPTIONS["risk_areas"])) or "Not specified")

    st.write("**Support type sought:**")
    st.write(", ".join(get_selected("support_type", OPTIONS["support_type"])) or "Not specified")

    st.write("**Additional notes:**")
    st.write(st.session_state.get("notes", "") or "_None provided_")

    st.markdown("---")
    if st.button("✅ Submit form"):
        st.success(
            "Thank you! Your responses have been submitted. "
            "A BPOHub consultant will review them and get back to you."
        )
        st.balloons()

# -------------------- NAV BUTTONS --------------------
st.markdown("---")
col_prev, col_next, _ = st.columns([1, 1, 6])

with col_prev:
    st.button(
        "⬅ Previous",
        disabled=(step == 1),
        on_click=set_step,
        args=(step - 1,),
    )

with col_next:
    label = "Next ➜" if step < TOTAL_STEPS else "Review ➜"
    st.button(
        label,
        disabled=(step == TOTAL_STEPS),
        on_click=set_step,
        args=(step + 1,),
    )

st.markdown("</div></div>", unsafe_allow_html=True)
