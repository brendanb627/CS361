# Elevator Interfaces
## On-car Computer
```js
function floor_button_press(floor_id: int) -> {go_to_floor(floor_id)}
function update_floor_number(floor_id: int) -> {None (updates display)}
function call_button_press(up: bool) -> {go_to_floor(floor_id)}
```
## Lift Motor Computer
### Outputs
```js
function arrived_at_floor() -> {ring_bell(), open_doors()}
function get_floor_location() -> {floor_id: int}
function get_position() -> {pos: int}
```
### Inputs
```js
function go_to_floor(floor_id: int) -> {update_floor_number(floor_id), arrived_at_floor()}
```
