# Day-to-Day Operations Guide

## Table of Contents
1. [Problem Discovery & Stakeholder Management](#problem-discovery--stakeholder-management)
2. [Project Structure & Planning](#project-structure--planning)
3. [Analysis Execution & Quality Control](#analysis-execution--quality-control)
4. [Communication & Reporting](#communication--reporting)
5. [Experiment Design & Implementation](#experiment-design--implementation)
6. [Cross-functional Collaboration](#cross-functional-collaboration)
7. [Quick Reference Checklists](#quick-reference-checklists)

---

## Problem Discovery & Stakeholder Management

### The Initial Stakeholder Meeting Framework

**Always start with these questions:**
- "What business decision are you trying to make with this analysis?"
- "What would success look like? How would you measure it?"
- "What's your hypothesis going in?"
- "What would change your mind about this hypothesis?"
- "When do you need this by, and what's driving that timeline?"

### Extracting the Real Problem

**Red flags that indicate unclear requirements:**
- Requests that start with "Can you just pull some data on..."
- Vague asks like "We need to understand our customers better"
- Solution-oriented requests: "We need a dashboard showing X"

**Techniques to dig deeper:**
1. **The 5 Whys**: Keep asking "why" to get to root cause
2. **Scenario Planning**: "If the data showed X, what would you do? What about Y?"
3. **Constraint Identification**: "What can't we change? What are we optimizing for?"

### Scope Definition Template

```
Business Question: [One clear sentence]
Success Metrics: [Specific, measurable outcomes]
Key Stakeholders: [Decision makers and their roles]
Timeline: [Deadline and key milestones]
Constraints: [Technical, business, or resource limitations]
Out of Scope: [What we're explicitly NOT doing]
```

### Managing Pushback and Expectations

**Common pushback scenarios:**
- "This will take too long" → Break into phases, deliver quick wins first
- "We need more detailed data" → Explain diminishing returns, cost/benefit
- "Can you just add one more thing?" → Scope creep management

**Professional responses:**
- "I want to make sure we're solving the right problem first..."
- "Let me walk you through the trade-offs here..."
- "Based on similar analyses, here's what I'd expect in terms of timeline..."

---

## Project Structure & Planning

### Standard Project Methodology

#### 1. Discovery Phase (20% of time)
- Stakeholder interviews
- Problem definition
- Data availability assessment
- Success criteria alignment

#### 2. Planning Phase (30% of time)
- Hypothesis development
- Analysis plan creation
- Risk identification
- Resource allocation

#### 3. Execution Phase (30% of time)
- Data collection and cleaning
- Analysis execution
- Quality checks and validation
- Peer review

#### 4. Communication Phase (20% of time)
- Results synthesis
- Recommendation development
- Presentation creation
- Follow-up planning

### Ticket Creation Best Practices

**For your own work:**
```
Title: [Business Question] - [Analysis Type]
Description: 
- Business Context: Why this matters
- Specific Ask: What we're delivering
- Success Criteria: How we'll know it's done
- Dependencies: What we need from others
- Timeline: Key dates and milestones
```

**For product/engineering requests:**
```
Title: [Feature/Change Request] - [Impact]
User Story: As a [user type], I want [functionality] so that [benefit]
Acceptance Criteria: 
- [ ] Specific, testable requirements
- [ ] Edge cases covered
- [ ] Success metrics defined
Technical Requirements:
- Data sources needed
- Performance requirements
- Integration points
```

### Risk Assessment Framework

**Technical Risks:**
- Data quality issues
- System performance constraints
- Integration complexity

**Business Risks:**
- Changing requirements
- Stakeholder alignment
- Timeline pressures

**Mitigation Strategies:**
- Build in buffer time (20-30%)
- Create fallback options
- Set up regular check-ins

---

## Analysis Execution & Quality Control

### Pre-Analysis Checklist

**Before you start coding:**
- [ ] Do I understand the business question?
- [ ] Have I documented my assumptions?
- [ ] Do I know what "good" looks like?
- [ ] Have I identified potential biases?
- [ ] Do I have the right data sources?

### The CRISP Mental Model for Every Analysis

**C - Context**: What's the business situation?
**R - Requirements**: What exactly are we measuring?
**I - Investigation**: What does the data actually show?
**S - Synthesis**: What does this mean for the business?
**P - Prescription**: What should we do about it?

### Data Quality Validation Steps

**Always check:**
1. **Completeness**: Missing data patterns, time gaps
2. **Consistency**: Same metrics across different sources
3. **Reasonableness**: Order of magnitude checks, trend validation
4. **Freshness**: When was data last updated?
5. **Granularity**: Right level of detail for the question

### Common Analytical Pitfalls to Avoid

**Statistical Pitfalls:**
- Simpson's Paradox (aggregation level effects)
- Selection bias in cohort analyses
- Survivorship bias in user behavior studies
- Multiple comparison problems

**Business Logic Pitfalls:**
- Confusing correlation with causation
- Ignoring seasonality patterns
- Not accounting for external factors
- Assuming linear relationships

### Validation Techniques

**Sanity Checks:**
- Compare totals to known benchmarks
- Check for impossible values (negative time, >100% rates)
- Validate against prior analyses
- Cross-check with different data sources

**Sensitivity Analysis:**
- How do results change with different assumptions?
- What if we exclude outliers?
- How robust are findings to time period selection?

---

## Communication & Reporting

### Audience-Specific Report Formats

#### Executive Summary (C-Suite/VP Level)
```
Structure:
1. Key Finding (1 sentence)
2. Business Impact (metrics/money)
3. Recommended Action (what to do)
4. Supporting Evidence (brief)
5. Next Steps (timeline/owners)

Length: 1 page maximum
Focus: Business outcomes, not methodology
```

#### Technical Report (Peer Review/Data Science)
```
Structure:
1. Problem Statement
2. Methodology & Assumptions
3. Data Sources & Limitations
4. Detailed Results
5. Statistical Significance
6. Robustness Checks
7. Technical Appendix

Length: 5-10 pages
Focus: Reproducibility and rigor
```

#### Product Team Report (PM/Engineering)
```
Structure:
1. User Impact Summary
2. Key Metrics Movement
3. Feature Performance Breakdown
4. Actionable Insights
5. Product Recommendations
6. Technical Implementation Notes

Length: 2-3 pages
Focus: Product decisions and user behavior
```

### Storytelling Framework: SCQA

**S - Situation**: What's the current state?
**C - Complication**: What's the problem/opportunity?
**Q - Question**: What should we do about it?
**A - Answer**: Here's what the data shows we should do

### Visualization Best Practices

**Chart Selection:**
- Trends over time → Line charts
- Comparisons → Bar charts
- Distributions → Histograms
- Relationships → Scatter plots
- Parts of whole → Stacked charts (avoid pie charts)

**Design Principles:**
- Direct labeling over legends
- Consistent color schemes
- Clear, descriptive titles
- Annotations for key insights
- Remove chart junk

---

## Experiment Design & Implementation

### End-to-End Experiment Workflow

#### 1. Experiment Planning
```
Business Hypothesis: What we think will happen and why
Success Metrics: Primary and secondary KPIs
Sample Size Calculation: Power analysis
Randomization Strategy: How we'll split users
Duration Planning: Minimum viable test period
```

#### 2. Technical Implementation
```
Experiment Setup:
- Feature flag configuration
- User assignment logic
- Data collection points
- Quality assurance testing

Pre-Launch Checklist:
- [ ] A/A test passed
- [ ] Sample ratio mismatch check
- [ ] Data pipeline validation
- [ ] Stakeholder sign-off
```

#### 3. Monitoring & Analysis
```
Daily Monitoring:
- Sample ratio checks
- Data quality validation
- Early anomaly detection
- Performance impact assessment

Analysis Framework:
- Primary metric significance
- Secondary metric movement
- Segment-level analysis
- Long-term impact projection
```

### Experiment Documentation Template

```markdown
# Experiment: [Name]
**Dates**: [Start] - [End]
**Status**: [Planning/Running/Complete]

## Hypothesis
We believe that [change] will result in [outcome] because [reasoning].

## Success Metrics
- Primary: [metric] with [X]% improvement target
- Secondary: [list other important metrics]
- Guardrail: [metrics we can't hurt]

## Design
- **Type**: [A/B test, multivariate, etc.]
- **Sample Size**: [users/sessions needed]
- **Duration**: [timeline and reasoning]
- **Traffic Split**: [percentage allocation]

## Results
- **Primary Outcome**: [statistical significance and practical significance]
- **Secondary Outcomes**: [summary of other metrics]
- **Segments**: [any interesting segment differences]

## Recommendation
[Launch/Don't Launch/Iterate] because [reasoning based on data]

## Next Steps
[Follow-up actions and timeline]
```

---

## Cross-functional Collaboration

### Working with Data Scientists

**Strategy Planning Sessions:**
- Focus on business value, not just technical feasibility
- Discuss model interpretability requirements upfront
- Align on success metrics and validation approaches
- Plan for model maintenance and monitoring

**Technical Collaboration:**
- Understand model assumptions and limitations
- Provide business context for feature engineering
- Help translate model outputs into business insights
- Bridge communication between DS team and stakeholders

### AI/ML Product Development

**Requirements Gathering:**
```
Business Requirements:
- What business problem are we solving?
- How will this create value?
- What are the success criteria?

Technical Requirements:
- Data availability and quality
- Latency and performance needs
- Integration requirements
- Monitoring and alertability
```

**Go-to-Market Planning:**
- User adoption strategy
- Success measurement framework
- Rollback procedures
- Performance monitoring

---

## Quick Reference Checklists

### Starting Any New Project
- [ ] Do I understand the business decision being made?
- [ ] Have I confirmed data availability?
- [ ] Are success criteria clearly defined?
- [ ] Have I identified key stakeholders?
- [ ] Is the timeline realistic?
- [ ] Have I documented assumptions?

### Before Presenting Results
- [ ] Do my conclusions directly answer the business question?
- [ ] Have I checked for statistical significance?
- [ ] Are my visualizations clear and accurate?
- [ ] Have I considered alternative explanations?
- [ ] Do I have actionable recommendations?
- [ ] Have I prepared for likely follow-up questions?

### Code Quality for Production
- [ ] Code is readable and well-commented
- [ ] Functions are modular and reusable
- [ ] Data sources and assumptions are documented
- [ ] Results are reproducible
- [ ] Version control is used properly
- [ ] Peer review has been completed

### Meeting Preparation
- [ ] Agenda shared in advance
- [ ] Key questions prepared
- [ ] Supporting materials ready
- [ ] Follow-up actions planned
- [ ] Decision makers included
- [ ] Technical backup prepared

---

## Emergency Responses

### "This analysis looks wrong"
1. Don't get defensive
2. "Let me walk through my methodology..."
3. "What specifically seems off to you?"
4. "Let's validate this together"
5. Document any corrections needed

### "We need this by tomorrow"
1. "Help me understand the urgency..."
2. "Here's what I can deliver by tomorrow vs. next week..."
3. "What's the minimum viable analysis for your decision?"
4. Always deliver something, even if preliminary

### "Can you just change this one number?"
1. "Let me understand the impact of that change..."
2. "Here are the assumptions that would need to change..."
3. "Would you like me to run a sensitivity analysis?"
4. Document any assumption changes clearly
