# Git and GitHub Practical Demo

This demo follows the beginner-friendly question-and-answer notebook. Replace `USERNAME` and `REPOSITORY` with your own GitHub details.

## 1. Check Git and configure your identity

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global --list
```

## 2. Create a local repository

```bash
mkdir git-demo
cd git-demo
git init
git branch -M main
```

Create a file named `README.md` and add a line such as `# My Git Demo`.

## 3. Stage and commit files

```bash
git status
git add .
git status
git commit -m "Initial commit"
git log --oneline
```

`git add .` stages changes; `git commit` saves the staged snapshot in local history.

## 4. Connect to a GitHub repository

First, create an empty repository on GitHub. Then run:

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git remote -v
git push -u origin main
```

The `origin` name refers to the remote URL. The first push with `-u` sets upstream tracking for `main`.

If the remote already contains commits (for example, a README created on GitHub), you may need to pull and reconcile that history before pushing.

## 5. Make another change and push it

Edit `README.md`, then run:

```bash
git status
git add .
git commit -m "Update README"
git push
```

Because upstream tracking was set with `-u`, `git push` can usually infer `origin main`.

## 6. Clone and pull

To get a separate local copy:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

To update an existing local copy later:

```bash
git pull
```

## Quick revision

| Command | Purpose |
|---|---|
| `git --version` | Check installed Git version |
| `git init` | Start a Git repository in the current folder |
| `git status` | Show changed/staged files and branch state |
| `git add .` | Stage changes under the current directory |
| `git commit -m "message"` | Save staged changes in local history |
| `git branch` | List local branches |
| `git branch -M main` | Rename current branch to `main` |
| `git remote add origin URL` | Add a remote nickname and URL |
| `git push -u origin main` | Push and set upstream tracking |
| `git clone URL` | Create a local copy of a remote repository |
| `git pull` | Fetch and integrate remote changes |

**Important:** Git commands above are examples. Do not type placeholder values like `USERNAME` literally; replace them with your GitHub username and repository name.
