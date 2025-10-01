# Agent Synergy Matrix

Visual guide to understanding agent relationships, workflows, and optimal combinations.

## 🎯 The Agent Ecosystem Map

```
                    CLAUDE CODE AGENT ECOSYSTEM

┌─────────────────────────────────────────────────────────────────┐
│                     🎨 DESIGN & PLANNING                        │
│                                                                 │
│  architect-review ──→ backend-architect ──→ frontend-developer │
│         ↓                    ↓                      ↓          │
│  ui-ux-designer      graphql-architect         mobile-dev      │
│         ↓                    ↓                      ↓          │
│  business-analyst    cloud-architect          ios-developer    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   💻 IMPLEMENTATION LAYER                       │
│                                                                 │
│  [Language Specialists: 18 agents]                             │
│                                                                 │
│  javascript-pro  typescript-pro  python-pro   java-pro         │
│  golang-pro      rust-pro        cpp-pro      c-pro            │
│  ruby-pro        php-pro         scala-pro    csharp-pro       │
│  elixir-pro      django-pro      fastapi-pro  sql-pro          │
│  minecraft-bukkit-pro      unity-developer                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   🧪 QUALITY ASSURANCE LAYER                    │
│                                                                 │
│  test-automator ←──→ tdd-orchestrator                          │
│         ↓                    ↓                                 │
│  debugger            ui-visual-validator                       │
│         ↓                    ↓                                 │
│  error-detective     code-reviewer ←──→ security-auditor       │
│                              ↓                                 │
│  [Security Specialists]                                        │
│  backend-security-coder  frontend-security-coder               │
│  mobile-security-coder                                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                🚀 DEPLOYMENT & INFRASTRUCTURE                   │
│                                                                 │
│  terraform-specialist ←──→ cloud-architect                     │
│         ↓                         ↓                            │
│  kubernetes-architect    hybrid-cloud-architect                │
│         ↓                         ↓                            │
│  deployment-engineer     database-admin                        │
│         ↓                         ↓                            │
│  devops-troubleshooter   database-optimizer                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  📊 OBSERVABILITY & SRE                         │
│                                                                 │
│  observability-engineer ←──→ incident-responder ⚡              │
│         ↓                            ↓                         │
│  performance-engineer        network-engineer                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    🤖 AI/ML SPECIALIZATION                      │
│                                                                 │
│  prompt-engineer ──→ ai-engineer ──→ ml-engineer               │
│         ↓                 ↓               ↓                    │
│  data-scientist   mlops-engineer   data-engineer               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              📝 DOCUMENTATION & CONTENT                         │
│                                                                 │
│  docs-architect ──→ api-documenter ──→ tutorial-engineer       │
│         ↓                 ↓                    ↓               │
│  mermaid-expert   reference-builder    content-marketer        │
│                                                                 │
│  [SEO Squad: 10 agents]                                        │
│  seo-content-auditor → seo-keyword-strategist → seo-writer     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                  💼 BUSINESS & OPERATIONS                       │
│                                                                 │
│  business-analyst  customer-support  legal-advisor             │
│  hr-pro           sales-automator    quant-analyst             │
│  risk-manager     payment-integration                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Workflow Patterns

### Pattern 1: Top-Down (Architecture First)
```
architect-review
    ↓
backend-architect + frontend-developer (parallel)
    ↓
test-automator
    ↓
security-auditor
    ↓
deployment-engineer
```

### Pattern 2: Bottom-Up (TDD Approach)
```
test-automator (write tests)
    ↓
[language-pro] (implement)
    ↓
code-reviewer
    ↓
deployment-engineer
```

### Pattern 3: Security-First
```
security-auditor (analyze requirements)
    ↓
backend-security-coder + frontend-security-coder (parallel)
    ↓
test-automator (security tests)
    ↓
code-reviewer (final check)
```

### Pattern 4: Performance-Driven
```
performance-engineer (profile)
    ↓
database-optimizer (fix queries)
    ↓
observability-engineer (add metrics)
    ↓
[language-pro] (optimize code)
```

### Pattern 5: AI Product Development
```
prompt-engineer (design prompts)
    ↓
ai-engineer (integrate LLM)
    ↓
mlops-engineer (infrastructure)
    ↓
observability-engineer (monitoring)
```

---

## 🎭 Agent Role Relationships

```
                    DECISION MAKERS (Opus)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Architects         Analysts           Auditors
        │                  │                  │
  cloud-architect    data-scientist    security-auditor
  backend-architect  business-analyst  code-reviewer
  kubernetes-arch    prompt-engineer   incident-responder
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    IMPLEMENTERS (Sonnet)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Developers         Engineers          Specialists
        │                  │                  │
  frontend-developer  deployment-eng    test-automator
  mobile-developer    devops-trouble    api-documenter
  [language-pros]     network-eng       tutorial-eng
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ASSISTANTS (Haiku)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    SEO Tools         Utilities          Support
        │                  │                  │
  seo-meta-optimizer  context-manager   sales-automator
  seo-keyword-strat   reference-builder search-specialist
  [other seo agents]
```

---

## 🔗 Dependency Chains

### Chain 1: Full-Stack Feature
```
Step 1: architect-review (design validation)
        ↓ (provides architecture)
Step 2: backend-architect (API design)
        ↓ (defines contracts)
Step 3: frontend-developer (UI implementation)
        ↓ (creates features)
Step 4: test-automator (test suite)
        ↓ (ensures quality)
Step 5: security-auditor (security scan)
        ↓ (approves security)
Step 6: deployment-engineer (ship it)
```

### Chain 2: Data Pipeline
```
Step 1: data-scientist (analyze requirements)
        ↓ (defines transformations)
Step 2: data-engineer (build pipeline)
        ↓ (creates infrastructure)
Step 3: database-optimizer (optimize queries)
        ↓ (monitors performance)
Step 4: observability-engineer (add monitoring)
        ↓ (tracks metrics)
Step 5: business-analyst (create dashboards)
```

### Chain 3: Infrastructure Automation
```
Step 1: cloud-architect (design infrastructure)
        ↓ (creates blueprints)
Step 2: terraform-specialist (write IaC)
        ↓ (defines resources)
Step 3: kubernetes-architect (container orchestration)
        ↓ (configures cluster)
Step 4: observability-engineer (monitoring setup)
        ↓ (adds observability)
Step 5: deployment-engineer (CI/CD pipeline)
```

---

## 💎 Diamond Patterns (Parallel → Merge)

### Diamond 1: Security Review
```
                 security-auditor
                 /              \
    backend-security-coder  frontend-security-coder
                 \              /
                 code-reviewer
```

### Diamond 2: Full-Stack Development
```
              architect-review
              /              \
    backend-architect    frontend-developer
              \              /
              test-automator
```

### Diamond 3: Documentation Complete
```
               docs-architect
              /      |       \
    api-documenter  tutorial-engineer  mermaid-expert
              \      |       /
            reference-builder
```

### Diamond 4: ML Lifecycle
```
              data-scientist
              /            \
        ml-engineer    mlops-engineer
              \            /
           ai-engineer (integration)
```

---

## 🌟 Star Patterns (Hub & Spoke)

### Hub: code-reviewer (connects to all)
```
                    code-reviewer
                    /    |    \
                   /     |     \
          security-   test-   performance-
           auditor   automator  engineer
              |         |          |
         [security] [quality]  [speed]
```

### Hub: observability-engineer
```
              observability-engineer
              /      |      |      \
             /       |      |       \
      incident-  performance- database-  network-
      responder   engineer    optimizer   engineer
```

### Hub: architect-review
```
                architect-review
                /      |      \
               /       |       \
      backend-    cloud-     kubernetes-
      architect   architect   architect
```

---

## 🎯 Specialization Clusters

### Cluster 1: Security Fortress
```
┌──────────────────────────────────┐
│    SECURITY SPECIALIZATION       │
│                                  │
│  security-auditor (entry point)  │
│         ├─ backend-security-coder│
│         ├─ frontend-security-coder│
│         └─ mobile-security-coder │
│                                  │
│  Supported by:                   │
│    • code-reviewer               │
│    • architect-review            │
└──────────────────────────────────┘
```

### Cluster 2: AI/ML Excellence
```
┌──────────────────────────────────┐
│    AI/ML SPECIALIZATION          │
│                                  │
│  prompt-engineer (strategy)      │
│  ai-engineer (integration)       │
│  ml-engineer (models)            │
│  mlops-engineer (infrastructure) │
│  data-scientist (analysis)       │
│  data-engineer (pipelines)       │
└──────────────────────────────────┘
```

### Cluster 3: SEO Powerhouse
```
┌──────────────────────────────────┐
│    SEO SPECIALIZATION            │
│                                  │
│  seo-content-auditor (analyze)   │
│  seo-keyword-strategist (plan)   │
│  seo-content-writer (create)     │
│  seo-meta-optimizer (optimize)   │
│  seo-structure-architect (build) │
│  + 5 more specialized SEO agents │
└──────────────────────────────────┘
```

### Cluster 4: Infrastructure Core
```
┌──────────────────────────────────┐
│  INFRASTRUCTURE SPECIALIZATION   │
│                                  │
│  cloud-architect (design)        │
│  terraform-specialist (code)     │
│  kubernetes-architect (orchestr.)│
│  deployment-engineer (delivery)  │
│  devops-troubleshooter (debug)   │
│  network-engineer (connectivity) │
└──────────────────────────────────┘
```

---

## 🔥 Critical Path Agents

Agents that are often bottlenecks or critical decision points:

```
MUST-HAVE for Production:
┌────────────────────────────────────────────┐
│ 1. security-auditor      (gate keeper)     │
│ 2. code-reviewer         (quality gate)    │
│ 3. incident-responder    (crisis response) │
│ 4. observability-engineer (visibility)     │
│ 5. database-optimizer    (performance)     │
└────────────────────────────────────────────┘

HIGH-VALUE for Development:
┌────────────────────────────────────────────┐
│ 1. architect-review      (early validation)│
│ 2. test-automator        (quality)         │
│ 3. backend-architect     (API design)      │
│ 4. frontend-developer    (UX delivery)     │
│ 5. deployment-engineer   (shipping)        │
└────────────────────────────────────────────┘

EFFICIENCY MULTIPLIERS:
┌────────────────────────────────────────────┐
│ 1. prompt-engineer       (AI optimization) │
│ 2. terraform-specialist  (automation)      │
│ 3. docs-architect        (knowledge)       │
│ 4. performance-engineer  (speed)           │
│ 5. dx-optimizer          (dev experience)  │
└────────────────────────────────────────────┘
```

---

## 🎲 Agent Selection Decision Tree

```
START: What are you building?

├─ Web Application
│  ├─ Frontend heavy → frontend-developer + ui-ux-designer
│  ├─ API service → backend-architect + api-documenter
│  └─ Full-stack → architect-review → both paths
│
├─ Mobile App
│  ├─ Cross-platform → mobile-developer or flutter-expert
│  ├─ iOS native → ios-developer
│  └─ With backend → backend-architect + mobile choice
│
├─ AI/ML Feature
│  ├─ LLM integration → prompt-engineer + ai-engineer
│  ├─ ML model → data-scientist + ml-engineer
│  └─ Production ML → + mlops-engineer
│
├─ Infrastructure
│  ├─ Cloud setup → cloud-architect + terraform-specialist
│  ├─ Kubernetes → kubernetes-architect
│  └─ Database → database-admin + database-optimizer
│
├─ Data Pipeline
│  ├─ Analytics → data-scientist + business-analyst
│  ├─ ETL → data-engineer + database-optimizer
│  └─ Real-time → data-engineer + observability-engineer
│
├─ Documentation
│  ├─ Technical docs → docs-architect
│  ├─ API docs → api-documenter
│  └─ Tutorials → tutorial-engineer
│
└─ Emergency!
   ├─ Production down → incident-responder ⚡
   ├─ Security breach → security-auditor
   ├─ Performance issue → performance-engineer
   └─ Database problem → database-optimizer
```

---

## 📊 Skill Transfer Map

Agents that work well together due to overlapping knowledge:

```
Easy Transitions (Similar Skills):
• backend-architect ↔ graphql-architect
• frontend-developer ↔ mobile-developer
• cloud-architect ↔ kubernetes-architect
• ml-engineer ↔ mlops-engineer
• test-automator ↔ tdd-orchestrator

Complementary Pairs (Cover gaps):
• architect-review + code-reviewer
• security-auditor + performance-engineer
• data-scientist + data-engineer
• prompt-engineer + ai-engineer
• docs-architect + api-documenter

Learning Paths:
Junior → Senior → Expert
• debugger → code-reviewer → architect-review
• test-automator → tdd-orchestrator → performance-engineer
• api-documenter → docs-architect → tutorial-engineer
```

---

Generated by agent ecosystem analysis | Optimized for workflow efficiency
