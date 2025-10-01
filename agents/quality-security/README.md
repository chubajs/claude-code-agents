# Quality Assurance & Security Agents

**9 agents** ensuring code quality, security compliance, and comprehensive testing.

## Code Quality & Review (3 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [code-reviewer](code-reviewer.md) | opus | Code review with security focus and production reliability |
| [debugger](debugger.md) | sonnet | Error resolution and test failure analysis |
| [error-detective](error-detective.md) | sonnet | Log analysis and error pattern recognition |

## Security Specialists (4 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [security-auditor](security-auditor.md) | opus | Vulnerability assessment and OWASP compliance |
| [backend-security-coder](backend-security-coder.md) | opus | Secure backend coding, API security implementation |
| [frontend-security-coder](frontend-security-coder.md) | opus | XSS prevention, CSP implementation, client-side security |
| [mobile-security-coder](mobile-security-coder.md) | opus | Mobile security patterns, WebView security, biometric auth |

## Testing & TDD (2 agents)

| Agent | Model | Description |
|-------|-------|-------------|
| [test-automator](test-automator.md) | sonnet | Comprehensive test suite creation (unit, integration, e2e) |
| [tdd-orchestrator](tdd-orchestrator.md) | opus | Test-Driven Development methodology guidance |

## Security Hardening Workflow

```
security-auditor (scan)
    ↓
backend-security-coder + frontend-security-coder + mobile-security-coder (parallel fixes)
    ↓
code-reviewer (final review)
    ↓
test-automator (security tests)
```

## Quality Gate Workflow

```
test-automator (tests first)
    ↓
[development]
    ↓
code-reviewer (quality check)
    ↓
security-auditor (security check)
    ↓
[deploy]
```

## TDD Development Cycle

```
tdd-orchestrator (coordinate)
    ↓
test-automator (write failing tests)
    ↓
[implement feature]
    ↓
debugger (fix issues)
    ↓
code-reviewer (refactor)
```

## Power Combos

**Pre-deployment Gate**: code-reviewer + security-auditor
**Security Fortress**: All 4 security agents in sequence
**Quality First**: tdd-orchestrator + test-automator
**Debug & Fix**: error-detective + debugger

## Key Stats

- **4 Opus security agents** - All critical security tasks
- **test-automator** - 203 lines, 143 capabilities
- **Security coverage** - Backend, frontend, mobile
- **TDD support** - Complete red-green-refactor cycle

[← Back to Main Catalog](../../README.md)
