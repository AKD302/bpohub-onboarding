import streamlit as st

st.set_page_config(
    page_title="BPOHub – Client Onboarding",
    page_icon="📊",
    layout="centered",
)

# ---------- Helper: checkbox group (multi-select bullets) ----------

def checkbox_group(label, options, key_prefix):
    """
    Renders a label + a group of checkboxes.
    Returns a list of selected options.
    key_prefix must be unique per question.
    """
    st.markdown(f"**{label}**")
    selected = []
    for i, opt in enumerate(options):
        if st.checkbox(opt, key=f"{key_prefix}_{i}"):
            selected.append(opt)
    st.markdown("---")
    return selected


# ---------- Initialize step ----------

if "step" not in st.session_state:
    st.session_state.step = 1

TOTAL_STEPS = 5

def go_next():
    if st.session_state.step < TOTAL_STEPS:
        st.session_state.step += 1

def go_prev():
    if st.session_state.step > 1:
        st.session_state.step -= 1


st.title("BPOHub – Client Onboarding")
st.caption("Help us understand your firm so we can design the right support model for you.")

st.progress(st.session_state.step / TOTAL_STEPS)
st.write(f"Step {st.session_state.step} of {TOTAL_STEPS}")

# ---------- MAIN MULTI-STEP FORM ----------

with st.form(key=f"step_form_{st.session_state.step}"):

    # ---------------- STEP 1: BASIC BUSINESS INFO ----------------
    if st.session_state.step == 1:
        st.subheader("Basic Business Information")

        name = st.text_input("Your Name")
        company = st.text_input("Company / Firm Name")
        email = st.text_input("Email Address")
        country = st.text_input("Country of Operation")
        sector = st.text_input("Primary Industry / Client Sector")

        firm_size_options = [
            "Solo CPA",
            "Small Firm (1–10 staff)",
            "Mid-size Firm (11–50 staff)",
            "Large Firm (50+ staff)",
        ]
        selected_firm_sizes = checkbox_group(
            "Size of Your Firm (you may select more than one if you operate multiple entities):",
            firm_size_options,
            key_prefix="firm_size",
        )

        system_options = [
            "QuickBooks",
            "Xero",
            "NetSuite",
            "SAP",
            "Sage",
            "Excel",
            "Other / Mixed",
        ]
        selected_systems = checkbox_group(
            "Which accounting systems do you currently use?",
            system_options,
            key_prefix="acct_systems",
        )

    # ---------------- STEP 2: HIGH-LEVEL OVERVIEW ----------------
    elif st.session_state.step == 2:
        st.subheader("High-Level Accounting & Operations Overview")

        challenges = checkbox_group(
            "What are the biggest challenges you currently face in your finance function?",
            [
                "High operational costs",
                "Staff shortage",
                "Delayed month-end close",
                "Accuracy issues",
                "Outdated software / tools",
                "Compliance burden",
                "Seasonal workload spikes",
                "Other",
            ],
            key_prefix="challenges",
        )

        cost_pressure = checkbox_group(
            "Are your current bookkeeping and accounting costs higher than expected?",
            [
                "Yes",
                "No",
                "Not sure",
            ],
            key_prefix="cost_pressure",
        )

        books_status = checkbox_group(
            "How current are your books and reconciliations? (select all that apply across different entities)",
            [
                "Fully up to date",
                "1–2 months behind",
                "3–6 months behind",
                "More than 6 months behind (cleanup required)",
            ],
            key_prefix="books_status",
        )

        busy_season = checkbox_group(
            "Do you experience seasonal workload spikes (e.g., tax season)?",
            [
                "Yes — high impact",
                "Yes — moderate impact",
                "No",
            ],
            key_prefix="busy_season",
        )

        close_time = checkbox_group(
            "How long does your month-end close usually take across your entities?",
            [
                "Less than 10 days",
                "10–20 days",
                "More than 20 days",
            ],
            key_prefix="close_time",
        )

    # ---------------- STEP 3: PROCESS & COMPLIANCE ----------------
    elif st.session_state.step == 3:
        st.subheader("Process, Controls & Compliance")

        delay_areas = checkbox_group(
            "Which areas currently cause the most delays or rework?",
            [
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
            key_prefix="delay_areas",
        )

        capacity = checkbox_group(
            "Do you have sufficient internal capacity for audits, tax deadlines, and regulatory compliance?",
            [
                "Yes",
                "Partially",
                "No",
            ],
            key_prefix="capacity",
        )

        sop_needs = checkbox_group(
            "Which processes require SOPs or standardization?",
            [
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
            key_prefix="sop_needs",
        )

        erp_status = checkbox_group(
            "Are you planning or currently undergoing an ERP or accounting system migration?",
            [
                "Yes, ongoing",
                "Planned in next 3–6 months",
                "Yes but delayed",
                "No",
            ],
            key_prefix="erp_status",
        )

        compliance_issues = checkbox_group(
            "Do you face challenges with audit readiness, compliance, or internal controls?",
            [
                "Yes — recurring issues",
                "Occasionally",
                "No",
                "No, but we need better documentation",
            ],
            key_prefix="compliance_issues",
        )

        reporting_confidence = checkbox_group(
            "How confident are you in your reporting accuracy, dashboards, and analytics?",
            [
                "Very confident",
                "Somewhat confident",
                "Not confident",
                "Reporting delays are impacting decision-making",
            ],
            key_prefix="reporting_confidence",
        )

    # ---------------- STEP 4: SCALABILITY & STRATEGIC ----------------
    elif st.session_state.step == 4:
        st.subheader("Scalability & Strategic Needs")

        constraint = checkbox_group(
            "What is the biggest constraint limiting your ability to scale?",
            [
                "Lack of skilled staff",
                "High operational costs",
                "Manual processes",
                "Inconsistent turnaround times",
                "Limited FP&A / advisory bandwidth",
                "Other",
            ],
            key_prefix="constraint",
        )

        growth_plan = checkbox_group(
            "What are your growth plans for the next 12 months?",
            [
                "Maintain current size",
                "Moderate growth",
                "Rapid scaling",
            ],
            key_prefix="growth_plan",
        )

        urgency = checkbox_group(
            "How urgent is your need for additional finance or back-office support?",
            [
                "Immediate",
                "Within 1–3 months",
                "3–6 months",
                "Just exploring",
            ],
            key_prefix="urgency",
        )

    # ---------------- STEP 5: ADVANCED DIAGNOSTIC & NOTES ----------------
    elif st.session_state.step == 5:
        st.subheader("Advanced Diagnostic & Additional Context")

        automation_targets = checkbox_group(
            "Which processes would benefit most from automation or tech enablement?",
            [
                "AP automation",
                "AR automation",
                "Bank feeds & reconciliation automation",
                "Financial dashboards",
                "Reporting packs / consolidations",
                "All of the above",
                "Not sure",
            ],
            key_prefix="automation_targets",
        )

        risk_areas = checkbox_group(
            "Where do you see the highest risk of errors or compliance issues?",
            [
                "Intercompany accounting",
                "Revenue recognition",
                "Reconciliations",
                "Audit preparation",
                "Tax schedules",
                "Financial reporting",
                "Other",
            ],
            key_prefix="risk_areas",
        )

        support_type = checkbox_group(
            "What type of support are you seeking from BPOHub?",
            [
                "Full finance back-office outsourcing",
                "Specific process support (AP/AR/Payroll/Reporting)",
                "Cleanup & catch-up accounting",
                "ERP migration & data transfer",
                "BI / Dashboarding",
                "Seasonal / tax season staffing",
                "CFO / FP&A advisory",
                "Not sure — need guidance",
            ],
            key_prefix="support_type",
        )

        notes = st.text_area(
            "Please share any additional context, pain points, or goals you want us to consider.",
            height=150,
        )

    # ------------- NAVIGATION BUTTONS -------------

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.session_state.step > 1:
            prev_clicked = st.form_submit_button("⬅ Previous")
            if prev_clicked:
                go_prev()

    with col2:
        if st.session_state.step < TOTAL_STEPS:
            next_clicked = st.form_submit_button("Next ➜")
            if next_clicked:
                go_next()
        else:
            submit_clicked = st.form_submit_button("✅ Submit")
            if submit_clicked:
                st.success("Thank you for taking out the time to engage with here! Your onboarding responses have been submitted to the relevant team at BPO Hub. Our representatives will reach out to you shortly")
                st.balloons()
