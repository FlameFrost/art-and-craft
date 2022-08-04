## Working with continuous stream of data

- `input.py` generates stream of data into `STDOUT` (continuous flush-ing)
- `output.py` reads continuous stream of data from `STDIN` and regurgitates to `STDOUT`

#### Run me
```bash
./input.py | ./output.py
```
