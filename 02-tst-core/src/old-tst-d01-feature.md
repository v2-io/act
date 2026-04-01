---
label: D-01
type: Definition
name: Feature
dependencies: []
older-tag: DEF-001
revision: 0.3
---
    
# D-01 Definition: Feature

A unit of functionality, as perceived by those who requested, implement, or use it, that coherently changes the codebase and/or running system, including fixes through to full intended functionality.

## Discussion

- Includes changes to non-functional requirements (performance, security, accessibility)
- Includes infrastructure changes that affect system capabilities
- Includes documentation changes that affect stakeholder understanding
- May include configuration changes and coordinated changes across multiple codebases or coupled systems
- Excludes pure no-op changes but includes changes that alter future implementation time while preserving external behavior
- Note that what are often called "no-op changes" are typically attempts at refactoring that fall under this definition