# py-Tark-Hideout-Bot

Automated Hideout Interactions for Escape From Tarkov

Join the [Discord server](https://discord.gg/Cf8fXtayXA)!

## What is Py-Tark-Hideout-Bot?

The bot's purpose is to automatically start and collect hideout crafts. The bot works by cycling your hideout, initiating or collecting crafts in your selected stations.

This bot's purpose is to make you money while you're afk!

<img src="https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/blob/main/assets/hideout_bot_demo.gif?raw=true" width="70%"/><img src="https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/blob/main/assets/hideout_bot_demo_gui.png?raw=true" width="30%"/>

## Install

Download the latest Windows Installer [here](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/releases/latest).

## Bug report

Report bugs in the [Github issues tab](https://github.com/matthewmiglio/Py-Tark-Hideout-Bot/issues). Be descriptive as possible, including screenshots, error messages, and steps to reproduce.

## Contributing and Running from Source

All contributions are welcome, open a pull request to contribute.

For developers, to install the source code with the following:

```bash
git clone https://github.com/matthewmiglio/Py-Tark-Hideout-Bot.git
cd Py-Tark-Hideout-Bot
python -m pip install poetry # install poetry for dependency management if you don't have it
poetry install --with dev # --with build # install dependencies
poetry run pre-commit install # optional, but highly recommended for contributing
poetry run python hideoutbot/__main__.py # run the program from source
```
