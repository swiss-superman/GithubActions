## Types of custom actions:
```text
    composite actions
    js/ts actions
    container actions
    resuable workflows
```

custom-actions/action.yml
```yml
name: Action name
description: Action description

input:
    varname:
        description:
        required:
        default:
output:
    var-name:
        description:
        value: ${{ steps.step-id.outputs.varname }}
runs:
    using: '(composite)'
    steps:
        - name: Step name
          id: step-di
          run: |
            echo "varname=foo" >> "$GITHUB_OUTPUT"
```

Always checkout before using custom actions
