# Anonymized Building Energy Forecasting Case Study

> Cold-start forecasting with virtual sensors, transfer learning, and a 12-member ensemble.

I am a Data Scientist and Machine Learning Engineer specializing in predictive analytics, system modeling, and high-performance AI pipelines for energy, industrial IoT, and sensor-based ecosystems.

This case study presents work completed during an academically supervised R&D internship in Tallinn, Estonia. The task was to use **two months of data from one building to estimate the remaining roughly 365-day forecast period** under severe data sparsity.

The public version is intentionally anonymized. It contains **no raw measurements, target time series, prediction files, supervisor correspondence, institutional identifiers, or private building metadata**.

## Technical contribution

The solution used a **virtual-sensor method**: concurrent peer-building loads acted as indirect sensors of shared activity, occupancy, calendar effects, and campus-wide behavior. I combined those signals with weather and calendar features in a fixed **12-member model ensemble** built from LightGBM, XGBoost, and temporal profile members.

The workflow included cross-building transfer learning, blind leave-one-building-out testing, SHAP-based interpretability, strict timestamp validation, and production-oriented input/output checks. The design was intended to remain useful when the target history is too short for a conventional seasonal model.

## Public results

The original profile headline reports **12.42% MAPE** and a **0.9456 correlation coefficient** over 7,344 hourly observations. In the internal anonymized proxy benchmark, the fixed ensemble reached approximately **10.1% MAPE** under leave-one-building-out validation. These are different validation summaries and should not be treated as interchangeable.

| Metric or comparison | Result |
|---|---:|
| Profile headline over 7,344 observations | 12.42% MAPE |
| Profile headline correlation | 0.9456 |
| Anonymized proxy benchmark | ~10.1% MAPE |
| Two-peer robustness check | ~10.4% MAPE |
| Same-building winter forward check | ~5.4% MAPE |
| Previous single-model version | ~10.6% MAPE |

The headline metric is not a guarantee of future performance. The largest risk was summer behavior that was not represented in the target building's two-month calibration history.

## Portfolio relevance

This work demonstrates an approach to cold-start and data-sparsity bottlenecks in new SaaS, energy, and IoT deployments. The broader consulting focus is predictive product architecture, feature engineering, interpretable model optimization, and rapid delivery of commercially useful forecasting systems.

## Repository structure

```text
.
├── README.md
├── CASE_STUDY.md
├── DATA_POLICY.md
├── PROFILE_COPY.md
├── requirements.txt
├── src/
│   └── pipeline_outline.py
└── results/
    ├── benchmark_summary.csv
    └── benchmark_summary.png
```

## Data policy

The original data are not redistributed. The included Python file is a generic, data-agnostic outline; it does not contain private schema names or hidden data paths. Reproduction requires permissioned, de-identified inputs with the same conceptual fields described in `DATA_POLICY.md`.

## Limitations

This was a conditional retrospective forecast: it used observed peer-building loads and historical weather for the forecast window. A true year-ahead deployment would also require forecasts of those covariates. The small number of proxy buildings also makes the uncertainty materially larger than a single headline metric suggests.

## Attribution

Case study prepared by Ege. The public repository is an anonymized portfolio presentation of the author's modeling work. It does not claim ownership of the underlying building data or confidential project materials.
