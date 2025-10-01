# Business & Operations Agents

**7 agents** for business analytics, finance, HR, legal, and customer operations.

## Business Analysis & Finance (3 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [business-analyst](business-analyst.md) | sonnet | Metrics analysis, reporting, KPI tracking |
| [quant-analyst](quant-analyst.md) | opus | Financial modeling, trading strategies, market analysis |
| [risk-manager](risk-manager.md) | opus | Portfolio risk monitoring and management |

## Marketing & Sales (2 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [content-marketer](content-marketer.md) | sonnet | Blog posts, social media, email campaigns |
| [sales-automator](sales-automator.md) | haiku | Cold emails, follow-ups, proposal generation |

## Support & Legal (2 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [customer-support](customer-support.md) | sonnet | Support tickets, FAQ responses, customer communication |
| [hr-pro](hr-pro.md) | opus | HR operations, policies, employee relations |
| [legal-advisor](legal-advisor.md) | opus | Privacy policies, terms of service, legal documentation |

## Workflow Patterns

### Business Intelligence
```
business-analyst → data-scientist → business-analyst (insights)
```

### Financial Analysis
```
quant-analyst → risk-manager → business-analyst (reporting)
```

### Customer Experience
```
customer-support → business-analyst (metrics) → content-marketer (content)
```

### Sales Pipeline
```
sales-automator → customer-support → business-analyst (conversion tracking)
```

### Compliance & Legal
```
legal-advisor → hr-pro → business-analyst (compliance metrics)
```

## Use Cases

**Quarterly business review**: business-analyst
**Investment strategy**: quant-analyst + risk-manager
**Sales automation**: sales-automator
**Customer success**: customer-support + business-analyst
**HR policies**: hr-pro + legal-advisor
**Content strategy**: content-marketer + business-analyst
**Risk assessment**: risk-manager + quant-analyst

## Integration Points

**With Data/AI**: data-scientist, data-engineer for advanced analytics
**With Documentation**: docs-architect for policy documentation
**With SEO**: All SEO agents for content marketing

## Model Distribution Strategy

- **Opus (4)**: Complex decisions (quant, risk, HR, legal)
- **Sonnet (2)**: Operational tasks (analyst, support)
- **Haiku (1)**: Simple automation (sales)

[← Back to Main Catalog](../../README.md)
