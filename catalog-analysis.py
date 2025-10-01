#!/usr/bin/env python3
"""
Clever Catalog Sorting & Analysis for Claude Code Agents
Provides multiple views and classifications of the agent ecosystem
"""

import re
import glob
from collections import defaultdict

def parse_agents():
    """Parse all agent files and extract metadata"""
    agents = {}
    for file in glob.glob("*.md"):
        if file == "README.md":
            continue

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

            name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
            model_match = re.search(r'^model:\s*(.+)$', content, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)

            if name_match:
                name = name_match.group(1).strip()

                # Count capabilities (lines starting with -)
                capabilities = len(re.findall(r'^\s*-\s+', content, re.MULTILINE))

                # Count sections (###)
                sections = len(re.findall(r'^###\s+', content, re.MULTILINE))

                # Line count
                lines = len(content.split('\n'))

                agents[name] = {
                    'model': model_match.group(1).strip() if model_match else 'unknown',
                    'desc': desc_match.group(1).strip() if desc_match else '',
                    'file': file,
                    'capabilities': capabilities,
                    'sections': sections,
                    'lines': lines,
                    'content': content
                }

    return agents

def workflow_chains(agents):
    """Identify common agent workflow chains"""
    print("\n" + "="*70)
    print("🔗 COMMON WORKFLOW CHAINS")
    print("="*70 + "\n")

    chains = {
        "🚀 Feature Development Pipeline": [
            "architect-review",
            "backend-architect",
            "frontend-developer",
            "test-automator",
            "security-auditor",
            "deployment-engineer"
        ],
        "🔥 Incident Response": [
            "incident-responder",
            "devops-troubleshooter",
            "error-detective",
            "database-optimizer",
            "observability-engineer"
        ],
        "🤖 AI/ML Development": [
            "ai-engineer",
            "ml-engineer",
            "mlops-engineer",
            "data-scientist",
            "prompt-engineer"
        ],
        "🏗️ Infrastructure Setup": [
            "cloud-architect",
            "terraform-specialist",
            "kubernetes-architect",
            "database-admin",
            "observability-engineer"
        ],
        "🔒 Security Hardening": [
            "security-auditor",
            "backend-security-coder",
            "frontend-security-coder",
            "mobile-security-coder",
            "code-reviewer"
        ],
        "📊 Data Pipeline": [
            "data-engineer",
            "database-optimizer",
            "data-scientist",
            "business-analyst",
            "observability-engineer"
        ],
        "📝 Documentation Sprint": [
            "docs-architect",
            "api-documenter",
            "tutorial-engineer",
            "mermaid-expert",
            "reference-builder"
        ],
        "🎯 SEO Optimization": [
            "seo-content-auditor",
            "seo-keyword-strategist",
            "seo-content-writer",
            "seo-meta-optimizer",
            "seo-structure-architect"
        ]
    }

    for workflow, chain in chains.items():
        print(f"{workflow}")
        for i, agent in enumerate(chain, 1):
            model = agents.get(agent, {}).get('model', '?')
            print(f"  {i}. {agent:<30} ({model})")
        print()

def specialization_index(agents):
    """Calculate specialization vs generalization score"""
    print("\n" + "="*70)
    print("🎯 SPECIALIZATION INDEX (Focused ←→ Versatile)")
    print("="*70 + "\n")

    # Calculate based on name specificity and capability density
    scores = {}
    for name, data in agents.items():
        # More capabilities per section = more specialized
        if data['sections'] > 0:
            density = data['capabilities'] / data['sections']
        else:
            density = 0

        # Longer names often = more specific
        name_specificity = len(name.split('-'))

        # Combined score
        spec_score = (density * 2) + (name_specificity * 10)
        scores[name] = spec_score

    # Top 10 most specialized
    print("Most Specialized (Deep Experts):")
    for i, (name, score) in enumerate(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10], 1):
        model = agents[name]['model']
        print(f"  {i:2}. {name:<35} [{model:>6}] Score: {score:.1f}")

    print("\nMost Versatile (Broad Capability):")
    for i, (name, score) in enumerate(sorted(scores.items(), key=lambda x: x[1])[:10], 1):
        model = agents[name]['model']
        print(f"  {i:2}. {name:<35} [{model:>6}] Score: {score:.1f}")

def learning_curve(agents):
    """Estimate learning curve based on complexity"""
    print("\n" + "="*70)
    print("📚 LEARNING CURVE (Beginner → Expert)")
    print("="*70 + "\n")

    # Complexity = capabilities + (sections * 2) + (opus multiplier)
    complexity = {}
    for name, data in agents.items():
        model_multiplier = 1.5 if data['model'] == 'opus' else 1.2 if data['model'] == 'sonnet' else 1.0
        score = (data['capabilities'] + (data['sections'] * 2)) * model_multiplier
        complexity[name] = score

    # Categorize
    sorted_agents = sorted(complexity.items(), key=lambda x: x[1])
    total = len(sorted_agents)

    beginner = sorted_agents[:total//4]
    intermediate = sorted_agents[total//4:total//2]
    advanced = sorted_agents[total//2:3*total//4]
    expert = sorted_agents[3*total//4:]

    print("🟢 Beginner-Friendly (Low Complexity):")
    for name, score in beginner[:5]:
        print(f"  • {name:<35} ({agents[name]['model']})")

    print("\n🟡 Intermediate Level:")
    for name, score in intermediate[:5]:
        print(f"  • {name:<35} ({agents[name]['model']})")

    print("\n🟠 Advanced Practitioners:")
    for name, score in advanced[:5]:
        print(f"  • {name:<35} ({agents[name]['model']})")

    print("\n🔴 Expert Territory (High Complexity):")
    for name, score in expert[-5:]:
        print(f"  • {name:<35} ({agents[name]['model']}) - Score: {score:.0f}")

def tech_stack_coverage(agents):
    """Identify technology stack coverage"""
    print("\n" + "="*70)
    print("💻 TECHNOLOGY STACK COVERAGE")
    print("="*70 + "\n")

    stacks = {
        'AWS': ['SageMaker', 'Lambda', 'S3', 'CloudFormation', 'ECS', 'CloudWatch'],
        'Azure': ['Azure ML', 'Azure Functions', 'AKS', 'Azure DevOps'],
        'GCP': ['Vertex AI', 'Cloud Functions', 'GKE', 'BigQuery'],
        'Kubernetes': ['Kubernetes', 'K8s', 'kubectl', 'Helm', 'Istio'],
        'React Ecosystem': ['React', 'Next.js', 'Redux', 'React Query'],
        'Python ML': ['PyTorch', 'TensorFlow', 'scikit-learn', 'pandas'],
        'Databases': ['PostgreSQL', 'MongoDB', 'Redis', 'Elasticsearch'],
        'Monitoring': ['Prometheus', 'Grafana', 'DataDog', 'New Relic'],
        'Testing': ['Jest', 'Pytest', 'Playwright', 'Selenium'],
    }

    coverage = {stack: [] for stack in stacks}

    for name, data in agents.items():
        content_lower = data['content'].lower()
        for stack, keywords in stacks.items():
            if any(kw.lower() in content_lower for kw in keywords):
                coverage[stack].append(name)

    for stack, agent_list in sorted(coverage.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{stack:<20} {len(agent_list):3} agents")
        # Show top 3
        for agent in agent_list[:3]:
            print(f"  ↳ {agent}")

def team_roles(agents):
    """Map agents to typical team roles"""
    print("\n" + "="*70)
    print("👥 TEAM ROLE MAPPING")
    print("="*70 + "\n")

    roles = {
        "Senior Architect": ['architect-review', 'cloud-architect', 'backend-architect',
                            'graphql-architect', 'kubernetes-architect', 'hybrid-cloud-architect'],
        "Full-Stack Developer": ['frontend-developer', 'backend-architect', 'database-optimizer',
                                'api-documenter'],
        "DevOps Engineer": ['deployment-engineer', 'devops-troubleshooter', 'terraform-specialist',
                           'kubernetes-architect', 'network-engineer'],
        "Security Specialist": ['security-auditor', 'backend-security-coder',
                               'frontend-security-coder', 'mobile-security-coder'],
        "Data Professional": ['data-scientist', 'data-engineer', 'database-admin',
                             'database-optimizer', 'business-analyst'],
        "QA Engineer": ['test-automator', 'tdd-orchestrator', 'debugger', 'error-detective',
                       'ui-visual-validator'],
        "ML Engineer": ['ai-engineer', 'ml-engineer', 'mlops-engineer', 'prompt-engineer'],
        "SRE": ['incident-responder', 'observability-engineer', 'performance-engineer',
               'network-engineer'],
        "Technical Writer": ['docs-architect', 'api-documenter', 'tutorial-engineer',
                            'mermaid-expert'],
        "Product Manager": ['business-analyst', 'ui-ux-designer', 'customer-support'],
    }

    for role, agent_list in roles.items():
        available = [a for a in agent_list if a in agents]
        if available:
            print(f"🎭 {role}")
            for agent in available:
                model = agents[agent]['model']
                print(f"   • {agent:<30} ({model})")
            print()

def power_combos(agents):
    """Suggest powerful agent combinations"""
    print("\n" + "="*70)
    print("⚡ POWER COMBOS (High-Synergy Pairs)")
    print("="*70 + "\n")

    combos = [
        ("code-reviewer", "security-auditor", "Pre-deployment quality gate"),
        ("ai-engineer", "prompt-engineer", "LLM application development"),
        ("data-scientist", "mlops-engineer", "ML model to production"),
        ("architect-review", "performance-engineer", "Scalable system design"),
        ("frontend-developer", "ui-ux-designer", "User experience excellence"),
        ("database-optimizer", "observability-engineer", "Production database reliability"),
        ("terraform-specialist", "cloud-architect", "Infrastructure automation"),
        ("test-automator", "tdd-orchestrator", "Quality-first development"),
        ("incident-responder", "devops-troubleshooter", "Crisis management"),
        ("docs-architect", "api-documenter", "Comprehensive documentation"),
    ]

    for agent1, agent2, purpose in combos:
        if agent1 in agents and agent2 in agents:
            m1 = agents[agent1]['model']
            m2 = agents[agent2]['model']
            print(f"🔥 {agent1} ({m1}) + {agent2} ({m2})")
            print(f"   → {purpose}\n")

def capability_champions(agents):
    """Find agents with most capabilities in each category"""
    print("\n" + "="*70)
    print("🏆 CAPABILITY CHAMPIONS")
    print("="*70 + "\n")

    # Sort by different metrics
    metrics = {
        'Most Capabilities': lambda a: agents[a]['capabilities'],
        'Most Sections': lambda a: agents[a]['sections'],
        'Longest Documentation': lambda a: agents[a]['lines'],
        'Highest Capability Density': lambda a: agents[a]['capabilities'] / max(agents[a]['sections'], 1),
    }

    for metric_name, metric_fn in metrics.items():
        sorted_agents = sorted(agents.keys(), key=metric_fn, reverse=True)[:5]
        print(f"🥇 {metric_name}:")
        for i, name in enumerate(sorted_agents, 1):
            value = metric_fn(name)
            model = agents[name]['model']
            print(f"  {i}. {name:<30} [{model:>6}] = {value:.1f}")
        print()

def main():
    print("\n" + "="*70)
    print("🎯 CLAUDE CODE AGENTS - CLEVER CATALOG ANALYSIS")
    print("="*70)

    agents = parse_agents()
    print(f"\n📊 Total Agents Analyzed: {len(agents)}")

    # Run all analyses
    capability_champions(agents)
    workflow_chains(agents)
    power_combos(agents)
    team_roles(agents)
    specialization_index(agents)
    learning_curve(agents)
    tech_stack_coverage(agents)

    print("\n" + "="*70)
    print("✨ Analysis Complete!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
