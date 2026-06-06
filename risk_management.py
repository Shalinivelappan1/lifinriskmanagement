import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats
from scipy.stats import norm
import random

st.set_page_config(
    page_title="Risk Management Lab",
    page_icon="⚠️",
    layout="wide"
)

def pct(x, d=2): return f"{round(x, d)}%"
def currency(x): return f"₹{x:,.2f}"

st.title("⚠️ Experiential Learning Lab: Risk Management")
st.markdown("""
Welcome to the **Risk Management Learning Platform**. This app covers:

- Introduction to Risk Management
- Types of Financial Risk
- Risk Measurement — Variance & Standard Deviation
- Value at Risk (VaR) — Historical, Parametric, Monte Carlo
- Expected Shortfall (CVaR)
- Beta & Systematic Risk
- Credit Risk & Credit Ratings
- Altman Z-Score
- Liquidity Risk
- Operational Risk
- Market Risk — Interest Rate, Currency, Equity
- Risk-Adjusted Return — Sharpe, Treynor, Jensen, Sortino
- Portfolio Risk & Diversification
- Hedging with Derivatives
- Enterprise Risk Management (ERM)
- CAMEL Framework (Banks)
- Basel III & Capital Adequacy
- Indian Risk Management Regulations
- Stress Testing & Scenario Analysis
- Risk Management in Indian Context

through ✅ Interactive calculators ✅ VaR engine ✅ Portfolio risk analyser ✅ Quiz engine ✅ Formula cheat sheet ✅ Case-based learning
""")

menu = st.sidebar.radio("Choose Module", [
    "Introduction to Risk",
    "Types of Financial Risk",
    "Risk Measurement — Variance & SD",
    "Value at Risk (VaR) — Parametric",
    "VaR — Historical Simulation",
    "VaR — Monte Carlo",
    "Expected Shortfall (CVaR)",
    "Beta & Systematic Risk",
    "Portfolio Risk & Diversification",
    "Sharpe, Treynor & Jensen Ratios",
    "Sortino & Calmar Ratios",
    "Credit Risk & Credit Ratings",
    "Altman Z-Score",
    "Liquidity Risk",
    "Interest Rate Risk",
    "Currency (Forex) Risk",
    "Operational Risk",
    "Hedging Strategies",
    "Enterprise Risk Management (ERM)",
    "Stress Testing & Scenario Analysis",
    "CAMEL Framework",
    "Basel III & Capital Adequacy",
    "Indian Risk Regulations",
    "Step-by-Step Solver",
    "AI Hint System",
    "Quiz Engine",
    "Formula Cheat Sheet",
    "Common Student Mistakes",
    "Advanced Quiz Bank",
    "Progress Tracker",
    "Case-Based Learning",
])

# =========================================================
if menu == "Introduction to Risk":
    st.header("📘 Introduction to Risk Management")
    st.markdown("""
## What is Risk?

**Risk** is the possibility of an outcome being different from what was expected —
particularly, the possibility of a **loss** or **unfavourable outcome**.

> "Risk comes from not knowing what you are doing." — Warren Buffett

## Risk vs Uncertainty

| | Risk | Uncertainty |
|---|---|---|
| **Definition** | Measurable — probabilities known | Unmeasurable — probabilities unknown |
| **Example** | Equity portfolio can fall 10% (historical) | COVID pandemic impact (no prior data) |
| **Management** | Hedge, diversify, insure | Scenario planning, resilience |

## Why Manage Risk?

| Purpose | Benefit |
|---|---|
| **Protect capital** | Avoid catastrophic losses |
| **Improve decision making** | Know the risk before committing capital |
| **Regulatory compliance** | Basel III, SEBI, RBI requirements |
| **Enhance returns** | Risk-adjusted returns — better Sharpe ratio |
| **Stakeholder confidence** | Investors, lenders trust managed firms |

## The Risk-Return Tradeoff

$$E(R) = R_f + \\text{Risk Premium}$$

**Higher expected return always comes with higher risk.**
The goal is not to eliminate risk — it's to be **adequately compensated** for the risk taken.
""")

    col1, col2, col3 = st.columns(3)
    col1.info("""
**Financial Risk**
- Market risk
- Credit risk
- Liquidity risk
- Interest rate risk
- Currency risk
""")
    col2.warning("""
**Non-Financial Risk**
- Operational risk
- Strategic risk
- Reputational risk
- Regulatory risk
- Cyber risk
""")
    col3.success("""
**Risk Management Process**
1. Identify risks
2. Measure / quantify
3. Assess & prioritise
4. Mitigate / hedge
5. Monitor & review
""")

# =========================================================
elif menu == "Types of Financial Risk":
    st.header("📊 Types of Financial Risk")

    risk_types = {
        "Market Risk": {
            "description": "Risk of loss due to changes in market prices (equity, interest rates, FX, commodities)",
            "subtypes": ["Equity risk — stock price fall", "Interest rate risk — bond price fall",
                         "Currency risk — FX rate adverse movement", "Commodity risk — price change"],
            "example": "Nifty falls 20% → equity portfolio loses ₹20L",
            "measure": "VaR, Beta, Duration",
            "color": "🔴"
        },
        "Credit Risk": {
            "description": "Risk of loss when a borrower/counterparty fails to meet their obligation",
            "subtypes": ["Default risk", "Downgrade risk", "Counterparty risk", "Concentration risk"],
            "example": "A borrower defaults on a ₹50Cr term loan",
            "measure": "Credit rating, PD, LGD, EAD",
            "color": "🟠"
        },
        "Liquidity Risk": {
            "description": "Risk of being unable to meet financial obligations or sell assets at fair value",
            "subtypes": ["Funding liquidity risk", "Market/asset liquidity risk", "Call/rollover risk"],
            "example": "Bank faces sudden withdrawals, can't sell assets fast enough",
            "measure": "LCR, NSFR, Current ratio, Bid-ask spread",
            "color": "🟡"
        },
        "Operational Risk": {
            "description": "Risk of loss from inadequate/failed processes, people, systems or external events",
            "subtypes": ["Fraud risk", "Technology/cyber risk", "Process failure", "Natural disaster"],
            "example": "Bank's core banking system crashes → ₹5Cr lost",
            "measure": "Loss event data, Key Risk Indicators (KRIs)",
            "color": "🟢"
        },
        "Interest Rate Risk": {
            "description": "Risk that changes in interest rates adversely affect financial positions",
            "subtypes": ["Repricing risk", "Yield curve risk", "Basis risk", "Optionality risk"],
            "example": "RBI raises repo by 50 bps → bond portfolio falls 3%",
            "measure": "Duration, BPV, Modified Duration",
            "color": "🔵"
        },
        "Currency Risk": {
            "description": "Risk of loss due to adverse movements in foreign exchange rates",
            "subtypes": ["Transaction risk", "Translation risk", "Economic risk"],
            "example": "USD/INR moves from 83 to 86 → importer faces extra ₹30L cost",
            "measure": "VaR, Hedge ratio, Forward premium",
            "color": "🟣"
        }
    }

    for risk, details in risk_types.items():
        with st.expander(f"{details['color']} {risk}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Definition:** {details['description']}")
                st.markdown("**Subtypes:**")
                for s in details["subtypes"]:
                    st.markdown(f"  - {s}")
            with col2:
                st.info(f"**Example:** {details['example']}")
                st.success(f"**Measurement:** {details['measure']}")

# =========================================================
elif menu == "Risk Measurement — Variance & SD":
    st.header("📐 Risk Measurement — Variance & Standard Deviation")
    st.markdown("""
## Measuring Risk with Statistics

**Standard Deviation (σ)** is the most common measure of **total risk**.

$$\\sigma = \\sqrt{\\frac{\\sum (R_i - \\bar{R})^2}{n-1}}$$

**Variance = σ²**

**Coefficient of Variation (CV)** = σ / Mean Return (risk per unit of return)
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Return Data Entry")
        data_input = st.text_area(
            "Enter monthly returns (%) comma-separated",
            value="2.5, -1.2, 3.8, -0.5, 4.2, 1.8, -2.1, 3.5, 0.9, -1.8, 2.8, 1.5"
        )
        try:
            returns = [float(x.strip()) for x in data_input.split(",") if x.strip()]
        except:
            returns = [2.5, -1.2, 3.8, -0.5, 4.2, 1.8, -2.1, 3.5, 0.9, -1.8, 2.8, 1.5]

        n = len(returns)
        mean_r = np.mean(returns)
        std_r = np.std(returns, ddof=1)
        var_r = np.var(returns, ddof=1)
        cv = abs(std_r / mean_r) if mean_r != 0 else 0
        skew = stats.skew(returns)
        kurt = stats.kurtosis(returns)

        col_a, col_b = st.columns(2)
        col_a.metric("Mean Return", pct(mean_r))
        col_b.metric("Std Deviation σ", pct(std_r))
        col_a.metric("Variance σ²", round(var_r, 4))
        col_b.metric("CV (Risk/Return)", round(cv, 4))
        col_a.metric("Skewness", round(skew, 4))
        col_b.metric("Kurtosis (Excess)", round(kurt, 4))

    with col2:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=list(range(1, n+1)), y=returns,
            marker_color=['#157A42' if r >= 0 else '#C03B3B' for r in returns],
            name='Monthly Returns'
        ))
        fig.add_hline(y=mean_r, line_dash='dash', line_color='blue',
                      annotation_text=f'Mean={round(mean_r,2)}%')
        fig.add_hline(y=mean_r + std_r, line_dash='dot', line_color='orange',
                      annotation_text=f'+1σ={round(mean_r+std_r,2)}%')
        fig.add_hline(y=mean_r - std_r, line_dash='dot', line_color='orange',
                      annotation_text=f'-1σ={round(mean_r-std_r,2)}%')
        fig.update_layout(title="Monthly Returns with ±1σ Band",
                          xaxis_title="Month", yaxis_title="Return (%)", height=350)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Normal Distribution Probability")
    st.info(f"""
Assuming returns are normally distributed with mean={round(mean_r,2)}% and σ={round(std_r,2)}%:
- **68% probability** returns fall between {round(mean_r-std_r,2)}% and {round(mean_r+std_r,2)}%
- **95% probability** returns fall between {round(mean_r-2*std_r,2)}% and {round(mean_r+2*std_r,2)}%
- **99% probability** returns fall between {round(mean_r-3*std_r,2)}% and {round(mean_r+3*std_r,2)}%
""")

# =========================================================
elif menu == "Value at Risk (VaR) — Parametric":
    st.header("📉 Value at Risk (VaR) — Parametric Method")
    st.markdown("""
## What is VaR?

**Value at Risk (VaR)** answers: *"What is the maximum loss I can expect over a given time period
at a given confidence level?"*

## Parametric VaR Formula

$$VaR = W \\times \\mu \\times T - W \\times \\sigma \\times \\sqrt{T} \\times Z_{\\alpha}$$

**Simplified (1-day, zero mean):**
$$VaR_{1\\text{-day}} = W \\times \\sigma \\times Z_{\\alpha}$$

**Scale to N days:**
$$VaR_{N\\text{-day}} = VaR_{1\\text{-day}} \\times \\sqrt{N}$$

Where:
- **W** = Portfolio value
- **σ** = Daily standard deviation of returns
- **Z_α** = Z-score for confidence level (95%=1.645, 99%=2.326)
- **T** = Time horizon in days
""")

    col1, col2 = st.columns(2)
    with col1:
        portfolio_val = st.number_input("Portfolio Value W (₹)", value=10000000.0, format="%.0f")
        daily_sigma = st.number_input("Daily Std Dev σ (%)", value=1.2)
        confidence = st.selectbox("Confidence Level", [90, 95, 99, 99.9])
        holding_period = st.number_input("Holding Period (days)", value=1, min_value=1, max_value=250)
        annual_return = st.number_input("Annual Mean Return (%)", value=12.0)

    z_scores = {90: 1.282, 95: 1.645, 99: 2.326, 99.9: 3.090}
    z = z_scores[confidence]
    daily_mean = annual_return / 252 / 100
    daily_sigma_dec = daily_sigma / 100

    var_1day_abs = portfolio_val * (daily_sigma_dec * z - daily_mean)
    var_nday_abs = var_1day_abs * np.sqrt(holding_period)
    var_1day_pct = var_1day_abs / portfolio_val * 100
    var_nday_pct = var_nday_abs / portfolio_val * 100

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric(f"1-Day VaR ({confidence}%)", currency(var_1day_abs))
        col_b.metric(f"1-Day VaR %", pct(var_1day_pct))
        col_a.metric(f"{holding_period}-Day VaR ({confidence}%)", currency(var_nday_abs))
        col_b.metric(f"{holding_period}-Day VaR %", pct(var_nday_pct))

    st.success(f"""
**Interpretation:** With {confidence}% confidence, the maximum loss on a ₹{portfolio_val/10000000:.1f}Cr portfolio
over {holding_period} day(s) is **{currency(var_nday_abs)}** ({pct(var_nday_pct)}).

In simple terms: There is only a {100-confidence}% chance of losing more than {currency(var_nday_abs)}.
""")

    # VaR across confidence levels
    conf_levels = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 99.5, 99.9]
    z_vals = [norm.ppf(c/100) for c in conf_levels]
    var_vals = [portfolio_val * daily_sigma_dec * z_v * np.sqrt(holding_period) for z_v in z_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=conf_levels, y=[v/1e6 for v in var_vals],
                             mode='lines+markers', line=dict(color='#C03B3B', width=2)))
    fig.add_vline(x=confidence, line_dash='dash', line_color='blue',
                  annotation_text=f"{confidence}%")
    fig.update_layout(title=f"VaR vs Confidence Level ({holding_period}-day)",
                      xaxis_title="Confidence Level (%)",
                      yaxis_title="VaR (₹ Crore)")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📚 VaR Limitations")
    st.warning("""
**VaR Limitations (Critical for Exams):**
- Does NOT tell you HOW MUCH you can lose beyond VaR (tail risk)
- Assumes normal distribution — real returns have fat tails
- VaR is not sub-additive: VaR(A+B) can > VaR(A) + VaR(B)
- Different methods give different VaR values
- Does not capture liquidity risk or model risk
- Fix: Use Expected Shortfall (CVaR) which captures tail losses
""")

# =========================================================
elif menu == "VaR — Historical Simulation":
    st.header("📊 VaR — Historical Simulation Method")
    st.markdown("""
## Historical Simulation VaR

**No distributional assumptions** — uses actual historical returns.

**Steps:**
1. Collect last N days of returns (typically 250–500 days)
2. Sort returns from worst to best
3. Find the return at the (1−confidence level) percentile
4. VaR = Portfolio Value × |that return|
""")

    col1, col2 = st.columns(2)
    with col1:
        np.random.seed(42)
        n_obs = st.number_input("Number of observations", value=500, min_value=100, step=50)
        portfolio_hs = st.number_input("Portfolio Value (₹)", value=10000000.0, format="%.0f", key="hs_port")
        confidence_hs = st.selectbox("Confidence Level", [90, 95, 99], key="hs_conf")

        # Simulate historical returns with fat tails
        returns_hs = np.concatenate([
            np.random.normal(0.05, 1.2, int(n_obs * 0.95)),
            np.random.normal(-3.0, 2.0, int(n_obs * 0.05))  # fat tail events
        ])
        np.random.shuffle(returns_hs)
        returns_hs = returns_hs[:n_obs]

    sorted_returns = np.sort(returns_hs)
    cutoff_idx = int((1 - confidence_hs/100) * n_obs)
    var_return = sorted_returns[cutoff_idx]
    var_hs = abs(var_return) * portfolio_hs / 100
    cvar_returns = sorted_returns[:cutoff_idx]
    cvar_return = np.mean(cvar_returns)
    cvar_hs = abs(cvar_return) * portfolio_hs / 100

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric(f"VaR ({confidence_hs}%)", currency(var_hs))
        col_b.metric(f"VaR return", pct(var_return))
        col_a.metric("CVaR (Expected Shortfall)", currency(cvar_hs))
        col_b.metric("Worst 1-day loss", pct(sorted_returns[0]))

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=returns_hs, nbinsx=50,
                               marker_color='#174EA6', opacity=0.7, name='Returns'))
    fig.add_vline(x=var_return, line_dash='dash', line_color='red',
                  annotation_text=f"VaR={pct(var_return)}")
    fig.add_vline(x=cvar_return, line_dash='dot', line_color='darkred',
                  annotation_text=f"CVaR={pct(cvar_return)}")
    fig.update_layout(title=f"Historical Return Distribution — {n_obs} observations",
                      xaxis_title="Daily Return (%)", yaxis_title="Frequency")
    st.plotly_chart(fig, use_container_width=True)

    st.info(f"""
**Historical VaR = {currency(var_hs)}** at {confidence_hs}% confidence

Based on {cutoff_idx} worst days out of {n_obs} historical observations.
The {100-confidence_hs}% worst days had returns ≤ {pct(var_return)}.
""")

# =========================================================
elif menu == "VaR — Monte Carlo":
    st.header("🎲 VaR — Monte Carlo Simulation")
    st.markdown("""
## Monte Carlo VaR

Generate thousands of random scenarios from a return distribution,
then find the percentile loss.

**Best for:** Complex portfolios with options, non-linear instruments

**Advantage over parametric:** Captures non-normal distributions and complex payoffs
""")

    col1, col2 = st.columns(2)
    with col1:
        port_mc = st.number_input("Portfolio Value (₹)", value=10000000.0, format="%.0f", key="mc_port")
        mu_mc = st.number_input("Annual Mean Return (%)", value=12.0)
        sigma_mc = st.number_input("Annual Volatility σ (%)", value=20.0)
        conf_mc = st.selectbox("Confidence Level", [90, 95, 99], key="mc_conf")
        n_sims = st.select_slider("Simulations", [1000, 5000, 10000, 50000], value=10000)
        T_mc = st.number_input("Holding Period (days)", value=1, min_value=1, max_value=252)

    np.random.seed(42)
    daily_mu = mu_mc / 100 / 252
    daily_sigma_mc = sigma_mc / 100 / np.sqrt(252)
    sim_returns = np.random.normal(daily_mu * T_mc,
                                    daily_sigma_mc * np.sqrt(T_mc),
                                    n_sims)
    sim_pnl = port_mc * sim_returns
    var_mc = np.percentile(sim_pnl, 100 - conf_mc)
    cvar_mc = sim_pnl[sim_pnl <= var_mc].mean()
    prob_loss = (sim_pnl < 0).mean() * 100

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric(f"MC VaR ({conf_mc}%)", currency(abs(var_mc)))
        col_b.metric("CVaR", currency(abs(cvar_mc)))
        col_a.metric("Prob of any loss", pct(prob_loss))
        col_b.metric("Mean P&L", currency(np.mean(sim_pnl)))

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=sim_pnl/1e5, nbinsx=100,
                               marker_color='#174EA6', opacity=0.7))
    fig.add_vline(x=var_mc/1e5, line_dash='dash', line_color='red',
                  annotation_text=f"VaR=₹{round(abs(var_mc)/1e5,1)}L")
    fig.add_vline(x=cvar_mc/1e5, line_dash='dot', line_color='darkred',
                  annotation_text=f"CVaR=₹{round(abs(cvar_mc)/1e5,1)}L")
    fig.add_vline(x=0, line_color='black')
    fig.update_layout(title=f"Monte Carlo P&L Distribution ({n_sims:,} simulations)",
                      xaxis_title="P&L (₹ Lakhs)", yaxis_title="Frequency")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Expected Shortfall (CVaR)":
    st.header("📉 Expected Shortfall (CVaR / ES)")
    st.markdown("""
## Expected Shortfall (ES) / Conditional VaR

**VaR problem:** VaR says "you won't lose more than X with 95% confidence"
but says NOTHING about losses beyond X.

**ES/CVaR solves this:**
$$ES_{\\alpha} = E[\\text{Loss} \\mid \\text{Loss} > VaR_{\\alpha}]$$

**ES = Average loss in the worst (1−α)% of scenarios**

| Metric | VaR | Expected Shortfall (CVaR) |
|---|---|---|
| **What it measures** | Threshold loss | Average loss beyond threshold |
| **Tail risk** | Ignored | Captured |
| **Sub-additivity** | Not always | Yes (coherent risk measure) |
| **Basel III preference** | Being replaced | Now preferred by Basel III |
| **Interpretation** | Max loss (95%) | Average of worst 5% losses |
""")

    col1, col2 = st.columns(2)
    with col1:
        sigma_es = st.number_input("Daily Volatility σ (%)", value=1.5, key="es_sig")
        port_es = st.number_input("Portfolio Value (₹)", value=10000000.0, format="%.0f", key="es_port")
        conf_es = st.selectbox("Confidence Level", [90, 95, 99], key="es_conf")

    alpha = (100 - conf_es) / 100
    z_var = norm.ppf(1 - alpha)
    var_es = port_es * (sigma_es/100) * z_var
    es_val = port_es * (sigma_es/100) * norm.pdf(z_var) / alpha

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric(f"VaR ({conf_es}%)", currency(var_es))
        col_b.metric(f"ES/CVaR ({conf_es}%)", currency(es_val))
        st.metric("ES/VaR Ratio", round(es_val/var_es, 3),
                  help="ES is always > VaR. Ratio shows tail heaviness.")

    st.success(f"""
**VaR ({conf_es}%) = {currency(var_es)}**: Maximum loss in normal ({conf_es}%) circumstances.

**ES ({conf_es}%) = {currency(es_val)}**: AVERAGE loss in the worst {100-conf_es}% of days.

ES > VaR always. The ratio ES/VaR = {round(es_val/var_es,3)} shows how heavy the tail is.
""")

    st.info("""
**Why Basel III prefers Expected Shortfall:**
- VaR ignores tail events entirely
- ES captures the severity of tail losses
- ES is sub-additive (diversification always helps)
- Better risk aggregation across business lines
- Basel IV moving to ES at 97.5% confidence
""")

# =========================================================
elif menu == "Beta & Systematic Risk":
    st.header("β Beta — Systematic Risk Measure")
    st.markdown("""
## Decomposing Total Risk

$$\\text{Total Risk} = \\text{Systematic Risk} + \\text{Unsystematic Risk}$$

$$\\sigma^2_i = \\beta_i^2 \\sigma^2_M + \\sigma^2_{\\epsilon}$$

**Systematic Risk (β):** Cannot be diversified away — affects all assets
**Unsystematic Risk (ε):** Can be eliminated through diversification

## Beta Formula

$$\\beta_i = \\frac{Cov(R_i, R_M)}{Var(R_M)} = \\rho_{iM} \\times \\frac{\\sigma_i}{\\sigma_M}$$
""")

    col1, col2 = st.columns(2)
    with col1:
        sigma_stock = st.number_input("Stock Std Dev σ_i (%)", value=25.0)
        sigma_market = st.number_input("Market Std Dev σ_M (%)", value=15.0)
        correlation = st.slider("Correlation ρ with market", -1.0, 1.0, 0.75, step=0.01)

    beta = correlation * sigma_stock / sigma_market
    systematic_risk_pct = (beta**2 * sigma_market**2) / sigma_stock**2 * 100
    unsystematic_pct = 100 - systematic_risk_pct
    r_squared = correlation**2

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric("Beta (β)", round(beta, 4))
        col_b.metric("R² (systematic %)", pct(r_squared*100))
        col_a.metric("Systematic Risk %", pct(systematic_risk_pct))
        col_b.metric("Unsystematic Risk %", pct(unsystematic_pct))

    st.latex(f"\\beta = {correlation} \\times \\frac{{{sigma_stock}}}{{{sigma_market}}} = {round(beta,4)}")

    if beta > 1.5:
        st.error(f"β={round(beta,2)} — Highly aggressive. Moves ~{round(beta,2)}x market. High risk!")
    elif beta > 1.0:
        st.warning(f"β={round(beta,2)} — Aggressive. Amplifies market moves. Above-market risk.")
    elif beta > 0.5:
        st.info(f"β={round(beta,2)} — Moderate. Less volatile than market.")
    elif beta > 0:
        st.success(f"β={round(beta,2)} — Defensive. Much less volatile than market.")
    else:
        st.info(f"β={round(beta,2)} — Negative beta! Acts as hedge against market.")

    st.subheader("Beta Interpretation Guide")
    beta_guide = pd.DataFrame({
        "Beta": ["β = 0", "0 < β < 1", "β = 1", "β > 1", "β < 0"],
        "Meaning": ["No market risk (T-bills)", "Less volatile than market (FMCG, Pharma)",
                     "Moves with market (Index fund)", "More volatile (Tech, Small cap)", "Moves opposite to market"],
        "Example (India)": ["Government bond", "ITC, Nestle, Dr Reddy's",
                             "Nifty BeES ETF", "ADANIENT, midcap tech", "Gold (partially)"]
    })
    st.table(beta_guide)

# =========================================================
elif menu == "Portfolio Risk & Diversification":
    st.header("📊 Portfolio Risk & Diversification")
    st.markdown("""
## Two-Asset Portfolio Risk

$$\\sigma_P^2 = w_1^2\\sigma_1^2 + w_2^2\\sigma_2^2 + 2w_1w_2\\sigma_1\\sigma_2\\rho_{12}$$

$$\\sigma_P = \\sqrt{w_1^2\\sigma_1^2 + w_2^2\\sigma_2^2 + 2w_1w_2\\text{Cov}_{12}}$$

**Diversification benefit = when ρ < 1, portfolio risk < weighted average of individual risks**
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Asset 1")
        r1 = st.number_input("Expected Return 1 (%)", value=15.0)
        s1 = st.number_input("Std Dev 1 σ₁ (%)", value=20.0)
        w1 = st.slider("Weight in Asset 1 (%)", 0, 100, 60)

    with col2:
        st.subheader("Asset 2")
        r2 = st.number_input("Expected Return 2 (%)", value=12.0)
        s2 = st.number_input("Std Dev 2 σ₂ (%)", value=15.0)
        rho = st.slider("Correlation ρ₁₂", -1.0, 1.0, 0.3, step=0.05)

    w2 = (100 - w1) / 100
    w1_dec = w1 / 100
    cov12 = rho * s1 * s2
    port_return = w1_dec * r1 + w2 * r2
    port_var = w1_dec**2 * s1**2 + w2**2 * s2**2 + 2 * w1_dec * w2 * cov12
    port_sigma = np.sqrt(port_var)
    weighted_avg_sigma = w1_dec * s1 + w2 * s2
    diversification_benefit = weighted_avg_sigma - port_sigma

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Portfolio Return", pct(port_return))
    col2.metric("Portfolio Sigma", pct(port_sigma))
    col3.metric("Weighted Avg Sigma", pct(weighted_avg_sigma))
    col4.metric("Diversification Benefit", pct(diversification_benefit))

    # Efficient frontier
    weights = np.arange(0, 1.01, 0.01)
    ef_returns = [w*r1 + (1-w)*r2 for w in weights]
    ef_sigmas = [np.sqrt(w**2*s1**2 + (1-w)**2*s2**2 + 2*w*(1-w)*cov12) for w in weights]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ef_sigmas, y=ef_returns, mode='lines',
                             line=dict(color='#174EA6', width=2), name='Efficient Frontier'))
    fig.add_trace(go.Scatter(x=[port_sigma], y=[port_return], mode='markers',
                             marker=dict(size=12, color='red'), name='Your Portfolio'))
    fig.add_trace(go.Scatter(x=[s1, s2], y=[r1, r2], mode='markers+text',
                             text=['Asset 1', 'Asset 2'], textposition='top center',
                             marker=dict(size=10, color='green'), name='Individual Assets'))
    fig.update_layout(title=f"Portfolio Efficient Frontier (ρ={rho})",
                      xaxis_title="Portfolio Sigma (%)", yaxis_title="Portfolio Return (%)")
    st.plotly_chart(fig, use_container_width=True)

    # Show diversification at different correlations
    st.subheader("Diversification Benefit at Different Correlations")
    rho_range = [-1.0, -0.5, 0.0, 0.3, 0.5, 0.7, 1.0]
    div_data = []
    for r in rho_range:
        ps = np.sqrt(w1_dec**2*s1**2 + w2**2*s2**2 + 2*w1_dec*w2*r*s1*s2)
        div_data.append({"Correlation": r, "Portfolio Sigma": pct(ps),
                          "Diversification Benefit": pct(weighted_avg_sigma - ps)})
    st.table(pd.DataFrame(div_data))

# =========================================================
elif menu == "Sharpe, Treynor & Jensen Ratios":
    st.header("📈 Risk-Adjusted Performance Measures")
    st.markdown("""
## Key Risk-Adjusted Return Metrics

| Metric | Formula | Risk Used | Best For |
|---|---|---|---|
| **Sharpe Ratio** | (Rp − Rf) / σp | Total risk (σ) | Undiversified portfolios |
| **Treynor Ratio** | (Rp − Rf) / βp | Systematic risk (β) | Diversified portfolios |
| **Jensen's Alpha** | Rp − [Rf + β(Rm − Rf)] | CAPM benchmark | Excess return over CAPM |
| **M² (Modigliani)** | (Sharpe × σm) + Rf | Total risk adjusted | Comparison with market |
""")

    col1, col2 = st.columns(2)
    with col1:
        rp = st.number_input("Portfolio Return Rp (%)", value=16.0)
        rf = st.number_input("Risk-free Rate Rf (%)", value=7.0)
        rm = st.number_input("Market Return Rm (%)", value=14.0)
        sigma_p = st.number_input("Portfolio Std Dev σp (%)", value=18.0)
        beta_p = st.number_input("Portfolio Beta βp", value=1.1)
        sigma_m = st.number_input("Market Std Dev σm (%)", value=15.0)

    sharpe = (rp - rf) / sigma_p
    treynor = (rp - rf) / beta_p
    capm_return = rf + beta_p * (rm - rf)
    jensen_alpha = rp - capm_return
    m_squared = (sharpe * sigma_m) + rf

    market_sharpe = (rm - rf) / sigma_m
    market_treynor = rm - rf  # beta_m = 1

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric("Sharpe Ratio", round(sharpe, 4))
        col_b.metric("Market Sharpe", round(market_sharpe, 4))
        col_a.metric("Treynor Ratio", round(treynor, 4))
        col_b.metric("Market Treynor", round(market_treynor, 4))
        col_a.metric("Jensen's Alpha", pct(jensen_alpha))
        col_b.metric("M² Measure", pct(m_squared))

    if jensen_alpha > 0:
        st.success(f"✅ Jensen's Alpha = {pct(jensen_alpha)} — Portfolio OUTPERFORMS CAPM-required return!")
    else:
        st.error(f"❌ Jensen's Alpha = {pct(jensen_alpha)} — Portfolio underperforms CAPM expectation")

    if sharpe > market_sharpe:
        st.success(f"✅ Sharpe ({round(sharpe,4)}) > Market Sharpe ({round(market_sharpe,4)}) — Better risk-adjusted performance!")
    else:
        st.warning(f"⚠️ Sharpe ({round(sharpe,4)}) < Market Sharpe ({round(market_sharpe,4)}) — Underperforming on risk-adjusted basis")

    st.subheader("Interpretation Summary")
    interp_df = pd.DataFrame({
        "Metric": ["Sharpe Ratio", "Treynor Ratio", "Jensen's Alpha", "M²"],
        "Your Portfolio": [round(sharpe,4), round(treynor,4), pct(jensen_alpha), pct(m_squared)],
        "Market Benchmark": [round(market_sharpe,4), round(market_treynor,4), "0.00%", pct(rm)],
        "Result": [
            "✅ Better" if sharpe > market_sharpe else "❌ Worse",
            "✅ Better" if treynor > market_treynor else "❌ Worse",
            "✅ Positive α" if jensen_alpha > 0 else "❌ Negative α",
            "✅ Better" if m_squared > rm else "❌ Worse"
        ]
    })
    st.table(interp_df)

# =========================================================
elif menu == "Sortino & Calmar Ratios":
    st.header("📊 Sortino & Calmar Ratios")
    st.markdown("""
## Sortino Ratio

**Improvement over Sharpe:** Only penalises for DOWNSIDE volatility, not upside.

$$\\text{Sortino} = \\frac{R_p - R_{MAR}}{\\sigma_d}$$

Where:
- **R_MAR** = Minimum Acceptable Return (often Rf)
- **σ_d** = Downside deviation (std dev of returns BELOW MAR only)

## Calmar Ratio

$$\\text{Calmar} = \\frac{\\text{Annual Return}}{|\\text{Maximum Drawdown}|}$$

**Maximum Drawdown** = Peak-to-trough decline in portfolio value
""")

    col1, col2 = st.columns(2)
    with col1:
        sample_returns = [3.2, -1.5, 2.8, -0.8, 4.5, 1.2, -3.1, 2.5, -0.5, 3.8, 1.8, -2.2]
        returns_input = st.text_area("Monthly Returns (%)", value=",".join(map(str, sample_returns)))
        try:
            monthly_returns = [float(x.strip()) for x in returns_input.split(",")]
        except:
            monthly_returns = sample_returns

        rf_sortino = st.number_input("MAR / Risk-free Rate (% monthly)", value=0.5)

    annual_return_s = (np.prod([(1+r/100) for r in monthly_returns]) ** (12/len(monthly_returns)) - 1) * 100
    excess_returns = [r - rf_sortino for r in monthly_returns]
    downside_returns = [r for r in excess_returns if r < 0]
    downside_sigma = np.std(downside_returns, ddof=1) if len(downside_returns) > 1 else 0.001
    sortino = (np.mean(excess_returns)) / downside_sigma if downside_sigma > 0 else 0

    # Max drawdown
    cum_returns = np.cumprod([1 + r/100 for r in monthly_returns])
    running_max = np.maximum.accumulate(cum_returns)
    drawdowns = (cum_returns - running_max) / running_max * 100
    max_drawdown = min(drawdowns)
    calmar = annual_return_s / abs(max_drawdown) if max_drawdown != 0 else 0

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric("Annual Return", pct(annual_return_s))
        col_b.metric("Max Drawdown", pct(max_drawdown))
        col_a.metric("Sortino Ratio", round(sortino, 4))
        col_b.metric("Calmar Ratio", round(calmar, 4))
        col_a.metric("Downside Sigma", pct(downside_sigma))

    # Drawdown chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(1, len(monthly_returns)+1)),
                             y=drawdowns, fill='tozeroy',
                             line=dict(color='red'), name='Drawdown'))
    fig.update_layout(title="Portfolio Drawdown Over Time",
                      xaxis_title="Month", yaxis_title="Drawdown (%)")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Credit Risk & Credit Ratings":
    st.header("💳 Credit Risk & Credit Ratings")
    st.markdown("""
## Credit Risk Components

$$\\text{Expected Loss (EL)} = PD \\times LGD \\times EAD$$

| Component | Definition |
|---|---|
| **PD** | Probability of Default — likelihood borrower defaults |
| **LGD** | Loss Given Default — % of exposure lost if default occurs |
| **EAD** | Exposure at Default — amount outstanding at time of default |
| **EL** | Expected Loss = PD × LGD × EAD |

## Credit Rating Scales (India)

| CRISIL | CARE | Moody's | S&P | Meaning |
|---|---|---|---|---|
| AAA | AAA | Aaa | AAA | Highest quality — minimal credit risk |
| AA | AA | Aa | AA | Very high quality |
| A | A | A | A | High quality |
| BBB | BBB | Baa | BBB | Adequate quality (investment grade minimum) |
| BB | BB | Ba | BB | Speculative grade |
| B | B | B | B | Vulnerable |
| C | C | C | C | Near default |
| D | D | D | D | Default |
""")

    col1, col2, col3 = st.columns(3)
    with col1:
        pd_pct = st.number_input("Probability of Default PD (%)", value=2.0)
    with col2:
        lgd_pct = st.number_input("Loss Given Default LGD (%)", value=45.0)
    with col3:
        ead = st.number_input("Exposure at Default EAD (₹ Cr)", value=100.0)

    el = pd_pct/100 * lgd_pct/100 * ead
    recovery_rate = 100 - lgd_pct

    col1, col2, col3 = st.columns(3)
    col1.metric("Expected Loss (EL)", f"₹{round(el,4)} Cr")
    col2.metric("Recovery Rate", pct(recovery_rate))
    col3.metric("EL as % of Exposure", pct(el/ead*100))

    st.subheader("Credit Risk Dashboard")
    ratings_data = pd.DataFrame({
        "Rating": ["AAA", "AA", "A", "BBB", "BB", "B", "CCC"],
        "1-Year PD (%)": [0.01, 0.04, 0.09, 0.20, 1.00, 4.00, 20.00],
        "LGD (typical %)": [35, 38, 40, 45, 50, 55, 65],
        "Spread (bps over G-Sec)": [50, 80, 130, 200, 300, 500, 800],
        "Example (India)": ["TCS, HDFC Bank", "Infosys, Reliance", "Tata Motors",
                             "Adani Enterprises", "High-yield corporate", "Distressed firms", "Pre-default"]
    })
    st.dataframe(ratings_data, use_container_width=True)

# =========================================================
elif menu == "Altman Z-Score":
    st.header("📊 Altman Z-Score — Predicting Bankruptcy")
    st.markdown("""
## Altman Z-Score (1968)

Used to predict the probability of bankruptcy using financial ratios.

## Formula

$$Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5$$

| Variable | Formula | What It Measures |
|---|---|---|
| **X₁** | Working Capital / Total Assets | Liquidity |
| **X₂** | Retained Earnings / Total Assets | Leverage / Accumulated profit |
| **X₃** | EBIT / Total Assets | Profitability / Asset productivity |
| **X₄** | Market Value of Equity / Book Value of Debt | Solvency / Financial structure |
| **X₅** | Revenue / Total Assets | Asset turnover / Efficiency |

## Interpretation

| Z-Score | Zone | Interpretation |
|---|---|---|
| **Z > 2.99** | Safe Zone | Low bankruptcy risk |
| **1.81 < Z < 2.99** | Grey Zone | Borderline — caution |
| **Z < 1.81** | Distress Zone | High bankruptcy risk |
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Enter Financial Data (₹ Crore)")
        working_capital = st.number_input("Working Capital (CA - CL)", value=150.0)
        retained_earnings = st.number_input("Retained Earnings", value=200.0)
        ebit_z = st.number_input("EBIT", value=120.0)
        market_cap = st.number_input("Market Capitalisation", value=800.0)
        total_debt = st.number_input("Total Debt", value=400.0)
        revenue_z = st.number_input("Revenue", value=600.0)
        total_assets = st.number_input("Total Assets", value=700.0)

    X1 = working_capital / total_assets
    X2 = retained_earnings / total_assets
    X3 = ebit_z / total_assets
    X4 = market_cap / total_debt if total_debt > 0 else 0
    X5 = revenue_z / total_assets
    Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

    with col2:
        ratios_df = pd.DataFrame({
            "Variable": ["X₁ (WC/TA)", "X₂ (RE/TA)", "X₃ (EBIT/TA)", "X₄ (MktCap/Debt)", "X₅ (Rev/TA)"],
            "Value": [round(X1,4), round(X2,4), round(X3,4), round(X4,4), round(X5,4)],
            "Weight": [1.2, 1.4, 3.3, 0.6, 1.0],
            "Contribution": [round(1.2*X1,4), round(1.4*X2,4), round(3.3*X3,4),
                              round(0.6*X4,4), round(1.0*X5,4)]
        })
        st.table(ratios_df)
        st.metric("**Altman Z-Score**", round(Z, 4))

    if Z > 2.99:
        st.success(f"✅ Z = {round(Z,4)} — SAFE ZONE. Low bankruptcy risk.")
    elif Z > 1.81:
        st.warning(f"⚠️ Z = {round(Z,4)} — GREY ZONE. Monitor closely.")
    else:
        st.error(f"❌ Z = {round(Z,4)} — DISTRESS ZONE. High bankruptcy risk!")

    st.latex(f"Z = 1.2({round(X1,3)}) + 1.4({round(X2,3)}) + 3.3({round(X3,3)}) + 0.6({round(X4,3)}) + 1.0({round(X5,3)}) = {round(Z,4)}")

# =========================================================
elif menu == "Liquidity Risk":
    st.header("💧 Liquidity Risk")
    st.markdown("""
## Types of Liquidity Risk

| Type | Definition | Example |
|---|---|---|
| **Funding Liquidity** | Inability to meet payment obligations | Bank run; bond rollover failure |
| **Market Liquidity** | Unable to sell asset at fair price quickly | Illiquid bonds in crisis |
| **Call/Rollover Risk** | Short-term borrowing cannot be renewed | CP rollover failure (IL&FS 2018) |

## Key Liquidity Metrics

**Liquidity Coverage Ratio (LCR)** — Basel III requirement:
$$LCR = \\frac{\\text{High Quality Liquid Assets (HQLA)}}{\\text{Net Cash Outflows (30-day stress)}} \\geq 100\\%$$

**Net Stable Funding Ratio (NSFR)**:
$$NSFR = \\frac{\\text{Available Stable Funding}}{\\text{Required Stable Funding}} \\geq 100\\%$$
""")

    col1, col2 = st.columns(2)
    with col1:
        hqla = st.number_input("HQLA (₹ Cr)", value=500.0, help="Cash + Gov Bonds + Level 1 assets")
        net_outflows_30d = st.number_input("Net Cash Outflows 30-day stress (₹ Cr)", value=400.0)
        current_assets_liq = st.number_input("Current Assets (₹ Cr)", value=800.0)
        current_liab_liq = st.number_input("Current Liabilities (₹ Cr)", value=600.0)
        inventory_liq = st.number_input("Inventory (₹ Cr)", value=200.0)
    with col2:
        lcr = hqla / net_outflows_30d * 100 if net_outflows_30d > 0 else 0
        current_ratio_liq = current_assets_liq / current_liab_liq
        quick_ratio_liq = (current_assets_liq - inventory_liq) / current_liab_liq
        cash_ratio = (current_assets_liq - inventory_liq - (current_assets_liq * 0.3)) / current_liab_liq

        col_a, col_b = st.columns(2)
        col_a.metric("LCR", pct(lcr), "Min 100% (RBI)")
        col_b.metric("Current Ratio", round(current_ratio_liq, 2), "Min 1.0x")
        col_a.metric("Quick Ratio", round(quick_ratio_liq, 2), "Min 0.8x")
        col_b.metric("Cash Ratio", round(cash_ratio, 2))

    if lcr >= 100:
        st.success(f"✅ LCR = {pct(lcr)} — Bank has adequate liquid assets for 30-day stress")
    else:
        st.error(f"❌ LCR = {pct(lcr)} — Below 100%! Regulatory breach. Need more HQLA!")

    st.info("""
**Indian Liquidity Crisis Examples:**
- **IL&FS (2018):** Infrastructure NBFC that couldn't roll over short-term CP/NCD → ₹90,000Cr default cascade
- **YES Bank (2020):** Rapid deterioration in asset quality → RBI imposed moratorium
- **DHFL (2019):** Housing finance company defaulted on CP → contagion across NBFC sector
- **Lesson:** NEVER fund long-term assets with short-term liabilities without adequate liquidity buffer
""")

# =========================================================
elif menu == "Interest Rate Risk":
    st.header("📈 Interest Rate Risk")
    st.markdown("""
## Interest Rate Risk Measurement

**Duration** measures sensitivity of bond price to interest rate changes.

$$\\% \\Delta P \\approx -D_{mod} \\times \\Delta y$$

$$D_{mod} = \\frac{D_{mac}}{1+y}$$

**BPV (Basis Point Value):** Change in price for 1 basis point (0.01%) change in yield

$$BPV = \\frac{D_{mod} \\times P}{10000}$$
""")

    col1, col2 = st.columns(2)
    with col1:
        face_ir = st.number_input("Face Value (₹)", value=1000.0)
        coupon_ir = st.number_input("Coupon Rate (%)", value=8.0)
        ytm_ir = st.number_input("Current YTM (%)", value=9.0)
        maturity_ir = st.number_input("Years to Maturity", value=5.0)
        portfolio_bonds = st.number_input("Portfolio Size (₹ Cr)", value=100.0)

    coupon_payment = face_ir * coupon_ir / 100
    r_ir = ytm_ir / 100

    # Bond price and duration
    price_ir = sum(coupon_payment / (1+r_ir)**t for t in range(1, int(maturity_ir)+1)) + \
               face_ir / (1+r_ir)**maturity_ir
    mac_dur = sum(t * (coupon_payment/(1+r_ir)**t) / price_ir for t in range(1, int(maturity_ir)+1)) + \
              maturity_ir * (face_ir/(1+r_ir)**maturity_ir) / price_ir
    mod_dur = mac_dur / (1 + r_ir)
    bpv = mod_dur * price_ir / 10000
    bpv_portfolio = mod_dur * portfolio_bonds * 1e7 / 10000

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric("Bond Price", currency(price_ir))
        col_b.metric("Macaulay Duration", f"{round(mac_dur, 4)} years")
        col_a.metric("Modified Duration", round(mod_dur, 4))
        col_b.metric("BPV (per bond)", f"₹{round(bpv, 4)}")
        col_a.metric("Portfolio BPV (1bp)", currency(bpv_portfolio))

    st.subheader("Interest Rate Scenario Analysis")
    rate_changes = [-200, -100, -50, -25, 0, 25, 50, 100, 200]
    ir_data = []
    for bps in rate_changes:
        dy = bps / 10000
        price_change_pct = -mod_dur * dy * 100
        portfolio_change = portfolio_bonds * price_change_pct / 100
        ir_data.append({
            "Rate Change (bps)": bps,
            "Price Change %": pct(price_change_pct),
            "Portfolio Impact (₹ Cr)": round(portfolio_change, 4)
        })
    df_ir = pd.DataFrame(ir_data)
    st.dataframe(df_ir, use_container_width=True)

    st.warning(f"""
⚠️ **Interest Rate Risk:**
Modified Duration = {round(mod_dur,2)} years.
If RBI raises rates by **100 bps (1%)**, portfolio falls by approximately **{pct(mod_dur)}** = ₹{round(portfolio_bonds*mod_dur/100,2)} Cr loss.
**Hedge:** Sell bond futures or enter interest rate swaps (pay fixed, receive floating).
""")

# =========================================================
elif menu == "Currency (Forex) Risk":
    st.header("💱 Currency (Forex) Risk")
    st.markdown("""
## Types of Forex Risk

| Type | Definition | Example |
|---|---|---|
| **Transaction Risk** | FX rate change before cash settlement | Exporter invoices in USD, INR appreciates before payment |
| **Translation Risk** | Converting foreign subsidiary financials | MNC's USD subsidiary shows lower INR profit when USD weakens |
| **Economic Risk** | Long-term impact on firm's competitive position | Persistent INR depreciation helps IT exporters |

## Hedging Currency Risk

1. **Forward contract** — lock in FX rate today for future payment
2. **Futures** — exchange-traded forward (USD/INR on NSE)
3. **Options** — buy the right to exchange at a specific rate
4. **Natural hedge** — match revenue and cost currency
5. **Money market hedge** — borrow/invest to lock in effective rate
""")

    col1, col2 = st.columns(2)
    with col1:
        exposure_usd = st.number_input("Foreign Currency Exposure (USD)", value=1000000.0)
        spot_rate = st.number_input("Current USD/INR Spot", value=83.50)
        forward_rate = st.number_input("3-Month Forward Rate (USD/INR)", value=84.20)
        expected_spot = st.number_input("Expected Spot at Settlement", value=82.50)
        hedge_type = st.radio("Hedging Strategy", ["No Hedge", "Forward Hedge", "Options Hedge"])

    inr_exposure_spot = exposure_usd * spot_rate
    inr_at_expected = exposure_usd * expected_spot
    inr_at_forward = exposure_usd * forward_rate

    if hedge_type == "No Hedge":
        outcome = inr_at_expected
        hedge_gain_loss = outcome - inr_exposure_spot
    elif hedge_type == "Forward Hedge":
        outcome = inr_at_forward
        hedge_gain_loss = outcome - inr_at_expected
    else:  # Options
        option_premium = exposure_usd * 0.005  # 0.5% premium
        outcome = max(inr_at_forward, inr_at_expected) - option_premium
        hedge_gain_loss = outcome - inr_at_expected

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric("INR at Spot Rate", currency(inr_exposure_spot))
        col_b.metric("INR at Forward", currency(inr_at_forward))
        col_a.metric("INR at Expected Spot", currency(inr_at_expected))
        col_b.metric("Outcome with Hedge", currency(outcome))
        st.metric("Hedge Gain / Loss", currency(hedge_gain_loss))

    if hedge_type == "Forward Hedge":
        if inr_at_forward > inr_at_expected:
            st.success(f"✅ Forward hedge gained {currency(hedge_gain_loss)} vs leaving unhedged!")
        else:
            st.info(f"Forward hedge: lost {currency(abs(hedge_gain_loss))} vs spot rate — but currency risk eliminated!")

# =========================================================
elif menu == "Operational Risk":
    st.header("⚙️ Operational Risk")
    st.markdown("""
## What is Operational Risk?

**Operational risk** is the risk of loss from inadequate or failed internal processes,
people, systems, or from external events.

**Basel III definition:** Includes legal risk but excludes strategic and reputational risk.

## Loss Event Types (Basel categories)

| Category | Examples | Typical Impact |
|---|---|---|
| **Internal Fraud** | Rogue trader, employee theft, account manipulation | Very High |
| **External Fraud** | Cyber attack, card fraud, phishing | High |
| **Employment Practices** | Discrimination, workplace injury | Medium |
| **Clients & Products** | Mis-selling, fiduciary breach | High |
| **Damage to Physical Assets** | Fire, natural disaster | Medium |
| **Business Disruption** | System outages, IT failure | High |
| **Process Failures** | Settlement errors, transaction mistakes | Medium |

## Key Risk Indicators (KRIs)

| KRI | Trigger Level | Action |
|---|---|---|
| System downtime (hrs/month) | > 4 hours | Escalate to IT risk |
| Failed transactions (%) | > 0.1% | Process review |
| Staff turnover (%) | > 25% | HR investigation |
| Customer complaints | > 50/month | Quality review |
| Audit findings | > 3 critical | Remediation plan |
""")

    st.subheader("🔢 Operational Risk Capital (Basel — Basic Indicator Approach)")
    st.markdown("""
$$\\text{Capital Charge} = \\alpha \\times \\text{Gross Income (3-year average)}$$

Where **α = 15%** (Basic Indicator Approach)
""")

    col1, col2, col3 = st.columns(3)
    gi_1 = col1.number_input("Gross Income Year 1 (₹ Cr)", value=500.0)
    gi_2 = col2.number_input("Gross Income Year 2 (₹ Cr)", value=550.0)
    gi_3 = col3.number_input("Gross Income Year 3 (₹ Cr)", value=600.0)

    avg_gi = (gi_1 + gi_2 + gi_3) / 3
    op_risk_capital = avg_gi * 0.15
    st.metric("Operational Risk Capital Charge (BIA)", f"₹{round(op_risk_capital,2)} Cr")
    st.info(f"15% × Average Gross Income ₹{round(avg_gi,2)} Cr = ₹{round(op_risk_capital,2)} Cr capital required")

# =========================================================
elif menu == "Hedging Strategies":
    st.header("🛡️ Hedging Strategies in Risk Management")
    st.markdown("""
## Overview of Hedging Instruments

| Risk Type | Hedging Instrument | Example |
|---|---|---|
| **Interest Rate Risk** | Interest Rate Swaps, Bond Futures | Pay fixed/receive floating swap |
| **Currency Risk** | Forward contracts, Currency Futures, Options | USD/INR forward for exporters |
| **Equity Risk** | Index Futures, Put Options, Short ETF | Short Nifty futures to hedge portfolio |
| **Commodity Risk** | Commodity Futures, Options | MCX Gold futures for jeweller |
| **Credit Risk** | Credit Default Swaps (CDS) | Buy CDS protection on corporate bond |

## Hedge Effectiveness

$$HE = 1 - \\frac{\\sigma^2_{\\text{hedged}}}{\\sigma^2_{\\text{unhedged}}}$$

**Perfect hedge:** HE = 1.0 (100%) — rarely achieved in practice
**Good hedge:** HE > 0.8 (80%)
""")

    hedge_type_sel = st.selectbox("Analyse a Hedging Strategy:", [
        "Equity Portfolio — Beta Hedge with Nifty Futures",
        "Bond Portfolio — Interest Rate Swap",
        "Currency Risk — Export Forward Hedge",
        "Commodity — Gold Futures Hedge",
    ])

    if hedge_type_sel == "Equity Portfolio — Beta Hedge with Nifty Futures":
        col1, col2 = st.columns(2)
        with col1:
            port_val_h = st.number_input("Portfolio Value (₹ Cr)", value=10.0)
            beta_h = st.number_input("Portfolio Beta", value=1.3)
            nifty_level = st.number_input("Nifty Futures Price", value=22000.0)
            target_beta = st.number_input("Target Beta (0=full hedge)", value=0.0)

        lot = 25
        n_contracts = (target_beta - beta_h) * port_val_h * 1e7 / (nifty_level * lot)
        st.metric("Contracts to SELL", round(abs(n_contracts), 0))
        st.success(f"""
Sell {round(abs(n_contracts),0):.0f} Nifty futures contracts (short) to reduce beta from {beta_h} to {target_beta}.

If Nifty falls 10%:
- Unhedged portfolio loss: {round(beta_h*10,1)}% = ₹{round(beta_h*10*port_val_h/100,2)} Cr
- After hedge (β={target_beta}): ~{round(target_beta*10,1)}% loss
""")

    elif hedge_type_sel == "Currency Risk — Export Forward Hedge":
        col1, col2 = st.columns(2)
        with col1:
            export_usd = st.number_input("USD Export Receivable", value=500000.0)
            spot_h = st.number_input("Current Spot USD/INR", value=83.50)
            fwd_h = st.number_input("3M Forward Rate", value=84.20)
        with col2:
            actual_spot = st.number_input("Actual Spot at Realisation", value=82.00)
            inr_unhedged = export_usd * actual_spot
            inr_hedged = export_usd * fwd_h
            hedge_benefit = inr_hedged - inr_unhedged
            st.metric("INR Received (Unhedged)", currency(inr_unhedged))
            st.metric("INR Received (Forward Hedged)", currency(inr_hedged))
            st.metric("Hedge Benefit", currency(hedge_benefit))

# =========================================================
elif menu == "Enterprise Risk Management (ERM)":
    st.header("🏢 Enterprise Risk Management (ERM)")
    st.markdown("""
## What is ERM?

**Enterprise Risk Management** is a firm-wide, integrated approach to identifying,
assessing, and managing ALL types of risks — strategic, operational, financial.

## COSO ERM Framework

The Committee of Sponsoring Organisations (COSO) ERM Framework has 8 components:

1. **Internal Environment** — Risk culture, governance, risk appetite
2. **Objective Setting** — Strategic goals aligned with risk appetite
3. **Event Identification** — What can go wrong?
4. **Risk Assessment** — Probability × Impact
5. **Risk Response** — Avoid, Reduce, Share, Accept
6. **Control Activities** — Policies, limits, authorisations
7. **Information & Communication** — Reporting structure
8. **Monitoring** — Ongoing review of risk management effectiveness

## Risk Response Strategies

| Response | When to Use | Example |
|---|---|---|
| **Avoid** | Risk too high / unacceptable | Exit a market with extreme political risk |
| **Reduce** | Partial mitigation possible | Add credit limits; better processes |
| **Share/Transfer** | Cost-effective to pass risk | Buy insurance; enter CDS |
| **Accept** | Risk within appetite; cost of hedge too high | Accept small operational losses |

## Risk Appetite vs Risk Tolerance

| Term | Definition |
|---|---|
| **Risk Appetite** | Amount of risk the firm is WILLING to take to achieve objectives |
| **Risk Tolerance** | Maximum variation from risk appetite the firm can absorb |
| **Risk Capacity** | Maximum risk the firm CAN bear without threatening solvency |
""")

    st.subheader("🔢 Risk Heat Map Builder")
    st.markdown("Rate your key risks:")

    risks_erm = [
        ("Credit Risk", 3, 4),
        ("Liquidity Risk", 2, 5),
        ("Market Risk", 3, 3),
        ("Operational Risk", 4, 2),
        ("Regulatory Risk", 2, 4),
        ("Cyber Risk", 3, 4),
    ]

    risk_names = [r[0] for r in risks_erm]
    probabilities = [r[1] for r in risks_erm]
    impacts = [r[2] for r in risks_erm]
    risk_scores = [p*i for p,i in zip(probabilities, impacts)]

    fig = go.Figure()
    colors_erm = ['#C03B3B' if s>=12 else '#F5A623' if s>=6 else '#157A42' for s in risk_scores]
    fig.add_trace(go.Scatter(
        x=probabilities, y=impacts, mode='markers+text',
        text=risk_names, textposition='top center',
        marker=dict(size=[r*5 for r in risk_scores], color=colors_erm, opacity=0.7),
    ))
    fig.update_layout(title="Risk Heat Map (Probability vs Impact)",
                      xaxis_title="Probability (1-5)",
                      yaxis_title="Impact (1-5)",
                      xaxis=dict(range=[0,6]), yaxis=dict(range=[0,6]))
    for thresh_x, thresh_y, color, label in [(3,3,'orange','Monitor'),(4,4,'red','Critical')]:
        fig.add_shape(type='rect', x0=thresh_x, y0=thresh_y, x1=6, y1=6,
                      fillcolor=color, opacity=0.1, line_width=0)
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Stress Testing & Scenario Analysis":
    st.header("🔥 Stress Testing & Scenario Analysis")
    st.markdown("""
## Stress Testing

**Stress testing** evaluates a firm's resilience under extreme but plausible adverse scenarios.

**Regulatory requirement:** RBI mandates stress testing for all scheduled commercial banks.

## Types of Stress Tests

| Type | Description |
|---|---|
| **Sensitivity Analysis** | Change ONE variable at a time |
| **Scenario Analysis** | Change MULTIPLE variables simultaneously (Bull/Base/Bear) |
| **Reverse Stress Test** | Start from failure point, work backwards to identify causes |
| **Historical Scenario** | Apply historical crisis scenarios (2008, COVID, Dotcom) |
""")

    st.subheader("🔢 Portfolio Stress Test Simulator")

    col1, col2 = st.columns(2)
    with col1:
        equity_alloc = st.number_input("Equity Allocation (₹ Cr)", value=50.0)
        bond_alloc = st.number_input("Bond Allocation (₹ Cr)", value=30.0)
        cash_alloc = st.number_input("Cash/Liquid (₹ Cr)", value=20.0)
        portfolio_total = equity_alloc + bond_alloc + cash_alloc

    scenarios_st = {
        "Normal Year": {"equity": 12, "bonds": 7, "cash": 6},
        "Bull Market": {"equity": 35, "bonds": 5, "cash": 6},
        "Bear Market 2022-type": {"equity": -25, "bonds": -5, "cash": 6},
        "COVID Crash (Mar 2020)": {"equity": -38, "bonds": 8, "cash": 6},
        "2008 Global Crisis": {"equity": -55, "bonds": 15, "cash": 6},
        "Dotcom Bust 2000": {"equity": -45, "bonds": 12, "cash": 6},
        "Rising Rates (100bps)": {"equity": -8, "bonds": -6, "cash": 7},
        "INR depreciation 10%": {"equity": 5, "bonds": -2, "cash": 6},
    }

    stress_results = []
    for scenario, returns in scenarios_st.items():
        eq_pnl = equity_alloc * returns["equity"] / 100
        bond_pnl = bond_alloc * returns["bonds"] / 100
        cash_pnl = cash_alloc * returns["cash"] / 100
        total_pnl = eq_pnl + bond_pnl + cash_pnl
        total_return = total_pnl / portfolio_total * 100
        stress_results.append({
            "Scenario": scenario,
            "Equity P&L (₹Cr)": round(eq_pnl,2),
            "Bond P&L (₹Cr)": round(bond_pnl,2),
            "Total P&L (₹Cr)": round(total_pnl,2),
            "Total Return %": round(total_return,1)
        })

    df_stress = pd.DataFrame(stress_results)
    st.dataframe(df_stress, use_container_width=True)

    fig = go.Figure(go.Bar(
        x=df_stress["Scenario"],
        y=df_stress["Total P&L (₹Cr)"],
        marker_color=['#157A42' if v > 0 else '#C03B3B' for v in df_stress["Total P&L (₹Cr)"]],
    ))
    fig.update_layout(title="Portfolio P&L Under Stress Scenarios",
                      xaxis_title="Scenario", yaxis_title="P&L (₹ Crore)",
                      xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "CAMEL Framework":
    st.header("🏦 CAMEL Framework — Bank Risk Assessment")
    st.markdown("""
## CAMEL Rating System

Used by **RBI** and banking regulators worldwide to assess bank health.

| Component | What It Measures | Key Ratios |
|---|---|---|
| **C** — Capital Adequacy | Buffer against losses | CRAR, Tier 1 ratio |
| **A** — Asset Quality | Quality of loan book | NPA%, PCR, Slippage ratio |
| **M** — Management Quality | Governance & efficiency | CIR, ROA, Compliance |
| **E** — Earnings | Profitability | ROA, ROE, NIM, NNPA |
| **L** — Liquidity | Ability to meet obligations | LCR, NSFR, CD ratio |

*(Some versions add **S** = Sensitivity to market risk → CAMELS)*
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Enter Bank Data")
        tier1_capital = st.number_input("Tier 1 Capital (₹ Cr)", value=5000.0)
        total_capital = st.number_input("Total Capital (₹ Cr)", value=6500.0)
        rwa = st.number_input("Risk-Weighted Assets (₹ Cr)", value=50000.0)
        gross_npa = st.number_input("Gross NPA (₹ Cr)", value=2500.0)
        total_advances = st.number_input("Total Advances (₹ Cr)", value=40000.0)
        provisions = st.number_input("NPA Provisions (₹ Cr)", value=1800.0)
        net_interest_income = st.number_input("Net Interest Income (₹ Cr)", value=2000.0)
        total_assets_bank = st.number_input("Total Assets (₹ Cr)", value=80000.0)
        pat_bank = st.number_input("PAT (₹ Cr)", value=800.0)
        net_worth_bank = st.number_input("Net Worth (₹ Cr)", value=8000.0)
        total_deposits = st.number_input("Total Deposits (₹ Cr)", value=65000.0)

    with col2:
        crar = total_capital / rwa * 100
        tier1_ratio = tier1_capital / rwa * 100
        gnpa_ratio = gross_npa / total_advances * 100
        net_npa = gross_npa - provisions
        nnpa_ratio = net_npa / total_advances * 100
        pcr = provisions / gross_npa * 100 if gross_npa > 0 else 0
        nim = net_interest_income / total_assets_bank * 100
        roa = pat_bank / total_assets_bank * 100
        roe_bank = pat_bank / net_worth_bank * 100
        cd_ratio = total_advances / total_deposits * 100

        camel_df = pd.DataFrame({
            "CAMEL Component": ["C — CRAR", "C — Tier 1 Ratio",
                                 "A — Gross NPA %", "A — Net NPA %", "A — PCR",
                                 "E — ROA", "E — ROE", "E — NIM",
                                 "L — Credit-Deposit Ratio"],
            "Value": [pct(crar), pct(tier1_ratio),
                       pct(gnpa_ratio), pct(nnpa_ratio), pct(pcr),
                       pct(roa), pct(roe_bank), pct(nim),
                       pct(cd_ratio)],
            "RBI Benchmark": ["≥11.5%","≥9.5%","<3% (PSBs)","<1.5%","≥75%",
                               ">1%",">12%",">2.5%","60-75%"],
            "Status": [
                "✅" if crar>=11.5 else "❌",
                "✅" if tier1_ratio>=9.5 else "❌",
                "✅" if gnpa_ratio<3 else "⚠️" if gnpa_ratio<7 else "❌",
                "✅" if nnpa_ratio<1.5 else "❌",
                "✅" if pcr>=75 else "⚠️",
                "✅" if roa>1 else "❌",
                "✅" if roe_bank>12 else "⚠️",
                "✅" if nim>2.5 else "⚠️",
                "✅" if 60<=cd_ratio<=75 else "⚠️"
            ]
        })
        st.dataframe(camel_df, use_container_width=True)

# =========================================================
elif menu == "Basel III & Capital Adequacy":
    st.header("🏛️ Basel III & Capital Adequacy")
    st.markdown("""
## Basel III Capital Requirements

| Capital Type | Minimum Requirement | India (RBI) |
|---|---|---|
| **Common Equity Tier 1 (CET1)** | 4.5% | 5.5% |
| **Tier 1 Capital** | 6.0% | 7.0% |
| **Total Capital (CRAR)** | 8.0% | 9.0% + 2.5% CCB = 11.5% |
| **Capital Conservation Buffer (CCB)** | 2.5% | 2.5% |
| **G-SIB Surcharge** | 1-3.5% | N/A (D-SIB: 0.2-0.8%) |

## Risk-Weighted Assets (RWA)

$$CRAR = \\frac{\\text{Eligible Capital}}{\\text{Risk-Weighted Assets}} \\times 100$$

**Risk Weights (Standard Approach):**
- Government securities: 0%
- AAA corporates: 20%
- Retail loans: 75%
- Residential mortgages: 35-75%
- Unsecured personal loans: 100%
- NPA: 150%
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Capital Adequacy Calculator")
        cet1_cap = st.number_input("CET1 Capital (₹ Cr)", value=4000.0)
        at1_cap = st.number_input("Additional Tier 1 (₹ Cr)", value=500.0)
        tier2_cap = st.number_input("Tier 2 Capital (₹ Cr)", value=1500.0)

        st.subheader("RWA by Category")
        govt_bonds = st.number_input("Govt Securities (₹ Cr)", value=15000.0)
        aaa_corporate = st.number_input("AAA Corporate Bonds (₹ Cr)", value=5000.0)
        retail_loans = st.number_input("Retail Loans (₹ Cr)", value=20000.0)
        home_loans = st.number_input("Home Loans (₹ Cr)", value=10000.0)
        npa_loans = st.number_input("NPA Loans (₹ Cr)", value=2000.0)

    total_capital_b3 = cet1_cap + at1_cap + tier2_cap
    tier1_b3 = cet1_cap + at1_cap
    rwa_calc = (govt_bonds * 0 + aaa_corporate * 0.20 +
                retail_loans * 0.75 + home_loans * 0.50 + npa_loans * 1.50)

    crar_calc = total_capital_b3 / rwa_calc * 100 if rwa_calc > 0 else 0
    tier1_ratio_calc = tier1_b3 / rwa_calc * 100 if rwa_calc > 0 else 0
    cet1_ratio_calc = cet1_cap / rwa_calc * 100 if rwa_calc > 0 else 0

    with col2:
        col_a, col_b = st.columns(2)
        col_a.metric("CET1 Ratio", pct(cet1_ratio_calc), "Min 5.5% (RBI)")
        col_b.metric("Tier 1 Ratio", pct(tier1_ratio_calc), "Min 7% (RBI)")
        col_a.metric("CRAR", pct(crar_calc), "Min 11.5% with CCB")
        col_b.metric("Total RWA", f"₹{round(rwa_calc,0):,.0f} Cr")

        if crar_calc >= 11.5:
            st.success(f"✅ CRAR={pct(crar_calc)} — Well-capitalised! Exceeds Basel III + CCB requirement")
        elif crar_calc >= 9.0:
            st.warning(f"⚠️ CRAR={pct(crar_calc)} — Adequately capitalised but below CCB")
        else:
            st.error(f"❌ CRAR={pct(crar_calc)} — Under-capitalised! Regulatory action required")

# =========================================================
elif menu == "Indian Risk Regulations":
    st.header("🇮🇳 Indian Risk Management Regulations")
    st.markdown("""
## Key Regulators & Their Risk Mandates

| Regulator | Institution Type | Key Risk Focus |
|---|---|---|
| **RBI** | Banks, NBFCs | Credit risk, liquidity risk, capital adequacy |
| **SEBI** | Brokers, AMCs, Exchanges | Market risk, operational risk, investor protection |
| **IRDAI** | Insurance companies | Insurance risk, solvency, investment limits |
| **PFRDA** | Pension funds | Investment risk, longevity risk |
| **IBBI** | Insolvency practitioners | Credit risk in resolution |

## RBI Risk Management Guidelines

| Regulation | Year | Requirement |
|---|---|---|
| **Basel III India rollout** | 2013-2019 | CRAR ≥ 11.5% (incl. CCB) |
| **ICAAP** | Ongoing | Internal Capital Adequacy Assessment Process |
| **SREP** | Ongoing | Supervisory Review & Evaluation Process |
| **ALM Guidelines** | 1999-updated | Asset-Liability Management for liquidity risk |
| **Market Risk Capital** | Updated | Standardised + IMA approaches |
| **Cyber Risk Framework** | 2016 | IT governance and cyber security |
| **Climate Risk** | 2023 | Pilot disclosures on climate-related risks |

## SEBI Risk Management — Brokers & Exchanges

| Rule | Requirement |
|---|---|
| **Upfront Margin (SEBI 2021)** | 100% margin before trade |
| **VAR Margin** | Daily VaR-based margin on equity |
| **SPAN Margin** | Portfolio-based margin for F&O |
| **Peak Margin Reporting** | Intra-day margin surveillance |
| **Stress Test** | Weekly stress test by clearing houses |

## NBFC Risk Framework (IL&FS Lessons)
- ALM mismatch monitoring: RBI circular 2019
- Liquidity risk management framework mandatory
- Interoperability risk disclosure
- Concentration risk limits

## India-Specific Risk Events

| Event | Year | Risk Type | Impact |
|---|---|---|---|
| UTI collapse | 2001 | Market + Credit risk | Retail investors lost; govt bailout |
| Satyam fraud | 2009 | Operational (fraud) | ₹7,000Cr accounting fraud |
| IL&FS default | 2018 | Credit + Liquidity | ₹90,000Cr; NBFC crisis |
| YES Bank AT1 | 2020 | Credit + Regulatory | AT1 bonds written off; moratorium |
| COVID crash | 2020 | Market risk | Nifty fell 38% in 40 days |
| Adani short | 2023 | Reputational + Market | ₹10L Cr market cap loss in days |
""")

# =========================================================
elif menu == "Step-by-Step Solver":
    st.header("🧠 Step-by-Step Solver")
    problem = st.selectbox("Choose Problem", [
        "Parametric VaR",
        "Portfolio Risk (2 assets)",
        "Sharpe Ratio",
        "Jensen's Alpha",
        "Altman Z-Score",
        "Expected Loss (Credit Risk)",
        "Modified Duration",
        "Beta Calculation",
    ])

    if problem == "Parametric VaR":
        W = st.number_input("Portfolio Value W (₹)", value=10000000.0)
        sigma = st.number_input("Daily σ (%)", value=1.5)
        conf = st.selectbox("Confidence", [95, 99])
        T = st.number_input("Days", value=1)
        z = 1.645 if conf == 95 else 2.326
        var = W * (sigma/100) * z * np.sqrt(T)
        st.write(f"**Formula:** VaR = W × σ × Z × √T")
        st.latex(f"= {W:,.0f} \\times {sigma/100} \\times {z} \\times \\sqrt{{{T}}} = ₹{round(var,2):,.2f}")
        st.success(f"VaR ({conf}%, {T}d) = ₹{round(var,2):,.2f}")

    elif problem == "Portfolio Risk (2 assets)":
        w1 = st.number_input("Weight 1 (%)", value=60.0)/100
        s1 = st.number_input("σ₁ (%)", value=20.0); s2 = st.number_input("σ₂ (%)", value=15.0)
        rho = st.number_input("Correlation ρ", value=0.4)
        var_p = w1**2*s1**2 + (1-w1)**2*s2**2 + 2*w1*(1-w1)*rho*s1*s2
        sigma_p = np.sqrt(var_p)
        st.write("**σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂**")
        st.latex(f"= {w1}^2\\times{s1}^2 + {round(1-w1,2)}^2\\times{s2}^2 + 2\\times{w1}\\times{round(1-w1,2)}\\times{rho}\\times{s1}\\times{s2}")
        st.success(f"Portfolio σ = {round(sigma_p,4)}%")

    elif problem == "Sharpe Ratio":
        rp = st.number_input("Rp (%)", value=16.0); rf = st.number_input("Rf (%)", value=7.0)
        sp = st.number_input("σp (%)", value=18.0)
        sharpe = (rp-rf)/sp
        st.write("**Sharpe = (Rp - Rf) / σp**")
        st.latex(f"= \\frac{{{rp}-{rf}}}{{{sp}}} = {round(sharpe,4)}")
        st.success(f"Sharpe Ratio = {round(sharpe,4)}")

    elif problem == "Jensen's Alpha":
        rp = st.number_input("Rp (%)", value=16.0, key="ja_rp"); rf = st.number_input("Rf (%)", value=7.0, key="ja_rf")
        rm = st.number_input("Rm (%)", value=14.0); beta = st.number_input("β", value=1.1)
        capm = rf + beta*(rm-rf); alpha = rp - capm
        st.write("**Jensen's α = Rp - [Rf + β(Rm-Rf)]**")
        st.latex(f"= {rp} - [{rf} + {beta}\\times({rm}-{rf})]")
        st.latex(f"= {rp} - {round(capm,4)} = {round(alpha,4)}\\%")
        st.success(f"Jensen's Alpha = {round(alpha,4)}%")

    elif problem == "Altman Z-Score":
        X1=st.number_input("X1=WC/TA",value=0.25); X2=st.number_input("X2=RE/TA",value=0.30)
        X3=st.number_input("X3=EBIT/TA",value=0.18); X4=st.number_input("X4=MktCap/Debt",value=2.0)
        X5=st.number_input("X5=Revenue/TA",value=0.90)
        Z=1.2*X1+1.4*X2+3.3*X3+0.6*X4+1.0*X5
        st.write("**Z = 1.2X₁ + 1.4X₂ + 3.3X₃ + 0.6X₄ + 1.0X₅**")
        st.latex(f"= 1.2({X1})+1.4({X2})+3.3({X3})+0.6({X4})+1.0({X5})")
        zone = "Safe (>2.99)" if Z>2.99 else "Grey (1.81-2.99)" if Z>1.81 else "Distress (<1.81)"
        st.success(f"Z = {round(Z,4)} — {zone}")

    elif problem == "Expected Loss (Credit Risk)":
        pd_val=st.number_input("PD (%)",value=2.0); lgd_val=st.number_input("LGD (%)",value=45.0)
        ead_val=st.number_input("EAD (₹ Cr)",value=100.0)
        el=pd_val/100*lgd_val/100*ead_val
        st.write("**EL = PD × LGD × EAD**")
        st.latex(f"= {pd_val/100} \\times {lgd_val/100} \\times {ead_val} = {round(el,4)} \\text{{ Cr}}")
        st.success(f"Expected Loss = ₹{round(el,4)} Cr")

    elif problem == "Modified Duration":
        coupon=st.number_input("Coupon (%)",value=8.0); ytm=st.number_input("YTM (%)",value=9.0)
        n=st.number_input("Years",value=5.0); face=st.number_input("Face",value=1000.0)
        r=ytm/100; c=face*coupon/100
        price=sum(c/(1+r)**t for t in range(1,int(n)+1))+face/(1+r)**n
        mac=sum(t*(c/(1+r)**t)/price for t in range(1,int(n)+1))+n*(face/(1+r)**n)/price
        mod=mac/(1+r)
        st.write(f"**Price = {round(price,2)} | Mac Duration = {round(mac,4)} | Mod Duration = {round(mod,4)}**")
        st.success(f"Modified Duration = {round(mod,4)} | Price change per 1% rate move = {round(mod,4)}%")

    elif problem == "Beta Calculation":
        rho=st.number_input("Correlation ρ",value=0.75); si=st.number_input("σ_i (%)",value=25.0)
        sm=st.number_input("σ_M (%)",value=15.0)
        beta=rho*si/sm
        st.write("**β = ρ × σᵢ / σ_M**")
        st.latex(f"= {rho} \\times {si}/{sm} = {round(beta,4)}")
        st.success(f"Beta = {round(beta,4)}")

# =========================================================
elif menu == "AI Hint System":
    st.header("🤖 AI Hint System")
    problems_h = {
        "Parametric VaR": {
            "q": "W=₹1Cr, σ=2%/day, 99% confidence, 1-day VaR.",
            "correct": 10000000*0.02*2.326,
            "hints":["VaR = W × σ × Z","Z(99%) = 2.326","= 1,00,00,000 × 0.02 × 2.326"],
            "formula": r"VaR = 1{,}00{,}00{,}000 \times 0.02 \times 2.326 = ₹4{,}65{,}200"
        },
        "Sharpe Ratio": {
            "q": "Rp=18%, Rf=7%, σp=20%. Find Sharpe.",
            "correct":(18-7)/20,
            "hints":["Sharpe = (Rp-Rf)/σp","=(18-7)/20","=11/20"],
            "formula": r"\text{Sharpe} = \frac{18-7}{20} = 0.55"
        },
        "Portfolio Risk": {
            "q": "w₁=0.6, σ₁=20%, σ₂=15%, ρ=0.3. Find portfolio σ.",
            "correct": np.sqrt(0.36*400+0.16*225+2*0.6*0.4*0.3*20*15),
            "hints":["σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂",
                     "= 0.36×400 + 0.16×225 + 2×0.6×0.4×0.3×20×15",
                     "= 144 + 36 + 43.2 = 223.2"],
            "formula": r"\sigma_p = \sqrt{223.2} = 14.94\%"
        }
    }
    sel=st.selectbox("Choose Problem",list(problems_h.keys()))
    prob=problems_h[sel]
    st.markdown(f"**Problem:** {prob['q']}")
    ans=st.number_input("Your Answer",value=0.0,key="rm_hint_ans")
    if st.button("Check"):
        correct=prob["correct"]
        if abs(ans-correct)<abs(correct)*0.02+0.001:
            st.success(f"✅ Correct! = {round(correct,4)}")
            st.balloons()
        else: st.error("❌ Use hints.")
    for i,h in enumerate(prob["hints"],1):
        if st.checkbox(f"Hint {i}",key=f"rmh_{sel}_{i}"): st.info(f"💡 {h}")
    if st.checkbox("Show Solution",key=f"rms_{sel}"): st.latex(prob["formula"])

# =========================================================
elif menu == "Quiz Engine":
    st.header("📝 Risk Management Quiz Engine")
    difficulty=st.selectbox("Difficulty",["Beginner","Intermediate","Advanced"])
    if "rm_quiz_gen" not in st.session_state or st.button("🔄 New Question"):
        if difficulty=="Beginner":
            st.session_state.rm_W=random.choice([5000000,10000000,20000000])
            st.session_state.rm_sig=random.choice([1.0,1.5,2.0])
            st.session_state.rm_conf=random.choice([95,99])
            st.session_state.rm_qtype="var"
        elif difficulty=="Intermediate":
            st.session_state.rm_rp=random.choice([14,16,18,20])
            st.session_state.rm_rf=random.choice([6,7,8])
            st.session_state.rm_sp=random.choice([15,18,20,25])
            st.session_state.rm_qtype="sharpe"
        else:
            st.session_state.rm_rp2=random.choice([15,16,18])
            st.session_state.rm_rf2=random.choice([6,7])
            st.session_state.rm_rm=random.choice([12,14,15])
            st.session_state.rm_beta=random.choice([1.0,1.2,1.4,0.8])
            st.session_state.rm_qtype="alpha"
        st.session_state.rm_quiz_gen=True

    qtype=st.session_state.rm_qtype
    if qtype=="var":
        W=st.session_state.rm_W; sig=st.session_state.rm_sig; conf=st.session_state.rm_conf
        z=1.645 if conf==95 else 2.326; correct=W*sig/100*z
        st.markdown(f"**1-Day Parametric VaR:**\nW=₹{W:,}, σ={sig}%/day, {conf}% confidence")
    elif qtype=="sharpe":
        rp=st.session_state.rm_rp; rf=st.session_state.rm_rf; sp=st.session_state.rm_sp
        correct=(rp-rf)/sp
        st.markdown(f"**Sharpe Ratio:**\nRp={rp}%, Rf={rf}%, σp={sp}%")
    else:
        rp=st.session_state.rm_rp2; rf=st.session_state.rm_rf2
        rm=st.session_state.rm_rm; beta=st.session_state.rm_beta
        correct=rp-(rf+beta*(rm-rf))
        st.markdown(f"**Jensen's Alpha:**\nRp={rp}%, Rf={rf}%, Rm={rm}%, β={beta}")

    ans=st.number_input("Your Answer",value=0.0,key="rm_quiz_ans")
    if st.button("Submit"):
        if abs(ans-correct)<max(0.001,abs(correct)*0.02):
            st.success(f"✅ Correct! = {round(correct,4)}")
            st.balloons()
        else: st.error(f"❌ Answer = {round(correct,4)}")

# =========================================================
elif menu == "Formula Cheat Sheet":
    st.header("📘 Risk Management — Formula Cheat Sheet")
    formulas = """
RISK MANAGEMENT — COMPLETE FORMULA REFERENCE
==============================================

VALUE AT RISK (VaR)
──────────────────────────────────────────────────
1. Parametric VaR (1-day):  VaR = W × σ × Z_α
2. Parametric VaR (N-day):  VaR_N = VaR_1 × √N
3. Z-scores: 90%=1.282 | 95%=1.645 | 99%=2.326 | 99.9%=3.090
4. Historical VaR: (1-α)th percentile of loss distribution
5. Expected Shortfall: ES = E[Loss | Loss > VaR]
6. ES (parametric): ES = W × σ × N'(Z_α)/α

PORTFOLIO RISK
──────────────────────────────────────────────────
7. Portfolio Variance (2 assets):
   σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov₁₂
8. Covariance:  Cov₁₂ = ρ₁₂ × σ₁ × σ₂
9. Diversification benefit: σ_p < w₁σ₁ + w₂σ₂ when ρ < 1

BETA & CAPM
──────────────────────────────────────────────────
10. Beta:  β = ρ × σᵢ/σ_M  =  Cov(Rᵢ,R_M)/Var(R_M)
11. Systematic Risk: β²σ²_M
12. Total Risk: β²σ²_M + σ²_ε
13. R² = systematic risk / total risk = ρ²

RISK-ADJUSTED RETURNS
──────────────────────────────────────────────────
14. Sharpe Ratio:     (Rp − Rf) / σp
15. Treynor Ratio:    (Rp − Rf) / βp
16. Jensen's Alpha:   Rp − [Rf + β(Rm − Rf)]
17. M² (Modigliani): Sharpe × σ_M + Rf
18. Sortino Ratio:    (Rp − MAR) / Downside σ
19. Calmar Ratio:     Annual Return / |Max Drawdown|

CREDIT RISK
──────────────────────────────────────────────────
20. Expected Loss:  EL = PD × LGD × EAD
21. Altman Z:  1.2X₁ + 1.4X₂ + 3.3X₃ + 0.6X₄ + 1.0X₅
    Z > 2.99: Safe | 1.81-2.99: Grey | < 1.81: Distress

INTEREST RATE RISK
──────────────────────────────────────────────────
22. Modified Duration:  D_mod = D_mac / (1+y)
23. Price change:  %ΔP ≈ −D_mod × Δy
24. BPV:  D_mod × P / 10000

LIQUIDITY RISK
──────────────────────────────────────────────────
25. LCR = HQLA / Net Cash Outflows (30d) ≥ 100%
26. NSFR = Available Stable Funding / Required ≥ 100%

CAPITAL ADEQUACY (BASEL III)
──────────────────────────────────────────────────
27. CRAR = Total Capital / RWA × 100 (min 11.5% India)
28. Tier 1 Ratio = Tier 1 Capital / RWA (min 7% India)
29. Op Risk Capital (BIA) = 15% × Average Gross Income

HEDGE RATIO
──────────────────────────────────────────────────
30. Optimal Hedge Ratio:  h* = ρ × σS/σF
31. Beta Hedge Contracts:  N* = (βT−βP) × P / (F₀×L)
32. Duration Hedge:  N* = (DT−DP) × P / (DF×F₀)

KEY RULES
──────────────────────────────────────────────────
- Higher confidence level → Higher VaR → More conservative
- VaR scales with √T (square root of time)
- ES > VaR always (captures tail severity)
- Diversification: ρ < 1 → portfolio risk < weighted sum
- Sharpe uses total risk (σ); Treynor uses systematic risk (β)
- Positive Jensen's Alpha = outperforms CAPM prediction
==============================================
"""
    st.text_area("Formula Reference", formulas, height=700)
    st.download_button("📥 Download", data=formulas,
                       file_name="Risk_Management_Formulas.txt")

# =========================================================
elif menu == "Common Student Mistakes":
    st.header("⚠️ Common Student Mistakes in Risk Management")
    mistakes = pd.DataFrame({
        "Mistake": [
            "VaR means you WILL NOT lose more than X",
            "Scaling VaR: multiplying by N (not √N)",
            "Higher σ = higher VaR at ALL confidence levels",
            "VaR is sub-additive (diversification always helps)",
            "Sharpe and Treynor always give same ranking",
            "Jensen's alpha = actual return − Rf",
            "Duration = maturity of bond",
            "Altman Z: using revenues not asset turnover",
            "EL = PD + LGD + EAD (adding not multiplying)",
            "CRAR benchmark = 8% (using global, not India)",
        ],
        "Correct Approach": [
            "VaR says: 'X% chance of losing MORE than VaR'. It does NOT say you won't lose more — it says the probability is (1-α)%.",
            "VaR scales with SQUARE ROOT of time: VaR_N = VaR_1 × √N. Never multiply directly.",
            "Higher σ raises VaR, but z-score changes with confidence. At lower confidence, difference is smaller.",
            "VaR is NOT always sub-additive — this is a known limitation. Expected Shortfall (ES) is sub-additive (coherent).",
            "Different risk bases: Sharpe=total risk; Treynor=systematic risk. Diversified portfolio: use Treynor. Rankings can differ!",
            "Jensen's α = Rp − [Rf + β(Rm−Rf)]. Must subtract CAPM-required return, not just Rf.",
            "Duration ≠ maturity. Duration < maturity (except zero-coupon). Modified duration measures price sensitivity.",
            "X₅ = Revenue / Total Assets (asset turnover). Common error: using Revenue/Equity or just Revenue.",
            "EL = PD × LGD × EAD (multiplication). These are three SEPARATE components multiplied together.",
            "India (RBI): CRAR min = 9% + 2.5% CCB = 11.5%. Global Basel minimum is 8%. Use 11.5% for Indian banks.",
        ]
    })
    st.table(mistakes)

# =========================================================
elif menu == "Advanced Quiz Bank":
    st.header("📝 Advanced Quiz Bank")
    level=st.selectbox("Difficulty",["Beginner","Intermediate","Advanced"])

    if level=="Beginner":
        st.markdown("""
**Problem:** Portfolio: W=₹50L, daily σ=1.8%.
(a) 1-day VaR at 95%  (b) 1-day VaR at 99%  (c) 10-day VaR at 95%
""")
        W=5000000; sig=0.018; z95=1.645; z99=2.326
        a1=W*sig*z95; a2=W*sig*z99; a3=a1*np.sqrt(10)
        c1,c2,c3=st.columns(3)
        c1.number_input("(a) 1-day VaR 95% (₹)",value=0.0,step=100.0,key="aqb_beg_a")
        c2.number_input("(b) 1-day VaR 99% (₹)",value=0.0,step=100.0,key="aqb_beg_b")
        c3.number_input("(c) 10-day VaR 95% (₹)",value=0.0,step=100.0,key="aqb_beg_c")
        if st.button("Evaluate",key="beg_btn"):
            if abs(st.session_state.aqb_beg_a-a1)<100 and abs(st.session_state.aqb_beg_b-a2)<100 and abs(st.session_state.aqb_beg_c-a3)<100:
                st.success(f"✅ (a)₹{round(a1,0):,.0f} (b)₹{round(a2,0):,.0f} (c)₹{round(a3,0):,.0f}")
                st.balloons()
            else: st.error(f"(a)₹{round(a1,0):,.0f} | (b)₹{round(a2,0):,.0f} | (c)₹{round(a3,0):,.0f}")

    elif level=="Intermediate":
        st.markdown("""
**Problem:** Fund A: Rp=18%, σ=22%, β=1.3. Fund B: Rp=16%, σ=15%, β=0.9. Rf=7%, Rm=14%, σ_M=15%.
(a) Sharpe A & B  (b) Treynor A & B  (c) Jensen's α for A  (d) Which fund is better on each measure?
""")
        shA=(18-7)/22; shB=(16-7)/15; trA=(18-7)/1.3; trB=(16-7)/0.9
        alphaA=18-(7+1.3*(14-7)); alphaB=16-(7+0.9*(14-7))
        c1,c2=st.columns(2)
        c1.number_input("Sharpe A",value=0.0,step=0.01,key="aqb_int_shA")
        c2.number_input("Sharpe B",value=0.0,step=0.01,key="aqb_int_shB")
        c3,c4=st.columns(2)
        c3.number_input("Treynor A",value=0.0,step=0.01,key="aqb_int_trA")
        c4.number_input("Treynor B",value=0.0,step=0.01,key="aqb_int_trB")
        c5=st.number_input("Jensen's Alpha A (%)",value=0.0,step=0.1,key="aqb_int_alphaA")
        if st.button("Evaluate",key="int_btn"):
            a_shA=st.session_state.aqb_int_shA; a_shB=st.session_state.aqb_int_shB
            a_trA=st.session_state.aqb_int_trA; a_trB=st.session_state.aqb_int_trB
            if all([abs(a_shA-shA)<0.01,abs(a_shB-shB)<0.01,abs(a_trA-trA)<0.01,abs(a_trB-trB)<0.01,abs(c5-alphaA)<0.1]):
                st.success(f"✅ ShA={round(shA,4)}, ShB={round(shB,4)}, TrA={round(trA,4)}, TrB={round(trB,4)}, αA={round(alphaA,2)}%")
                st.balloons()
            else: st.error(f"ShA={round(shA,4)} | ShB={round(shB,4)} | TrA={round(trA,4)} | TrB={round(trB,4)} | αA={round(alphaA,2)}%")

    elif level=="Advanced":
        st.markdown("""
**Problem:** Altman Z-Score:
WC=₹150Cr, RE=₹200Cr, EBIT=₹120Cr, MktCap=₹800Cr, Debt=₹400Cr, Revenue=₹600Cr, TA=₹700Cr.
(a) X₁ X₂ X₃ X₄ X₅  (b) Z-Score  (c) Zone  (d) Key risk action?
""")
        X1=150/700; X2=200/700; X3=120/700; X4=800/400; X5=600/700
        Z=1.2*X1+1.4*X2+3.3*X3+0.6*X4+1.0*X5
        zone="Safe" if Z>2.99 else "Grey" if Z>1.81 else "Distress"
        c1,c2,c3,c4,c5=st.columns(5)
        c1.number_input("X₁",value=0.0,step=0.001,key="aqb_adv_x1")
        c2.number_input("X₂",value=0.0,step=0.001,key="aqb_adv_x2")
        c3.number_input("X₃",value=0.0,step=0.001,key="aqb_adv_x3")
        c4.number_input("X₄",value=0.0,step=0.001,key="aqb_adv_x4")
        c5.number_input("X₅",value=0.0,step=0.001,key="aqb_adv_x5")
        c6=st.number_input("Z-Score",value=0.0,step=0.01,key="aqb_adv_Z")
        zone_ans=st.radio("Zone:",["Safe","Grey","Distress"])
        if st.button("Evaluate",key="adv_btn"):
            ok_x=all([abs(st.session_state.get(f"aqb_adv_x{j}",0)-v)<0.002
                       for j,v in enumerate([X1,X2,X3,X4,X5],1)])
            if ok_x and abs(c6-Z)<0.05 and zone_ans==zone:
                st.success(f"✅ Z={round(Z,4)}, Zone={zone}")
                st.balloons()
            else: st.error(f"X1={round(X1,4)} X2={round(X2,4)} X3={round(X3,4)} X4={round(X4,4)} X5={round(X5,4)} | Z={round(Z,4)} | {zone}")

# =========================================================
elif menu == "Progress Tracker":
    st.header("📈 Progress Tracker")
    if "rm_completed" not in st.session_state: st.session_state.rm_completed=[]
    if "rm_scores" not in st.session_state: st.session_state.rm_scores=[]
    all_modules=["Risk Measurement — Variance & SD","Value at Risk (VaR) — Parametric",
                 "VaR — Historical Simulation","VaR — Monte Carlo","Expected Shortfall (CVaR)",
                 "Beta & Systematic Risk","Portfolio Risk & Diversification",
                 "Sharpe, Treynor & Jensen Ratios","Sortino & Calmar Ratios",
                 "Credit Risk & Credit Ratings","Altman Z-Score","Liquidity Risk",
                 "Interest Rate Risk","Currency (Forex) Risk","Operational Risk",
                 "Enterprise Risk Management (ERM)","Stress Testing & Scenario Analysis",
                 "CAMEL Framework","Basel III & Capital Adequacy","Indian Risk Regulations"]
    selected=st.multiselect("Mark completed:",all_modules,default=st.session_state.rm_completed)
    st.session_state.rm_completed=selected
    col1,col2=st.columns(2)
    with col1: topic=st.selectbox("Quiz Topic",["VaR","Sharpe/Treynor","Altman Z","Credit Risk","Portfolio Risk","Basel III"])
    with col2: score=st.number_input("Score (%)",0,100,75,key="rm_score_inp")
    if st.button("Log Score"):
        st.session_state.rm_scores.append({"topic":topic,"score":score})
        st.success("Logged!")
    n_done=len(selected); n_total=len(all_modules)
    st.metric("Modules Completed",f"{n_done}/{n_total}")
    st.progress(n_done/n_total)
    if st.session_state.rm_scores:
        avg=sum(s["score"] for s in st.session_state.rm_scores)/len(st.session_state.rm_scores)
        st.metric("Average Score",f"{round(avg,1)}%")
    if n_done==n_total:
        st.success("🏆 All modules complete!")
        st.balloons()

# =========================================================
elif menu == "Case-Based Learning":
    st.header("📚 Case Study: IL&FS Default 2018 — Risk Management Failure")
    st.markdown("""
## Background

**Infrastructure Leasing & Financial Services (IL&FS)** was India's largest
infrastructure NBFC with ₹91,000 Crore in debt. In September 2018, it
defaulted on short-term commercial paper obligations — triggering India's
worst NBFC credit crisis.
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Financial Data (2018)")
        st.table(pd.DataFrame({
            "Metric": ["Total Debt", "Short-term borrowings", "Long-term assets",
                       "ALM Mismatch", "CRAR (estimated)", "NPA ratio", "Liquidity position"],
            "Value": ["₹91,000 Cr", "~₹17,000 Cr (short-term)", "₹85,000 Cr+ infrastructure",
                      "~15 years (funded ST with LT assets)", "<8% (inadequate)", ">50%",
                      "Critical — couldn't rollover CP"]
        }))

    with col2:
        st.subheader("Risk Failures Identified")
        failures = [
            "❌ **Liquidity Risk:** Funded 30-year roads with 90-day CP",
            "❌ **ALM Mismatch:** Asset duration 15+ years, liability duration <1 year",
            "❌ **Concentration Risk:** Over-reliance on short-term market funding",
            "❌ **Credit Risk:** Overstated asset quality; reclassified NPAs",
            "❌ **Governance Failure:** Board, auditors, rating agencies all missed it",
            "❌ **Rating Dependence:** CP rated A1+, investors blindly trusted ratings",
            "❌ **Regulatory Gap:** Infrastructure NBFCs not under same RBI supervision",
        ]
        for f in failures:
            st.markdown(f)

    st.subheader("Risk Framework Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.error("**LCR Analysis**")
        hqla_ilfs = 2000  # estimate ₹2000 Cr
        outflows_ilfs = 17000
        lcr_ilfs = hqla_ilfs / outflows_ilfs * 100
        st.metric("Estimated LCR", pct(lcr_ilfs), "Min 100% — VIOLATED")

    with col2:
        st.error("**Altman Z-Score (estimated)**")
        Z_ilfs = 1.2*0.02 + 1.4*0.08 + 3.3*0.03 + 0.6*0.5 + 1.0*0.3
        st.metric("Z-Score (est.)", round(Z_ilfs, 2), "Distress Zone!")

    with col3:
        st.error("**VaR Implication**")
        st.metric("Funding VaR", "Infinite", "No liquid asset buffer")

    st.subheader("Contagion Effect")
    contagion = pd.DataFrame({
        "Institution Affected": ["DHFL (NBFC)", "Yes Bank", "Mutual Funds", "Reliance Capital", "PSU Banks"],
        "Exposure to IL&FS/sector": ["₹12,000Cr", "₹2,500Cr", "₹2,500Cr CP", "₹3,000Cr", "Various"],
        "Consequence": ["Own default 2019", "Credit quality concerns", "NAV fall; redemption pressure",
                         "Rating downgrade", "NPA increase"]
    })
    st.table(contagion)

    st.subheader("Key Lessons")
    lessons = [
        "**Liquidity risk can kill even profitable firms** — IL&FS was theoretically 'asset-rich' but cash-poor",
        "**ALM mismatch = ticking time bomb** — never fund long-term assets with short-term liabilities",
        "**Credit ratings are lagging, not leading** — A1+ to D in weeks shows ratings failed",
        "**Concentration risk in funding** — diversify funding sources and maturities",
        "**Governance matters** — risk management requires board-level oversight",
        "**RBI response: 2019 ALM guidelines** — mandatory liquidity risk monitoring for NBFCs",
        "**SEBI response: Stricter credit rating surveillance** — quarterly monitoring required",
    ]
    for l in lessons:
        st.markdown(f"- {l}")

    st.subheader("Q&A Discussion")
    q_ilfs = st.radio("Which risk measure would have BEST predicted the IL&FS crisis?",
                       ["VaR on equity portfolio",
                        "Liquidity Coverage Ratio (LCR) — would have shown near-zero buffer",
                        "Sharpe Ratio of IL&FS equity",
                        "Altman Z-Score only"])
    if q_ilfs == "Liquidity Coverage Ratio (LCR) — would have shown near-zero buffer":
        st.success("✅ Correct! LCR < 5% would have flagged the extreme funding vulnerability months before default.")
    else:
        st.info("Think about the fundamental problem: IL&FS couldn't PAY. That's a LIQUIDITY problem. LCR measures exactly this.")
