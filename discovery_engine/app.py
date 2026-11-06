
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="SIP Continuity | AI Discovery Engine",
    page_icon="🔎",
    layout="wide"
)

ROOT = Path(__file__).parent

@st.cache_data
def load_csv(filename):
    return pd.read_csv(ROOT / filename).fillna("")

evidence = load_csv("sip_evidence.csv")
baseline = load_csv("baseline_predictions.csv")
golden = load_csv("golden_set.csv")
gate_tests = load_csv("ai_gate_tests.csv")

st.title("🔎 SIP Continuity Discovery Engine")
st.caption(
    "Groww growth PM research | Public evidence explorer | "
    "Prototype, not an official Groww product"
)

st.info(
    "Research in progress. Public posts are self-reports; "
    "they do not establish Groww's actual 12-month retention. "
    "Some excerpts and classifications await human verification."
)

tab1, tab2, tab3, tab4 = st.tabs([
    "Evidence Explorer",
    "Behavioral Patterns",
    "AI Evaluation",
    "Metric & Methodology"
])

with tab1:
    st.subheader("Public evidence explorer")

    search = st.text_input(
        "Search excerpts, themes, or SIP status"
    )

    themes = sorted(
        evidence["primary_theme"].dropna().unique()
    )

    selected = st.multiselect(
        "Filter by behavioral theme",
        themes,
        default=themes
    )

    filtered = evidence[
        evidence["primary_theme"].isin(selected)
    ].copy()

    if search:
        searchable = filtered.astype(str).agg(
            " ".join, axis=1
        )
        filtered = filtered[
            searchable.str.contains(
                search, case=False, regex=False
            )
        ]

    st.metric("Matching records", len(filtered))

    for _, item in filtered.iterrows():
        label = (
            f"{item.get('evidence_id', '')} — "
            f"{item.get('primary_theme', '')}"
        )

        with st.expander(label):
            st.write(
                "**Original excerpt:**",
                item.get("original_text", "")
            )
            st.write(
                "**SIP status:**",
                item.get("sip_status", "Unknown")
            )
            st.write(
                "**First-year eligibility:**",
                item.get("investor_experience", "Unknown")
            )
            st.write(
                "**Verification:**",
                item.get("verification_status", "Pending")
            )
            url = str(item.get("source_url", ""))
            if url.startswith(("https://", "http://")):
                st.markdown(f"[Open public source]({url})")

with tab2:
    st.subheader("Observed behavioral patterns")
    st.caption(
        "Descriptive counts within a small, "
        "non-representative research sample."
    )

    counts = (
        evidence["primary_theme"]
        .value_counts()
        .rename_axis("Theme")
        .reset_index(name="Records")
    )

    st.dataframe(counts, use_container_width=True)
    st.bar_chart(
        counts.set_index("Theme")["Records"]
    )

    st.subheader("Research opportunity hypotheses")
    st.markdown("""
    **1. Interruption clarity:** Help users distinguish
    failed payments, deliberate pauses, and completed stops.

    **2. Life-event flexibility:** Explain neutral,
    user-controlled options when financial priorities change.

    **3. Restart confidence:** Help users understand
    what happened and how to check their SIP status
    before deciding what to do next.
    """)

    st.warning(
        "These opportunities are hypotheses, not "
        "validated rankings. Interviews and additional "
        "verified evidence must determine priority."
    )

with tab3:
    st.subheader("AI evaluation and safeguards")

    st.write(
        "The project tested a Gemini classification "
        "on SIP002 and deliberately injected three "
        "faults to test the quality gate."
    )

    st.dataframe(
        gate_tests,
        use_container_width=True
    )

    st.caption(
        "The gate-test rows are synthetic fault-injection "
        "cases, not independent AI predictions."
    )

    st.subheader("Non-AI keyword baseline")
    st.dataframe(
        baseline,
        use_container_width=True
    )

    st.subheader("Human-labeled golden set")
    st.dataframe(
        golden,
        use_container_width=True
    )

    st.warning(
        "AI-vs-baseline accuracy is not reported until "
        "human labels, normalized categories, and "
        "comparable AI predictions are available."
    )

    st.subheader("Safe fallback")
    st.write(
        "When a prediction is unsupported or fails "
        "validation, the intended behavior is to show "
        "'Needs human review' rather than presenting "
        "the prediction as a verified finding."
    )

with tab4:
    st.subheader("North-star metric")

    st.latex(
        r"R_{12}=\\frac{\\text{First-time SIP starters "
        r"with a successful installment in past 30 days "
        r"at month 12}}{\\text{All first-time SIP starters "
        r"in the cohort}}"
    )

    st.markdown("""
    **Metric decomposition**

    - First-time investor onboarding and first SIP start
    - Payment setup and successful installment execution
    - Continuation through income and life-event changes
    - Recovery after failures or voluntary pauses
    - Successful installment in the 30-day month-12 window

    **Research limitations**

    - Public posts are convenience-sampled, not representative.
    - First-year status is often unknown.
    - Considering a pause is not evidence of cancellation.
    - Setup failures are outside the post-start cohort.
    - Public discussions cannot measure actual retention.
    - Human interviews and product analytics are required.
    """)

    st.caption(
        "Educational research prototype. "
        "No personalized investment advice."
    )
