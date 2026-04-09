from pathlib import Path
html = Path('output/index-2-river-marchand.html').read_text(encoding='utf-8')
old = '''<section id="experience">
    <div class="container">
      <p class="section-label">Experience</p>
      <h2 class="section-title">Where I've <em>worked</em></h2>
      <div class="divider"></div>
      <div class="timeline">
        <div class="exp-item">
          <div class="exp-dot"></div>
          <div class="exp-period">Jan 2026 - Present</div>
          <div class="exp-role">Applied AI Researcher · Data Science</div>
          <div class="exp-org">University at Buffalo, Dept. of AI & Society · Part-time · Buffalo, NY</div>
          <ul class="exp-bullets">
            <li>Designed and maintained structured datasets from unstructured text sources to support AI bias and misinformation research.</li>
            <li>Built reproducible data pipelines in Python to automate ingestion, cleaning, and transformation of research data across multiple studies.</li>
          </ul>
        </div>
        <div class="exp-item">
          <div class="exp-dot"></div>
          <div class="exp-period">Sep 2025 - Present</div>
          <div class="exp-role">Applied AI Researcher · Data Analyst</div>
          <div class="exp-org">UB Media Effects, Misinformation & Extremism Lab · Buffalo, NY</div>
          <ul class="exp-bullets">
            <li>Led data cleaning and qualitative-quantitative analysis of 20,000 Reddit posts to surface trust and concern signals around AI mental health tools; translated community discourse into structured sentiment data informing AI policy recommendations.</li>
            <li>Engineered a deep learning classification system using fine-tuned RoBERTa achieving 67% accuracy in automated code categorization with systematic human reviews.</li>
            <li>Applied BERTopic NLP to surface dominant public narratives on AI safety, bias, and access; visualized findings to provide empirical grounding for AI governance frameworks.</li>
          </ul>
        </div>
        <div class="exp-item">
          <div class="exp-dot"></div>
          <div class="exp-period">Sep 2025 - Present</div>
          <div class="exp-role">Applied AI Researcher · Data Analyst</div>
          <div class="exp-org">UB Systems Biomedicine & Pharmaceutics Lab · Buffalo, NY</div>
          <ul class="exp-bullets">
            <li>Built a WRMSE calibration pipeline fitting CompuCell3D cancer migration simulations to experimental invasion data across 5 time points and 2 phenotypes, handling heteroscedastic measurement error.</li>
            <li>Engineered a Python pipeline to extract 3 invasion metrics from 20 stochastic replicates per parameter set across 32 total sets per phenotype.</li>
            <li>Optimized a 5-parameter biological ML model using Bayesian Optimization with Gaussian Processes; reduced biologically invalid proposals by 35% using Feasibility-Constrained Acquisition Expected Improvement.</li>
          </ul>
        </div>
        <div class="exp-item">
          <div class="exp-dot"></div>
          <div class="exp-period">Jan 2025 - Aug 2025</div>
          <div class="exp-role">Applied AI Researcher · Data Analyst</div>
          <div class="exp-org">UB School of Pharmacy & Pharmaceutical Sciences · Buffalo, NY</div>
          <ul class="exp-bullets">
            <li>Modeled physiological age vs. Phase 1 drug metabolism across 10,000 NHANES participants to support personalized dosing strategies.</li>
            <li>Trained Random Survival Forest and XGBoost ML models using 20 biomarkers to predict physiological age; used SHAP to surface key clinical drivers for decision support tools.</li>
          </ul>
        </div>
        <div class="exp-item">
          <div class="exp-dot"></div>
          <div class="exp-period">Dec 2024 - Feb 2025</div>
          <div class="exp-role">Computer Vision Intern</div>
          <div class="exp-org">SETV Global · Remote</div>
          <ul class="exp-bullets">
            <li>Preprocessed and analyzed image datasets using Python, OpenCV, NumPy for computer vision model training; applied data augmentation techniques to improve model recall.</li>
            <li>Documented data pipeline workflows and communicated findings to cross-functional teams in weekly reviews.</li>
          </ul>
        </div>
        <div class="exp-item">
          <div class="exp-dot"></div>
          <div class="exp-period">Aug 2021 - Dec 2023</div>
          <div class="exp-role">Business Intelligence Analyst</div>
          <div class="exp-org">SafetyConnect IOTRL · Hyderabad, India</div>
          <ul class="exp-bullets">
            <li>Benchmarked 12 competitors and developed demand forecasting dashboards across 3 verticals; translated insights into a US market entry strategy supporting a $1.2M Seed A raise.</li>
            <li>Designed KPI dashboards across 4 workstreams; synthesized 20 stakeholder interviews into a feature gap analysis presented at 8 C-suite reviews, accelerating launch readiness by 30%.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>'''
new = '''<section id="experience">
    <div class="container">
      <p class="section-label">Experience</p>
      <h2 class="section-title">Where I've <em>worked</em></h2>
      <div class="divider"></div>
      <div class="timeline-scroller">
        <div class="timeline-track"></div>
        <article class="exp-card current">
          <div class="exp-date">2026 — Present</div>
          <div class="exp-role">Applied AI Researcher · Data Science</div>
          <div class="exp-org">University at Buffalo, Dept. of AI & Society</div>
          <p class="exp-summary">Built reproducible pipelines for research data and supported AI bias/misinformation studies.</p>
          <ul class="exp-bullets">
            <li>Designed and maintained structured datasets from unstructured text sources.</li>
            <li>Automated ingestion, cleaning, and transformation in Python across multiple studies.</li>
          </ul>
        </article>
        <article class="exp-card">
          <div class="exp-date">2025 — Present</div>
          <div class="exp-role">Applied AI Researcher · Data Analyst</div>
          <div class="exp-org">UB Media Effects, Misinformation & Extremism Lab</div>
          <p class="exp-summary">Analyzed Reddit discourse and built NLP systems for AI governance research.</p>
          <ul class="exp-bullets">
            <li>Analyzed 20,000 Reddit posts to surface trust and concern signals.</li>
            <li>Fine-tuned RoBERTa and used BERTopic to reveal public narratives.</li>
          </ul>
        </article>
        <article class="exp-card">
          <div class="exp-date">2025 — Present</div>
          <div class="exp-role">Applied AI Researcher · Data Analyst</div>
          <div class="exp-org">UB Systems Biomedicine & Pharmaceutics Lab</div>
          <p class="exp-summary">Calibrated cancer migration simulations and optimized biological models.</p>
          <ul class="exp-bullets">
            <li>Fitted CompuCell3D simulations to experimental invasion data.</li>
            <li>Used Bayesian Optimization to reduce invalid proposals by 35%.</li>
          </ul>
        </article>
        <article class="exp-card">
          <div class="exp-date">2025</div>
          <div class="exp-role">Applied AI Researcher · Data Analyst</div>
          <div class="exp-org">UB School of Pharmacy & Pharmaceutical Sciences</div>
          <p class="exp-summary">Modeled physiological age and drug metabolism for decision support.</p>
          <ul class="exp-bullets">
            <li>Built XGBoost and Random Survival Forest models on NHANES data.</li>
            <li>Used SHAP to surface key clinical drivers.</li>
          </ul>
        </article>
        <article class="exp-card">
          <div class="exp-date">2024 — 2025</div>
          <div class="exp-role">Computer Vision Intern</div>
          <div class="exp-org">SETV Global</div>
          <p class="exp-summary">Supported model training with image preprocessing and augmentation.</p>
          <ul class="exp-bullets">
            <li>Prepared datasets with OpenCV and NumPy.</li>
            <li>Documented pipelines and presented updates in weekly reviews.</li>
          </ul>
        </article>
        <article class="exp-card">
          <div class="exp-date">2021 — 2023</div>
          <div class="exp-role">Business Intelligence Analyst</div>
          <div class="exp-org">SafetyConnect IOTRL</div>
          <p class="exp-summary">Turned market data and stakeholder insights into dashboards and strategy.</p>
          <ul class="exp-bullets">
            <li>Built forecasting dashboards and supported a Seed A raise.</li>
            <li>Designed KPI dashboards and presented findings to leadership.</li>
          </ul>
        </article>
      </div>
    </div>
  </section>'''
html = html.replace(old, new)
extra_css = '''
.timeline-scroller{position:relative;display:grid;gap:1.5rem;padding-left:1rem}
.timeline-track{position:absolute;left:1.2rem;top:0;bottom:0;width:2px;background:linear-gradient(to bottom, rgba(0,255,65,0.15), rgba(0,255,65,0.9), rgba(0,255,65,0.15))}
.exp-card{position:relative;margin-left:2.4rem;padding:1.7rem 1.8rem;border:1px solid rgba(0,255,65,0.16);background:rgba(255,255,255,0.03);backdrop-filter:blur(8px);border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,0.35);transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease}
.exp-card::before{content:"";position:absolute;left:-2.95rem;top:1.9rem;width:14px;height:14px;border-radius:50%;background:#000;border:2px solid var(--green);box-shadow:0 0 0 8px rgba(0,255,65,0.08)}
.exp-card:hover{transform:translateY(-4px);border-color:rgba(0,255,65,0.4);box-shadow:0 14px 50px rgba(0,0,0,0.5)}
.exp-card.current{border-color:rgba(0,255,65,0.45)}
.exp-date{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#888;margin-bottom:.55rem}
.exp-summary{margin:.8rem 0 1rem;color:#bbb;line-height:1.75;font-size:.92rem}
.exp-card .exp-role{font-family:"Cormorant Garamond",serif;font-size:1.6rem;color:var(--ink);line-height:1.15}
.exp-card .exp-org{font-size:.85rem;color:var(--green-mid);margin-top:.25rem;margin-bottom:0}
.exp-card .exp-bullets{margin-top:1rem}
.exp-card .exp-bullets li{color:#c9c9c9}
@media (max-width: 900px){.timeline-track{left:0.35rem}.exp-card{margin-left:1.2rem}.exp-card::before{left:-1.65rem}}
'''
html = html.replace('</style>', extra_css + '\n</style>')
Path('output/index-2-timeline.html').write_text(html, encoding='utf-8')
print('saved timeline')
