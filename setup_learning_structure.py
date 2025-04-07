import os

# Define your learning structure
folders = {
    "1_experiment_design_stats": "Hypothesis testing, t-tests, sample size",
    "2_causal_inference": "DiD, Synthetic Control, IVs, RDD",
    "3_mmm_attribution": "Attribution models, MMM (Markov, Shapley, Robyn)",
    "4_forecasting": "ARIMA, Prophet, LSTMs, trend decomposition",
    "5_clv_bidding_optimization": "CLV estimation, ROAS modeling, bidding strategy",
    "6_execution_and_tooling": "Spark, SQL, Looker, Databricks, Visualization best practices"
}

# Create folders and one README.md in each
for folder, desc in folders.items():
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(f"# {folder.replace('_', ' ').title()}\n\n")
        f.write(f"**Topic Overview**: {desc}\n\n")
        f.write("## 📓 Notes & Summaries\n\n- [ ] Add theoretical explanations, formulas, and insights here.\n\n")
        f.write("## 🔗 Resources\n\n- [ ] Add articles, blogs, papers, videos, or documentation here.\n")

# Create (or overwrite) the main README.md from scratch
with open("README.md", "w") as readme:
    readme.write("# 📊 Marketing Science Learning Plan\n\n")
    readme.write("This repository tracks my structured learning journey into data analysis, experimentation, causal inference, MMM, forecasting, and marketing optimization.\n\n")
    
    readme.write("## ✅ Modules Overview\n\n")
    for i, (folder, desc) in enumerate(folders.items(), 1):
        title = folder.replace("_", " ").title()
        readme.write(f"- [ ] **{i}. [{title}](./{folder}/README.md)** – {desc}\n")

    readme.write("\n---\n\n")
    readme.write("## 📁 Folder Contents\n\n")
    for folder in folders:
        readme.write(f"- `{folder}/README.md` → Notes, summaries, and resources for this module\n")
