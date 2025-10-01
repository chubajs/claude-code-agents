#!/bin/bash
# Organize Claude Code Agents into folders

echo "📦 Organizing agents into folders..."

# Architecture & System Design
mkdir -p agents/architecture
mv backend-architect.md agents/architecture/ 2>/dev/null
mv frontend-developer.md agents/architecture/ 2>/dev/null
mv graphql-architect.md agents/architecture/ 2>/dev/null
mv architect-review.md agents/architecture/ 2>/dev/null
mv cloud-architect.md agents/architecture/ 2>/dev/null
mv hybrid-cloud-architect.md agents/architecture/ 2>/dev/null
mv kubernetes-architect.md agents/architecture/ 2>/dev/null
mv ui-ux-designer.md agents/architecture/ 2>/dev/null
mv ui-visual-validator.md agents/architecture/ 2>/dev/null
mv mobile-developer.md agents/architecture/ 2>/dev/null
mv ios-developer.md agents/architecture/ 2>/dev/null
mv flutter-expert.md agents/architecture/ 2>/dev/null

# Programming Languages
mkdir -p agents/languages
mv c-pro.md agents/languages/ 2>/dev/null
mv cpp-pro.md agents/languages/ 2>/dev/null
mv rust-pro.md agents/languages/ 2>/dev/null
mv golang-pro.md agents/languages/ 2>/dev/null
mv javascript-pro.md agents/languages/ 2>/dev/null
mv typescript-pro.md agents/languages/ 2>/dev/null
mv python-pro.md agents/languages/ 2>/dev/null
mv ruby-pro.md agents/languages/ 2>/dev/null
mv php-pro.md agents/languages/ 2>/dev/null
mv java-pro.md agents/languages/ 2>/dev/null
mv scala-pro.md agents/languages/ 2>/dev/null
mv csharp-pro.md agents/languages/ 2>/dev/null
mv elixir-pro.md agents/languages/ 2>/dev/null
mv sql-pro.md agents/languages/ 2>/dev/null
mv django-pro.md agents/languages/ 2>/dev/null
mv fastapi-pro.md agents/languages/ 2>/dev/null

# Infrastructure & Operations
mkdir -p agents/infrastructure
mv devops-troubleshooter.md agents/infrastructure/ 2>/dev/null
mv deployment-engineer.md agents/infrastructure/ 2>/dev/null
mv terraform-specialist.md agents/infrastructure/ 2>/dev/null
mv dx-optimizer.md agents/infrastructure/ 2>/dev/null
mv database-optimizer.md agents/infrastructure/ 2>/dev/null
mv database-admin.md agents/infrastructure/ 2>/dev/null
mv incident-responder.md agents/infrastructure/ 2>/dev/null
mv network-engineer.md agents/infrastructure/ 2>/dev/null
mv observability-engineer.md agents/infrastructure/ 2>/dev/null
mv performance-engineer.md agents/infrastructure/ 2>/dev/null

# Quality Assurance & Security
mkdir -p agents/quality-security
mv code-reviewer.md agents/quality-security/ 2>/dev/null
mv security-auditor.md agents/quality-security/ 2>/dev/null
mv backend-security-coder.md agents/quality-security/ 2>/dev/null
mv frontend-security-coder.md agents/quality-security/ 2>/dev/null
mv mobile-security-coder.md agents/quality-security/ 2>/dev/null
mv test-automator.md agents/quality-security/ 2>/dev/null
mv tdd-orchestrator.md agents/quality-security/ 2>/dev/null
mv debugger.md agents/quality-security/ 2>/dev/null
mv error-detective.md agents/quality-security/ 2>/dev/null

# Data & AI
mkdir -p agents/data-ai
mv data-scientist.md agents/data-ai/ 2>/dev/null
mv data-engineer.md agents/data-ai/ 2>/dev/null
mv ai-engineer.md agents/data-ai/ 2>/dev/null
mv ml-engineer.md agents/data-ai/ 2>/dev/null
mv mlops-engineer.md agents/data-ai/ 2>/dev/null
mv prompt-engineer.md agents/data-ai/ 2>/dev/null

# Documentation & Content
mkdir -p agents/documentation
mv docs-architect.md agents/documentation/ 2>/dev/null
mv api-documenter.md agents/documentation/ 2>/dev/null
mv reference-builder.md agents/documentation/ 2>/dev/null
mv tutorial-engineer.md agents/documentation/ 2>/dev/null
mv mermaid-expert.md agents/documentation/ 2>/dev/null
mv content-marketer.md agents/documentation/ 2>/dev/null

# Business & Operations
mkdir -p agents/business
mv business-analyst.md agents/business/ 2>/dev/null
mv quant-analyst.md agents/business/ 2>/dev/null
mv risk-manager.md agents/business/ 2>/dev/null
mv sales-automator.md agents/business/ 2>/dev/null
mv customer-support.md agents/business/ 2>/dev/null
mv hr-pro.md agents/business/ 2>/dev/null
mv legal-advisor.md agents/business/ 2>/dev/null

# SEO & Content Optimization
mkdir -p agents/seo
mv seo-content-auditor.md agents/seo/ 2>/dev/null
mv seo-meta-optimizer.md agents/seo/ 2>/dev/null
mv seo-keyword-strategist.md agents/seo/ 2>/dev/null
mv seo-structure-architect.md agents/seo/ 2>/dev/null
mv seo-snippet-hunter.md agents/seo/ 2>/dev/null
mv seo-content-refresher.md agents/seo/ 2>/dev/null
mv seo-cannibalization-detector.md agents/seo/ 2>/dev/null
mv seo-authority-builder.md agents/seo/ 2>/dev/null
mv seo-content-writer.md agents/seo/ 2>/dev/null
mv seo-content-planner.md agents/seo/ 2>/dev/null

# Specialized Domains
mkdir -p agents/specialized
mv blockchain-developer.md agents/specialized/ 2>/dev/null
mv payment-integration.md agents/specialized/ 2>/dev/null
mv legacy-modernizer.md agents/specialized/ 2>/dev/null
mv context-manager.md agents/specialized/ 2>/dev/null
mv unity-developer.md agents/specialized/ 2>/dev/null
mv minecraft-bukkit-pro.md agents/specialized/ 2>/dev/null
mv search-specialist.md agents/specialized/ 2>/dev/null

echo "✅ Agents organized into folders!"
echo ""
echo "📊 Folder structure:"
echo "  agents/"
echo "    ├── architecture/       (12 agents)"
echo "    ├── languages/          (16 agents)"
echo "    ├── infrastructure/     (10 agents)"
echo "    ├── quality-security/   (9 agents)"
echo "    ├── data-ai/            (6 agents)"
echo "    ├── documentation/      (6 agents)"
echo "    ├── business/           (7 agents)"
echo "    ├── seo/                (10 agents)"
echo "    └── specialized/        (7 agents)"
echo ""
echo "Total: 83 agents organized"
