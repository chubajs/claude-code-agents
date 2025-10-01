# Architecture & System Design Agents

**12 agents** specializing in system architecture, design patterns, and application structure.

## Core Architecture (4 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [backend-architect](backend-architect.md) | opus | RESTful API design, microservice boundaries, database schemas |
| [frontend-developer](frontend-developer.md) | sonnet | React components, responsive layouts, client-side state |
| [graphql-architect](graphql-architect.md) | sonnet | GraphQL schemas, resolvers, federation architecture |
| [architect-review](architect-review.md) | sonnet | Architectural consistency and pattern validation |

## Cloud & Infrastructure (3 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [cloud-architect](cloud-architect.md) | opus | AWS/Azure/GCP infrastructure design, cost optimization |
| [hybrid-cloud-architect](hybrid-cloud-architect.md) | opus | Multi-cloud strategies across cloud and on-premises |
| [kubernetes-architect](kubernetes-architect.md) | opus | Cloud-native infrastructure with Kubernetes and GitOps |

## UI/UX & Mobile (5 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [ui-ux-designer](ui-ux-designer.md) | sonnet | Interface design, wireframes, design systems |
| [ui-visual-validator](ui-visual-validator.md) | sonnet | Visual regression testing and UI verification |
| [mobile-developer](mobile-developer.md) | sonnet | React Native and Flutter application development |
| [ios-developer](ios-developer.md) | sonnet | Native iOS development with Swift/SwiftUI |
| [flutter-expert](flutter-expert.md) | sonnet | Advanced Flutter development with state management |

## Common Workflows

### Full-Stack Feature
```
architect-review → backend-architect → frontend-developer
```

### Cloud Migration
```
cloud-architect → kubernetes-architect → hybrid-cloud-architect
```

### Mobile App
```
ui-ux-designer → ios-developer or mobile-developer or flutter-expert
```

### API Development
```
backend-architect → graphql-architect → api-documenter
```

[← Back to Main Catalog](../../README.md)
