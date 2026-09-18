[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/penguin-crate/iso2chd-gui/releases)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Arch Linux](https://img.shields.io/badge/Arch%20Linux-Native-1793d1.svg?logo=arch-linux)](https://archlinux.org)

A sleek, user-friendly graphical companion for `iso2chd`, optimized for Arch Linux and retro-gaming setups. Designed and engineered by **Abhimanyu Bhadauriya**.

`iso2chd-gui` provides an intuitive point-and-click interface to batch-convert optical media backups (`.iso`, `.bin`, `.cue`) into high-efficiency Compressed Hunks of Data (`.chd`) without touching the terminal.

---

## Key Features

* **Visual Directory Selector**: Easily browse and select your games folder with a native graphical prompt.
* **Seamless Ecosystem**: The Arch Linux package automatically resolves and builds the backend `iso2chd` CLI tool from source.
* **Desktop Integration**: Instantly appears in your system app launcher with a custom icon.
* **Standalone Binary**: Compiled with PyInstaller so all frontend dependencies are cleanly self-contained.

---

## Installation (Arch Linux)

Ensure you have `git` and `base-devel` installed, then clone and build the package natively. It will automatically fetch and compile the CLI backend alongside the GUI:

```bash
git clone https://github.com/penguin-crate/iso2chd-gui.git
cd iso2chd-gui
makepkg -sic
