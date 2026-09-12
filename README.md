Pinnacle-Style Sports Algorithm

A sports analytics and prediction framework inspired by quantitative sports modeling.

«Important: This is an independent educational project. It does not reproduce or contain Pinnacle's proprietary algorithms, and it does not place wagers.»

🚀 Version

v0.2 — Historical Data + Machine Learning + Backtesting

📌 Overview

The Pinnacle-Style Sports Algorithm compares statistical model predictions against market-implied probabilities.

The system combines:

- Historical team performance
- ELO ratings
- Machine-learning predictions
- Market odds
- Implied probabilities
- Vig/overround normalization
- Model-vs-market edge
- Backtesting
- Performance metrics

🧠 Architecture

             HISTORICAL DATA
                    │
                    ▼
          ┌──────────────────┐
          │ Feature Engine   │
          └────────┬─────────┘
                   │
          ┌────────┴─────────┐
          ▼                  ▼
     ELO MODEL           ML MODEL
          │                  │
          └────────┬─────────┘
                   ▼
             ENSEMBLE MODEL
                   │
                   ▼
          MODEL PROBABILITY
                   │
                   │
MARKET ODDS ───────┤
                   ▼
          IMPLIED PROBABILITY
                   │
                   ▼
              EDGE ENGINE
                   │
                   ▼
             BACKTESTING
                   │
                   ▼
              PERFORMANCE
                REPORT

🏆 Supported Sports

The project is designed to support:

- 🏈 NFL
- 🏀 NBA
- ⚾ MLB
- 🏒 NHL
- ⚽ Soccer

Additional sports can be added through new data adapters and models.

📊 Core Calculation

American odds are converted into implied probability.

For positive odds:

Probability = 100 / (Odds + 100)

For negative odds:

Probability = |Odds| / (|Odds| + 100)

The system then normalizes the probabilities to account for the bookmaker's margin.

Model Edge

Edge = Model Probability - Market Probability

Example:

Model probability: 61%
Market probability: 55%

Edge = +6%

The edge is a statistical signal, not a guarantee of an outcome.

🤖 Models

ELO

The ELO model tracks relative team strength and updates ratings after games.

Machine Learning

v0.2 introduces a classification model using historical features such as:

- Team rating
- Recent performance
- Home/away status
- Points scored
- Points allowed
- Win percentage

Ensemble

The ensemble combines multiple model outputs:

ELO ─────────────┐
                 │
ML Model ────────┼──► Ensemble Probability
                 │
Statistics ──────┘

📈 Backtesting

Historical games can be processed to evaluate model performance.

Tracked metrics include:

- Accuracy
- Brier score
- Log loss
- ROI
- Total simulated profit/loss
- Maximum drawdown
- Closing-line comparison

Backtesting is designed to help determine whether a model has predictive value before being used with new data.

📁 Data

Place raw datasets in:

data/raw/

Processed datasets go into:

data/processed/

Do not commit private API keys or credentials.

Recommended ".gitignore" entries:

.env
*.key
*.secret
__pycache__/
.venv/

🛠️ Installation

Clone the repository:

git clone https://github.com/vegasdude/pinnacle-sports-algorithm.git

Enter the directory:

cd pinnacle-sports-algorithm

Create a virtual environment:

python -m venv .venv

Activate it on Linux/macOS:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

▶️ Run

python main.py

🧪 Testing

Run:

pytest

🔬 Example Workflow

1. Import historical games
        ↓
2. Calculate team statistics
        ↓
3. Update ELO ratings
        ↓
4. Generate ML features
        ↓
5. Train prediction model
        ↓
6. Generate probabilities
        ↓
7. Compare with market probabilities
        ↓
8. Calculate edge
        ↓
9. Backtest historical predictions
        ↓
10. Generate performance report

⚠️ Responsible Use

This repository is intended for:

- Sports analytics
- Machine-learning research
- Probability modeling
- Statistical education
- Historical backtesting

Predictions are uncertain. A positive model edge does not guarantee a winning outcome.

Do not use model output as a guarantee of financial returns.

🗺️ Roadmap

v0.1

- [x] American odds conversion
- [x] Implied probability
- [x] Vig normalization
- [x] ELO model
- [x] Basic edge calculation
- [x] Basic backtester

v0.2

- [x] Historical-data architecture
- [x] ML model architecture
- [x] Ensemble architecture
- [x] Backtesting metrics
- [x] Multi-sport structure
- [x] Documentation

v0.3 — Planned

- [ ] Automated data ingestion
- [ ] Advanced team statistics
- [ ] Player-level features
- [ ] Injury/news feature pipeline
- [ ] Time-series validation
- [ ] Probability calibration
- [ ] Advanced CLV tracking
- [ ] Model comparison dashboard

v0.4 — Planned

- [ ] Live odds ingestion
- [ ] Real-time prediction updates
- [ ] Historical odds database
- [ ] Advanced ensemble models
- [ ] Interactive dashboard

📜 License

This project can be released under the MIT License.

⭐ Project Goal

Build an open, transparent sports analytics framework for researching how statistical models, historical performance, and market probabilities can be combined to evaluate sports outcomes.

This project is not affiliated with or endorsed by Pinnacle.
