from docx import Document

# Create a Word document
doc = Document()
doc.add_heading("Unsupervised Drift Detection in GenAI (Comprehensive Notes)", level=1)

# Section 1
doc.add_heading("1. Overview", level=2)
doc.add_paragraph("""In Generative AI (GenAI) and ML production systems, models often face data distribution changes after deployment. 
These changes can silently degrade performance. Drift detection identifies when the live environment diverges from the training conditions. 
When ground truth (labels) is unavailable — which is often the case in GenAI — we use unsupervised drift detectors.""")

# Section 2
doc.add_heading("2. Types of Drift", level=2)
doc.add_paragraph("""
- Data Drift: Input data distribution changes over time (e.g., users start using new slang in prompts)
- Concept Drift: The relationship between inputs and outputs changes (e.g., meaning of “positive sentiment” evolves)
- Model Drift: Model output behavior or quality degrades (e.g., LLM responses become less accurate)
""")

# Section 3
doc.add_heading("3. Why Unsupervised Drift Detection?", level=2)
doc.add_paragraph("""
In GenAI systems, labeled data is rare or delayed (e.g., user feedback, human evaluation). 
Unsupervised methods can detect anomalies without ground truth, monitor feature, embedding, and output distributions, 
and enable automated alerting before quality drops.
""")

# Section 4
doc.add_heading("4. Common Unsupervised Drift Detection Techniques", level=2)
doc.add_paragraph("""
- Kolmogorov–Smirnov (KS) Test: Compare numeric feature distributions (Data drift)
- Population Stability Index (PSI): Quantify distribution shift (Data drift)
- Jensen–Shannon Divergence (JSD): Compare probability distributions (Data drift)
- Embedding Similarity (Cosine): Compare semantic meaning (Concept drift)
- Autoencoder Reconstruction Error: Measure input pattern deviation (Data/Concept drift)
- Output Distribution Shift: Compare model outputs (Model drift)
""")

# Section 5
doc.add_heading("5. Practical Examples", level=2)
doc.add_paragraph("A. Data Drift — Using Population Stability Index (PSI)")
doc.add_paragraph("""
Example Python Code:
--------------------
import numpy as np

def calculate_psi(expected, actual, buckets=10):
    def scale_range(arr, min_val, max_val):
        return (arr - min_val) / (max_val - min_val)

    breakpoints = np.arange(0, buckets + 1) / buckets
    expected_percents = np.histogram(scale_range(expected, expected.min(), expected.max()), bins=breakpoints)[0] / len(expected)
    actual_percents = np.histogram(scale_range(actual, expected.min(), expected.max()), bins=breakpoints)[0] / len(actual)
    psi = np.sum((expected_percents - actual_percents) * np.log(expected_percents / actual_percents))
    return psi

train_feature = np.random.normal(0, 1, 1000)
prod_feature = np.random.normal(0.5, 1.2, 1000)

psi = calculate_psi(train_feature, prod_feature)
print(f"PSI = {psi:.3f}")
if psi > 0.2:
    print("⚠️ Data drift detected!")
""")

doc.add_paragraph("Interpretation: PSI < 0.1 → No drift | 0.1–0.2 → Moderate drift | > 0.2 → Significant drift")

doc.add_paragraph("B. Concept Drift — Using Embedding Similarity")
doc.add_paragraph("""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
train_texts = ["I love this product", "Great service", "Amazing experience!"]
prod_texts = ["This is mid", "Not bad", "Could be better"]

train_emb = model.encode(train_texts, normalize_embeddings=True)
prod_emb = model.encode(prod_texts, normalize_embeddings=True)

similarity = np.mean(cosine_similarity([train_emb.mean(axis=0)], [prod_emb.mean(axis=0)]))
print(f"Mean Embedding Similarity: {similarity:.3f}")
if similarity < 0.9:
    print("⚠️ Concept drift suspected.")
""")

doc.add_paragraph("C. Model Drift — Using Output Distribution (KS Test)")
doc.add_paragraph("""
from scipy.stats import ks_2samp
import numpy as np

train_outputs = np.random.uniform(0.8, 1.0, 1000)
prod_outputs = np.random.uniform(0.4, 0.9, 1000)

stat, p_value = ks_2samp(train_outputs, prod_outputs)
print(f"KS Statistic: {stat:.3f}, p-value: {p_value:.3f}")
if p_value < 0.05:
    print("⚠️ Model drift detected!")
""")

# Section 6
doc.add_heading("6. Unified Production-Level Monitoring", level=2)
doc.add_paragraph("""
Example with Evidently:
-----------------------
from evidently.report import Report
from evidently.metrics import DataDriftPreset
import pandas as pd
import numpy as np

train = pd.DataFrame({'feature': np.random.normal(0, 1, 1000)})
prod = pd.DataFrame({'feature': np.random.normal(1, 1.2, 1000)})

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=train, current_data=prod)
report.save_html("drift_report.html")
print("✅ Drift report generated: drift_report.html")
""")

# Section 7
doc.add_heading("7. Best Practices for Production", level=2)
doc.add_paragraph("""
- Automate Checks: Run drift checks periodically using Airflow or Prefect.
- Monitor Multiple Levels: Input data, intermediate embeddings, model outputs.
- Use Dashboards: Store metrics (PSI, KS, similarity) in Prometheus/Grafana.
- Trigger Alerts: Set thresholds (PSI>0.2, cosine<0.9).
- Log Reference Distributions: Keep training stats for comparison.
- Use Specialized Libraries: Evidently, WhyLogs, River.
""")

# Section 8
doc.add_heading("8. Tools & Frameworks", level=2)
doc.add_paragraph("""
- Evidently AI: Statistical & visual drift reports.
- WhyLogs: Data logging and drift metrics (streaming-compatible).
- River: Online learning & incremental drift detection.
- Alibi Detect: Advanced drift detection (KS, MMD, KL Divergence).
""")

# Section 9
doc.add_heading("9. Summary Table", level=2)
doc.add_paragraph("""
| Drift Type | Detection Method | Key Metric | Example Tool |
|-------------|------------------|-------------|---------------|
| Data Drift | PSI / KS Test | PSI > 0.2 | Evidently, SciPy |
| Concept Drift | Embedding Similarity | Cosine < 0.9 | Sentence Transformers |
| Model Drift | Output Distribution | KS p < 0.05 | SciPy, WhyLogs |
""")

# Section 10
doc.add_heading("10. Key Takeaways", level=2)
doc.add_paragraph("""
- Unsupervised drift detection is crucial in GenAI where labels are scarce.
- Combine statistical, semantic, and behavioral methods for robust monitoring.
- Automate drift detection pipelines for early detection and prevention.
- Use Evidently, WhyLogs, and River for production deployment.
""")

# Save the document
file_path = "/mnt/data/Unsupervised_Drift_Detection_in_GenAI.docx"
doc.save(file_path)

file_path
