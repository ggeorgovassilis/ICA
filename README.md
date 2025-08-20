# Independent Component Analysis (ICA) Demo

This project demonstrates Independent Component Analysis [ICA](https://en.wikipedia.org/wiki/Independent_component_analysis) using Python and [scikit-learn](https://scikit-learn.org/stable/). It generates synthetic signals, mixes them, and then uses ICA to recover the original sources.

# Why is this interesting?

I always wondered how a radio can tell stations which transmit on the same frequency apart. ICA is an algorithm that can isolate signals from a mix of signals, as long as there are multiple (at least 2) "observers" who receive different mixtures of those signals. Imagine two antennas 

## Features
- Generates two source signals (one is a sum of sinusoids, the other is a square wave)
- Mixes the sources into observed signals
- Applies ICA to separate the mixed signals
- Plots and saves the results, matching colors for true and estimated sources

## Requirements
- Python 3.7+
- See `requirements.txt` for required packages

## Setup
1. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the demo script:
```bash
python ica_demo.py
```
This will generate an `ica_results.png` file with the plots.

## Notes
- The script automatically matches the colors of the true and estimated sources for easier visual comparison.
- The virtual environment directory `venv/` is excluded from version control via `.gitignore`.

## Real sounds

receiver1.wav all three WAVs mixed equally
receiver2.wav cowbells default, horse races 20ms delay -10db, interview 40ms delay -26db
receiver3.wav cowbells -10db 40ms, horse races -20db 20ms, interview default

## Credits and licenses

Brennan, Jennifer, and Donald Brennan. Interview with Donald Brennan, Stafford, Virginia,part 1 of 2. 2001. Audio. https://www.loc.gov/item/afc911000148/.

Cowbells, Horse race audio
bbc.co.uk – © copyright 2025 BBC
https://sound-effects.bbcrewind.co.uk/licensing

Code and documentation MIT license
https://opensource.org/license/mit
