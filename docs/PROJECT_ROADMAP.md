# Project Roadmap: IHS DeepRacer Engineering Expo 2026

---

## Overview

This document outlines the vision for the IHS DeepRacer project across three phases. Each phase builds on the previous, adding complexity, sophistication, and competitive capability.

---

## Phase 1: Lane Following "Hello World"

**Status:** 🔄 In Progress  
**Target Date:** April 25, 2026 (Expo)  
**Objective:** Build a basic lane-following model; demonstrate that the team can program AWS DeepRacer and train an autonomous model.

### Key Achievements
- ✅ Working reward function (center-line logic)
- ✅ Local testing infrastructure (`train.py`)
- ✅ Complete documentation (student-friendly)
- ✅ Successful AWS training job
- ✅ Memorable expo demo
- ✅ Foundational understanding of reinforcement learning

### Scope
- Single reward function (center-line + speed + smoothness)
- Single track (AWS default)
- Manual AWS console workflow
- ~2 hours training per model

### Success Criteria
- Car completes lap while staying mostly centered
- Demo explainable in < 2 minutes
- Code is clean and well-commented
- Team can answer reward function questions confidently

---

## Phase 2: Advanced Strategies & Multi-Track Mastery

**Status:** 📋 Planned  
**Target Date:** May-June 2026  
**Objective:** Develop more sophisticated reward functions; train models for multiple tracks; optimize for speed and strategy.

### Key Features
- **Multi-Track Support** — Build track-specific strategies
- **Hybrid Rewards** — Combine speed + safety + smoothness
- **Automated Pipeline** — AWS CLI integration for faster iteration
- **Model Versioning** — Track performance across iterations
- **Video Analysis** — Analyze trained model behavior
- **Parameter Tuning** — Optimize hyperparameters

### Scope
- 3–5 custom reward functions (each with different strategy)
- 2–3 different AWS tracks
- Comparative performance analysis
- Team-specific strategies (draft)
- ~10 hours total training

### Deliverables
- [ ] 5 trained models with documented strategies
- [ ] Performance comparison chart (lap time, success rate)
- [ ] AWS CLI automation scripts
- [ ] Model versioning system
- [ ] Strategy documentation for each model

### Success Criteria
- Best model completes lap in < 60 seconds
- Consistent lap completion (90%+ success rate)
- Clear differentiation between strategies
- Training automation works smoothly

---

## Phase 3: Competition Preparation & Optimization

**Status:** 📋 Planned  
**Target Date:** July-August 2026  
**Objective:** Prepare for actual AWS DeepRacer competition; optimize for winning; deploy best model to physical car hardware (optional).

### Key Features
- **Competition-Grade Models** — Optimized for real DeepRacer league
- **Ensemble Methods** — Combine multiple models
- **Real Hardware Testing** — Test on physical DeepRacer (if available)
- **Advanced Tactics** — Aggressive cornering, slipstreaming, collision avoidance
- **Analytics Dashboard** — Real-time training metrics
- **Community Engagement** — Share strategies with other teams

### Scope
- 10+ trained models (each highly specialized)
- 5+ different tracks
- Continuous improvement cycle
- Model ensemble voting
- Physical car deployment (optional)

### Deliverables
- [ ] Final competition model
- [ ] Strategy documentation (what worked, what didn't)
- [ ] Analytics & performance dashboard
- [ ] Team presentation for competition
- [ ] Post-mortem & lessons learned

### Success Criteria
- Model performs well in AWS DeepRacer league/competition
- Competitive with other teams
- All strategies documented for future reference
- Team learns advanced ML concepts in practice

---

## Long-Term Vision (Future Phases)

### Phase 4: Real-World Applications (Q4 2026+)
- Deploy models to physical autonomous robots
- Multi-agent training (cooperative driving)
- Real-world sensor integration

### Phase 5: Production & Deployment (2027+)
- End-to-end ML pipeline
- Model monitoring and retraining
- Student contributions to open-source DeepRacer community

---

## Timeline

```
April 2026
├── Phase 1 Launch
├── └── Apr 25: Expo Demo ✨
│
May-June 2026
├── Phase 2 Development
├── ├── May 1: Multi-track training starts
├── ├── May 15: Model versioning system live
├── └── Jun 1: 5 models trained & compared
│
July-August 2026
├── Phase 3 Competition Prep
├── ├── Jul 1: Competition models finalized
├── ├── Jul 15: Physical car testing (optional)
├── └── Aug 1: Ready for competition
│
September 2026+
├── Post-Competition Analysis
├── Phase 4 & 5 Planning
└── Community Contributions
```

---

## Technology Stack

### Phase 1
- **Language:** Python 3.7+
- **Testing:** Local (train.py)
- **Deployment:** AWS DeepRacer Console (manual)
- **Tools:** Git, GitHub, Markdown

### Phase 2
- **AWS CLI** — Automated job submission
- **Boto3** — Python AWS SDK
- **Pandas** — Data analysis
- **Matplotlib** — Visualization

### Phase 3
- **Scikit-learn** — Ensemble methods
- **TensorFlow/Keras** — Model inspection
- **Docker** — Reproducible environments
- **MLflow** — Experiment tracking

---

## Team Roles

| Role | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| **ML Engineer** | Reward function design | Model optimization | Competition strategy |
| **DevOps** | Git workflow | AWS automation | Infrastructure scaling |
| **Data Analyst** | Local testing | Performance analysis | Meta-analysis |
| **Documentation** | Code comments | Strategy docs | Team presentation |
| **Demo Lead** | Expo presentation | Strategic explanation | Competition liaison |

---

## Risk Management

| Risk | Phase | Mitigation |
|------|-------|-----------|
| AWS costs exceed budget | 1-3 | Monitor spending; use free tier; batch jobs |
| Model doesn't train well | 1-3 | Validate locally; start simple; iterate |
| Competition model overfits | 3 | Cross-validation; test on multiple tracks |
| Team loses momentum | 1-3 | Regular check-ins; celebrate milestones |
| Hardware becomes unavailable | 3 | Plan alternative (simulation only) |

---

## Success Metrics

### Phase 1
- ✅ Expo demo is memorable and well-executed
- ✅ Students understand reward functions
- ✅ Car completes lap successfully

### Phase 2
- ✅ Multiple trained models with clear strategy differences
- ✅ Performance improvements measurable
- ✅ AWS automation works reliably

### Phase 3
- ✅ Competitive performance in DeepRacer league
- ✅ Team can explain winning strategy
- ✅ Knowledge documented for future students

---

## Budget Estimate

| Item | Phase 1 | Phase 2 | Phase 3 | Notes |
|------|---------|---------|---------|-------|
| AWS DeepRacer free tier | Free | Free | Free | Covers basic training |
| AWS training hours (if beyond free tier) | $0 | $20–50 | $50–100 | Monitor spending |
| Development time (estimated) | 20 hrs | 40 hrs | 60 hrs | Team effort |
| Physical car (optional) | N/A | N/A | $300–400 | One-time if purchased |

---

## Learning Objectives by Phase

### Phase 1 Students Will Learn:
- How reward functions guide AI behavior
- Basic reinforcement learning concepts
- Python programming for ML applications
- AWS service basics
- Presentation and demo skills

### Phase 2 Students Will Learn:
- Advanced reward function design
- Comparative analysis and optimization
- AWS automation (CLI, SDKs)
- Performance profiling
- Version control for ML models

### Phase 3 Students Will Learn:
- Ensemble machine learning methods
- Real-time inference and monitoring
- Production ML pipelines
- Competition strategy and game theory
- Professional presentations

---

## Success Stories & Milestones to Celebrate

- ✨ First local test success (Phase 1)
- ✨ AWS training job completion (Phase 1)
- ✨ First successful lap (Phase 1)
- ✨ Expo demo completion (Phase 1)
- ✨ 3-model ensemble training (Phase 2)
- ✨ Multi-track strategy comparison published (Phase 2)
- ✨ Competition registration (Phase 3)
- ✨ Final competition model deployed (Phase 3)

---

## Appendix: Getting Involved

### For Students
- Join the IHS Engineering Club
- Attend Phase 1 kickoff meeting
- Contribute to GitHub repository
- Participate in weekly check-ins

### For Mentors
- Guide architecture decisions
- Review reward functions
- Support AWS deployment
- Coach demo preparation

### For Teachers
- Integrate project into curriculum
- Highlight student work at expo
- Support team logistics
- Connect to career pathways

---

## Questions & Updates

**Last Updated:** April 4, 2026  
**Next Review:** April 15, 2026 (Phase 1 mid-point check)  
**Contact:** [Mentor Name]

---

**Approved By:**  
Project Lead: ________________ Date: ________  
Mentor: ___________________ Date: ________
