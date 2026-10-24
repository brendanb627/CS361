## Challenge 4.5: Component Diagram

```mermaid
flowchart LR
    Client
    Server
    StatsDB[Stats Database]
    Room/Lobby

    Client-->|connects to|Server
    Server-->|API Calls|StatsDB
    Server-->|creates|Room/Lobby
    Server-->|creates instance|GameEngine[Game Engine]
    Room/Lobby-->|players join instance|GameEngine
```
