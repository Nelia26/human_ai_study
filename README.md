# Human–AI Collaborative Decision-Making Study

## Overview

This repository contains a web-based experimental platform for conducting a Human–AI collaborative decision-making study in the field of Human–Computer Interaction (HCI).

The platform is designed to collect large-scale participant responses for the analysis of how AI-generated recommendations influence user confidence, trust, and decision-making autonomy during interaction with intelligent systems.

This work represents an original empirical research tool developed for remote participation, centralized data collection, and reproducible experimental analysis.

---

## Research Objective

The primary objective of this study is to investigate the influence of artificial intelligence-generated recommendations on human decision-making behavior.

Specifically, the study examines:

* User confidence in decision-making
* Trust in AI-generated recommendations
* Perceived autonomy during decision-making
* Recommendation acceptance and rejection behavior

The collected data is intended for further statistical analysis in Human–Computer Interaction research.

---

## Repository Structure

```text
human-ai-study/
│
├── app.py
├── tasks.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## System Description

The experimental platform is implemented using Python and Streamlit.

The system presents participants with structured decision-making tasks under two experimental conditions:

* **AI-assisted condition** – participants receive AI-generated recommendations
* **Non-AI condition** – participants make decisions independently

The order of experimental conditions is randomized for each participant.

Each participant receives an anonymous automatically generated identifier.

---

## Data Collection Method

Data is collected through a web-based interface deployed via Streamlit Community Cloud.

Participants access the experiment remotely through a public web link and complete a sequence of decision-making tasks.

For each task, the system records:

* Participant identifier
* Task identifier
* Experimental condition
* AI recommendation (if presented)
* Selected response
* Response time
* Confidence rating
* Trust rating
* Perceived autonomy rating
* Recommendation rejection behavior

---

## Experimental Variables

The study evaluates the following key variables:

### Independent Variable

Presence or absence of AI-generated recommendations.

### Dependent Variables

* Decision confidence
* Trust in AI
* Perceived decision autonomy
* Response time
* Recommendation rejection rate

---

## Local Deployment

To run the application locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application will launch in a local browser session.

---

## Online Deployment

The platform is designed for cloud deployment using Streamlit Community Cloud.

This enables:

* Remote participant access
* Large-scale distributed data collection
* Centralized response storage
* Reproducible experimental execution

---

## Data Ethics and Anonymization

All participant data is fully anonymized.

The system does not collect personally identifiable information (PII).

Each participant is assigned an automatically generated anonymous identifier for research purposes.

Participation is voluntary and intended exclusively for academic research.

---

## Intended Use

This platform is intended for:

* Human–Computer Interaction research
* Human–AI interaction studies
* Decision-making behavior analysis
* Experimental data collection for academic publication
* Reproducible empirical research

---

## Technologies Used

* Python
* Streamlit
* Pandas
* JSON-based task configuration

---

## Citation


Author(s). (2026).
**Human–AI Collaborative Decision-Making Study: Experimental Platform for Investigating AI Influence on User Confidence, Trust, and Decision Autonomy.**

---

## License

This project is provided for academic and research purposes.
