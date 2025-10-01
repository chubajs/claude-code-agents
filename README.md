# Claude Code Subagents Collection

A comprehensive collection of **84 specialized AI subagents** for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), organized by domain expertise.

## 🗂️ Agent Categories

All agents are organized into folders for easy navigation:

### 📐 [Architecture & System Design](agents/architecture/) - 12 agents
Design systems, build applications, and architect solutions.
- **Core**: backend-architect, frontend-developer, graphql-architect, architect-review
- **Cloud**: cloud-architect, hybrid-cloud-architect, kubernetes-architect
- **UI/Mobile**: ui-ux-designer, mobile-developer, ios-developer, flutter-expert, ui-visual-validator

### 💻 [Programming Languages](agents/languages/) - 16 agents
Language-specific expertise from systems to web development.
- **Systems**: c-pro, cpp-pro, rust-pro, golang-pro
- **Web**: javascript-pro, typescript-pro, python-pro, ruby-pro, php-pro, sql-pro
- **Enterprise**: java-pro, scala-pro, csharp-pro
- **Frameworks**: elixir-pro, django-pro, fastapi-pro

### 🏗️ [Infrastructure & Operations](agents/infrastructure/) - 10 agents
DevOps, databases, and site reliability engineering.
- **DevOps**: devops-troubleshooter, deployment-engineer, terraform-specialist, dx-optimizer
- **Databases**: database-optimizer, database-admin
- **SRE**: incident-responder ⚡, observability-engineer, performance-engineer, network-engineer

### 🛡️ [Quality & Security](agents/quality-security/) - 9 agents
Code review, security, and comprehensive testing.
- **Review**: code-reviewer, debugger, error-detective
- **Security**: security-auditor, backend-security-coder, frontend-security-coder, mobile-security-coder
- **Testing**: test-automator, tdd-orchestrator

### 🤖 [Data & AI](agents/data-ai/) - 6 agents
Complete ML/AI lifecycle from research to production. **All Opus models.**
- data-scientist, data-engineer
- ai-engineer, ml-engineer, mlops-engineer
- prompt-engineer

### 📝 [Documentation & Content](agents/documentation/) - 6 agents
Technical writing and content creation.
- docs-architect, api-documenter, tutorial-engineer
- reference-builder, mermaid-expert, content-marketer

### 💼 [Business & Operations](agents/business/) - 7 agents
Analytics, finance, HR, legal, and customer ops.
- **Analysis**: business-analyst, quant-analyst, risk-manager
- **Sales/Support**: sales-automator, customer-support
- **Compliance**: hr-pro, legal-advisor

### 🎯 [SEO & Content Optimization](agents/seo/) - 10 agents
**Highest capability density** in the entire collection.
- Complete SEO workflow from audit to authority building
- All agents: content-auditor, meta-optimizer, keyword-strategist, structure-architect, snippet-hunter, content-refresher, cannibalization-detector, authority-builder, content-writer, content-planner

### ⚙️ [Specialized Domains](agents/specialized/) - 8 agents
Unique platforms and use cases.
- blockchain-developer, payment-integration, legacy-modernizer
- context-manager, unity-developer, minecraft-bukkit-pro, quasar-developer, search-specialist

---

## 🚀 Quick Start

### Installation
```bash
cd ~/.claude
git clone https://github.com/wshobson/agents.git
```

Agents are automatically available in Claude Code once placed in `~/.claude/agents/`.

### Usage

**Automatic**: Claude Code selects agents based on context
```
"Build a React dashboard with authentication"
→ Auto-activates: frontend-developer, backend-architect
```

**Explicit**: Specify agents by name
```
"Use security-auditor to scan for vulnerabilities"
"Have prompt-engineer optimize my LLM prompts"
```

---

## 📊 Model Distribution

| Model | Count | Use Case |
|-------|-------|----------|
| **Haiku** | 12 | Quick, focused tasks (SEO, context, search) |
| **Sonnet** | 47 | Standard development and engineering |
| **Opus** | 26 | Complex reasoning, architecture, critical analysis |

**Special Note**:
- Only **1 agent** uses IMMEDIATE activation: `incident-responder` ⚡ (for production crises)
- **80 agents** are PROACTIVE (designed to activate automatically)

---

## 🎯 Navigation Guides

### Quick References
- **[CATALOG.md](CATALOG.md)** - User-friendly quick reference by use case, skill level, and project phase
- **[AGENT-MATRIX.md](AGENT-MATRIX.md)** - Visual ecosystem map with workflows and relationships
- **[catalog-analysis.py](catalog-analysis.py)** - Advanced analysis tool for agent metrics

### Folder READMEs
Each category folder contains:
- Complete agent list with descriptions
- Common workflow patterns
- Use case selection guide
- Integration points
- Power combinations

---

## 🔗 Common Workflows

### Full-Stack Feature
```
architect-review → backend-architect → frontend-developer → test-automator → security-auditor → deployment-engineer
```

### Production Incident
```
incident-responder ⚡ → devops-troubleshooter → observability-engineer
```

### AI/ML Development
```
prompt-engineer → ai-engineer → ml-engineer → mlops-engineer
```

### Security Hardening
```
security-auditor → [backend + frontend + mobile]-security-coder → code-reviewer
```

### Infrastructure Setup
```
cloud-architect → terraform-specialist → kubernetes-architect → observability-engineer
```

---

## 🏆 Featured Agents

### Most Comprehensive
1. **prompt-engineer** (250 lines, 150 capabilities) - LLM optimization master
2. **observability-engineer** (210 lines, 156 capabilities) - Production monitoring expert
3. **unity-developer** (207 lines, 148 capabilities) - Game development specialist
4. **test-automator** (203 lines, 143 capabilities) - Quality assurance champion
5. **mlops-engineer** (197 lines, 140 capabilities) - ML infrastructure architect

### Highest Specialization
1. **seo-authority-builder** - 59 capabilities/section
2. **seo-content-refresher** - 48 capabilities/section
3. **seo-cannibalization-detector** - 43 capabilities/section

### Critical Path Agents
- **incident-responder** ⚡ - Only IMMEDIATE activation agent
- **security-auditor** - Security gateway
- **code-reviewer** - Quality gateway
- **observability-engineer** - Production visibility
- **database-optimizer** - Performance critical

---

## 💡 Power Combinations

| Combo | Agents | Purpose |
|-------|--------|---------|
| **Security Gate** | code-reviewer + security-auditor | Pre-deployment check |
| **AI Dream Team** | prompt-engineer + ai-engineer + mlops-engineer | LLM to production |
| **Performance** | performance-engineer + database-optimizer | Eliminate bottlenecks |
| **Infrastructure** | cloud-architect + terraform-specialist | Cloud automation |
| **Quality First** | tdd-orchestrator + test-automator | TDD workflow |
| **Documentation** | docs-architect + api-documenter + tutorial-engineer | Complete docs |
| **SEO Campaign** | Full SEO folder (10 agents) | Complete SEO strategy |

---

## 🎓 Learning Paths

### Beginner → Expert

**Beginner** (Low complexity, quick wins):
- sales-automator, debugger, error-detective, mermaid-expert, reference-builder

**Intermediate** (Standard development):
- frontend-developer, api-documenter, tutorial-engineer, business-analyst, customer-support

**Advanced** (Deep expertise):
- backend-architect, cloud-architect, data-scientist, kubernetes-architect, test-automator

**Expert** (Maximum complexity):
- observability-engineer, prompt-engineer, mlops-engineer, incident-responder, security-auditor

---

## 🔧 Tech Stack Coverage

- **Kubernetes**: 24 agents
- **Databases**: 21 agents
- **AWS**: 20 agents
- **React**: 16 agents
- **Monitoring**: 14 agents
- **GCP**: 13 agents
- **Testing**: 11 agents
- **Azure**: 10 agents
- **Python ML**: 7 agents

---

## 📚 Additional Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Subagents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Claude Code Commands](https://github.com/wshobson/commands) - 52 pre-built slash commands
- [TDD Usage Examples](examples/tdd-usage.md)

---

## 🤝 Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for guidelines on:
- Adding new agents
- Improving existing agents
- Quality standards
- Community guidelines

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🎯 Quick Selection Guide

**Need to...**
- Build an API? → `agents/architecture/backend-architect.md`
- Fix production issue? → `agents/infrastructure/incident-responder.md` ⚡
- Optimize ML model? → `agents/data-ai/ml-engineer.md`
- Security review? → `agents/quality-security/security-auditor.md`
- Write documentation? → `agents/documentation/docs-architect.md`
- Improve SEO? → `agents/seo/` (entire folder)
- Modernize legacy code? → `agents/specialized/legacy-modernizer.md`

---

<div align="center">

**84 Agents • 9 Categories • Production Ready**

[Browse Agents](agents/) • [View Workflows](AGENT-MATRIX.md) • [Quick Reference](CATALOG.md)

</div>
