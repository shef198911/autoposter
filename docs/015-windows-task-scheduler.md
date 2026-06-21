# Windows Task Scheduler notes

Windows Task Scheduler can run the autoposter on a schedule after manual testing is complete.

## Recommended command

Use the project folder as the working directory and run:

```bat
python app.py send --all --dry
```

Switch from `--dry` to real sending only after several successful checks.

## Checklist

- Python is available in PATH.
- Dependencies are installed.
- `.env` exists in the project folder.
- The task runs from the repository directory.
- Logs are saved somewhere easy to review.

Start with a conservative schedule, such as once per day.
