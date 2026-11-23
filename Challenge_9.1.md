## Classes

- **CommandTests**
  - Is a test case
- **WorldValidationTests**
  - Is a test case
- **ParserTests**
  - Is a test case
- **WalkthroughTests**
  - Is a test case
- **VerbSpec**
- **Game**
  - Has a World
  - Has an Output
  - Has a GameState
  - Has an Item
- **Exit**
  - Has a Condition
- **Extra**
  - Has a Condition
- **Room**
  - Has Exits
  - Has Extras
- **Item**
  - Has Extras
- **Trigger**
  - Has an Effect
  - Has a Condition
- **Event**
  - Has a Condition
  - Has an Effect
- **World**
  - Has Triggers
  - Has Rooms
  - Has Items
  - Has Events
  - Has GameState
- **GameState**
- **Output**
- **Command**
  - Has an Item
- **SaveError**
  - Is an Exception
- **BufferOutput**
  - Is an Output

## Imports

- **Main**
  - From `engine` import `Game`
  - From `WorldLoader` import `WorldError`

- **helpers.py**
  - From `pathlib` import `Path`
  - From `engine` import `Game`
  - From `output` import `BufferOutput`
  - From `WorldLoader` import `build_world`, `load_world`

- **testcommands.py**
  - From `pathlib` import `Path`
  - Import `INVENTORY`
  - Import `WorldError`, `build_world`
  - Import `TINY_WORLD`, `run`, `tiny_game`

- **commands.py**
  - Import `Game`
  - Import `Item`
  - Import `SaveError`, `load_game`, `save_game`

- **conditions.py**
  - From `model` import `INVENTORY`, `Condition`, `Effect`, `room_loc`
  - From `engine` import `Game`

- **engine.py**
  - From `pathlib` import `Path`
  - From `.` import `commands`
  - From `conditions` import `apply_all`, `check_all`
  - From `model` import `INVENTORY`, `Extra`, `GameState`, `Item`, `World`, `in_loc`, `room`
  - From `parser` import `Output`, `join_list`

- **model.py**
  - From `dataclasses` import `asdict`, `dataclasses`, `field`, `fields`

- **output.py**

- **parser.py**
  - From `typing` import `TYPE_CHECKING`
  - From `model` import `Item`

- **save.py**
  - From `pathlib` import `Path`
  - From `model` import `GameState`, `World`

- **World_loader.py**
  - Import `conditions`
  - Import `model`

  ## Data
  - **world.json**
   - used in `AGENTS.md`
   - used in `main.py`
   - used in `helpers.py`
   - used in `world_loader.py`