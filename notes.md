# Troubleshooting Notes

| Symptom | Cause | Command that found it | Fix |
|---|---|---|---|
| Service failed, status=203/EXEC | Project built under another user, venv missing | systemctl status, ls -l on the path | Copied project, chown, rebuilt venv |
| Permission denied (publickey) | New SSH key not added to GitHub | ssh -vT git@github.com | Added key in GitHub settings |
| Temporary failure in name resolution | Brief DNS glitch in WSL | ping 8.8.8.8 vs ping github.com | Recovered by itself |
| not a git repository | Folder copied without .git | git status | git init, add remote, push |
