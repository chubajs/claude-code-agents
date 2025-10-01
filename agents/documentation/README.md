# Documentation & Content Agents

**6 agents** for technical writing, API documentation, and content marketing.

## Technical Documentation (4 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [docs-architect](docs-architect.md) | opus | Comprehensive technical documentation generation |
| [api-documenter](api-documenter.md) | sonnet | OpenAPI/Swagger specifications and developer docs |
| [reference-builder](reference-builder.md) | haiku | Technical references and API documentation |
| [tutorial-engineer](tutorial-engineer.md) | opus | Step-by-step tutorials and educational content |

## Visualization & Content (2 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [mermaid-expert](mermaid-expert.md) | sonnet | Diagram creation (flowcharts, sequences, ERDs) |
| [content-marketer](content-marketer.md) | sonnet | Blog posts, social media, email campaigns |

## Documentation Sprint Workflow

```
1. docs-architect (plan documentation structure)
2. api-documenter (generate API docs)
3. tutorial-engineer (create tutorials)
4. mermaid-expert (add diagrams)
5. reference-builder (build reference docs)
```

## By Documentation Type

### API Documentation
```
api-documenter → reference-builder → mermaid-expert (diagrams)
```

### User Guides
```
docs-architect → tutorial-engineer → mermaid-expert
```

### Marketing Content
```
content-marketer → tutorial-engineer (customer education)
```

### Technical Specs
```
docs-architect → mermaid-expert (architecture diagrams) → reference-builder
```

## Use Cases

**New API launch**: api-documenter + reference-builder
**Product documentation**: docs-architect + tutorial-engineer
**Architecture docs**: docs-architect + mermaid-expert
**Developer portal**: api-documenter + tutorial-engineer + reference-builder
**Marketing campaign**: content-marketer
**Onboarding guides**: tutorial-engineer + mermaid-expert

## Model Distribution

- **Opus (2)**: docs-architect, tutorial-engineer - Complex narrative
- **Sonnet (3)**: api-documenter, mermaid-expert, content-marketer - Technical details
- **Haiku (1)**: reference-builder - Quick reference lookup

## Power Combinations

**Complete API Docs**: api-documenter + reference-builder + mermaid-expert
**User Documentation**: docs-architect + tutorial-engineer + mermaid-expert
**Developer Onboarding**: tutorial-engineer + api-documenter
**Marketing + Education**: content-marketer + tutorial-engineer

[← Back to Main Catalog](../../README.md)
