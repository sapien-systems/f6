# Contributing to f6

Thank you for helping. Every kind of contribution is welcome, including questions.

## Ways to contribute

1. **Add or challenge a word** in the lexicon (the easiest start).
2. **Answer an open question** listed at the bottom of each document in `docs/`.
3. **Improve the Delphi Dice prototype** in `prototype/`.
4. **Translate or clarify** the docs. English is the working language, Swedish and other languages are welcome alongside it.
5. **Report problems** by opening an issue.

## Adding a word

1. Open `lexicon/lexicon.json` and add an entry:

   ```json
   {"word": "family dinner", "lang": "en", "lambda": 0.15, "delta": 0.20, "alpha": 0.65,
    "mass": 0.3, "runlevel": 3, "notes": "Why you placed it here."}
   ```

2. Rules:
   - `lambda + delta + alpha` must equal 1 (Λ solo, Δ chaos, Α order).
   - `mass` is zero or more. For now, use the relative 0 to 1 scale.
   - `runlevel` is optional, an integer from 0 to 6.
   - One entry per word per language. If a word already exists and you disagree with its position, **do not overwrite it**: open an issue using the *Word proposal* template and show your coordinates. Disagreements are useful data.
   - Put your reasoning in `notes`.

3. Run `python3 tools/validate_lexicon.py` to check your entry.
4. Open a pull request.

## Changing the specs

Open an issue first, describing what is unclear or inconsistent and what you propose. Small fixes (typos, clearer wording) can go straight to a pull request.

## Code

- Python 3.9 or newer, standard library only, so the project stays easy to read and port.
- Add a test in `tests/` for new behaviour. Run `python3 -m unittest discover -s tests`.
- The prototype is a single self-contained HTML file. Keep it that way.

## Privacy

Privacy comes first in this project. Contributing under a pseudonym is fine. Use a pseudonymous git identity, strip metadata from images, and keep personal details out of issues and pull requests. See [docs/team.md](docs/team.md#privacy-for-contributors).

## License

By contributing, you agree that your contribution is released under the project license, the [Physix Perpetualicense and Ideological Money Pump](LICENSE), including its IMP (Ideological Money Pump) clause: at least 10% of profits derived from SophiOS must be given to those less fortunate. See [docs/imp.md](docs/imp.md).

## Principles

- **No words in the interface.** Anything user-facing in SophiOS must work without text.
- **Make judgments visible.** Prefer explicit numbers and stated reasons over hidden assumptions.
- **Be kind.** See the [Code of Conduct](CODE_OF_CONDUCT.md).
