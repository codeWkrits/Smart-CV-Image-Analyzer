# Workflow and UML-Style Views

## Workflow
1. User supplies media path and operation.
2. System validates the input.
3. OpenCV loads the media.
4. The selected vision pipeline processes it.
5. Features/statistics are calculated.
6. Annotated media and reports are saved.
7. CLI displays completion status or an error.

## Use Cases
```mermaid
flowchart TB
    U((User)) --> A[Preprocess Image]
    U --> B[Detect Faces]
    U --> C[Detect Shapes]
    U --> D[Analyze Image]
    U --> E[Analyze Video]
    A --> O[(Output Files)]
    B --> O
    C --> O
    D --> O
    E --> O
```

## Sequence Diagram
```mermaid
sequenceDiagram
    actor User
    participant CLI
    participant CV as CV Modules
    participant Output
    User->>CLI: Select command and media
    CLI->>CLI: Validate input
    CLI->>CV: Process media
    CV->>Output: Save results
    Output-->>CLI: Status/path
    CLI-->>User: Completion message
```
