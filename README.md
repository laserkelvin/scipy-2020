
# SciPy-2020 Talk

These are my slides for SciPy 2020; the first I attended!

The slides are built with `reveal.js`, and are served as static HTML on the Github
pages [https://laserkelvin.github.io/scipy-2020](of this repo).

## Instructions

1. Make sure you have Node Package Manager (`npm`) installed.
2. Run `make setup` to install the latest version of `reveal-md`
3. Run `make present` to serve the presentation locally
4. Run `make pdf` to dump to `slides.pdf`

## Notes on serving

- Put figures and whatnot into the `figures` folder, which will be copied when a static version of the deck is created.
- Most of the control is done through the `Makefile`; variables should be self-explanatory.
