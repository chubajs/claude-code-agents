# Infrastructure & Operations Agents

**10 agents** specializing in DevOps, deployment, databases, and SRE practices.

## DevOps & Deployment (4 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [devops-troubleshooter](devops-troubleshooter.md) | sonnet | Production debugging, log analysis, deployment troubleshooting |
| [deployment-engineer](deployment-engineer.md) | sonnet | CI/CD pipelines, containerization, cloud deployments |
| [terraform-specialist](terraform-specialist.md) | opus | Infrastructure as Code with Terraform modules and state management |
| [dx-optimizer](dx-optimizer.md) | sonnet | Developer experience optimization and tooling improvements |

## Database Management (2 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [database-optimizer](database-optimizer.md) | opus | Query optimization, index design, migration strategies |
| [database-admin](database-admin.md) | sonnet | Database operations, backup, replication, monitoring |

## Incident Response & SRE (4 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [incident-responder](incident-responder.md) ⚡ | opus | **CRITICAL** - Production incident management and resolution |
| [network-engineer](network-engineer.md) | sonnet | Network debugging, load balancing, traffic analysis |
| [observability-engineer](observability-engineer.md) | opus | Production monitoring, distributed tracing, SLI/SLO management |
| [performance-engineer](performance-engineer.md) | opus | Application profiling and optimization |

## Critical Response Workflows

### Production Incident
```
incident-responder ⚡ → devops-troubleshooter → observability-engineer
```

### Infrastructure Setup
```
terraform-specialist → deployment-engineer → observability-engineer
```

### Database Performance
```
database-optimizer → observability-engineer → performance-engineer
```

### Network Issues
```
network-engineer → devops-troubleshooter → incident-responder
```

## Key Features

🔥 **incident-responder** - Only agent with IMMEDIATE activation
📊 **observability-engineer** - Most comprehensive (156 capabilities)
⚡ **performance-engineer** - Critical path for production optimization
🗄️ **database-optimizer** - Essential for scale

[← Back to Main Catalog](../../README.md)
