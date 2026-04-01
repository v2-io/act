---
label: D-02
type: Definition
name: Atomic Change-Set
dependencies: []
older-tag: DEF-002
revision: 0.2
---

# D-02 Definition: Atomic Change-Set

The human or AI-generated diff (e.g., excluding build artifacts and intermediate generated code) between the codebase state before and after a feature is fully implemented.

Note that "codebase" here crosses architectural boundaries and includes any changeable part of the system that can and sometimes does change in order to implement features:

- Source code across all services/microservices
- Database schemas and migrations
- Configuration files and feature flags
- Infrastructure-as-code definitions
- Test suites (unit, integration, e2e)
- API documentation and contracts
- Deployment pipelines and CI/CD configurations
- Monitoring and observability configurations
- Runbooks and operational documentation

**Key Principle:** If it must change to deliver the feature and would be reviewed in a pull request, it's part of the atomic change-set.