# py-Tark-Hideout-Bot

Automated Hideout Interactions for Escape From Tarkov

Join the [Discord server](https://discord.gg/Cf8fXtayXA)!

## What is Py-Tark-Hideout-Bot?
The bot's purpose is to automatically start and collect hideout crafts. The bot works by cycling your hideout, initiating or collecting crafts in your selected stations.

This bot's purpose is to make you money while you're afk!

![hideout bot photo](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/assets/105177840/98ae05cc-90b7-41a3-8b2b-f408e16083ca)

[![hideout bot video](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/assets/105177840/fd9412b6-d64d-439c-b64e-4f2f2577a04a)](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/assets/105177840/fd9412b6-d64d-439c-b64e-4f2f2577a04a)

## Install

Releases for the Py-Tark-Hideout-Bot are available [here](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/releases)

## Bug report

Report bugs in the [Github issues tab](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/issues). Be descriptive as possible, including screenshots, error messages, and steps to reproduce.

## Contributing and Running from Source

All contributions are welcome, open a pull request to contribute.

For developers, to install the source code with the following:

!!!THIS PROJECT IS MISSING AN ENVIRONMENT AT THE MOMENT!!!

```bash
git clone https://github.com/matthewmiglio/Py-Tark-Hideout-Bot.git
cd Py-Tark-Hideout-Bot
python -m pip install poetry # install poetry for dependency management if you don't have it
poetry install --with dev # --with build # install dependencies
poetry run pre-commit install # optional, but highly recommended for contributing
poetry run python src/__main__.py # run the program from source
