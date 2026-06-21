# Installation guide

This project is intended to run locally with Python.

## Requirements

- Python 3.10 or newer
- Internet access for the content feed and platform APIs
- A local `.env` file with the credentials you want to use

## Install dependencies

From the repository folder:

```bash
python -m pip install -r requirements.txt
```

If your system uses `python3` instead of `python`, run:

```bash
python3 -m pip install -r requirements.txt
```

## First check

Before publishing anything, run:

```bash
python app.py status
```

Then run a preview:

```bash
python app.py preview --limit 3
```

Only publish after the status and preview look correct.
