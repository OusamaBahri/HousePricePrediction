Get started with Git
============
### What is Git ?
Git is a version control system designed to track changes in a source code over time.

___

_A list of the basic Git commands_


--

### Getting & Creating Projects

| Command | Description |
| ------- | ----------- |
| `git init` | Initialize a local Git repository |
| `git clone ssh://git@github.com/[username]/[repository-name].git` | Create a local copy of a remote repository |

### Snapshotting and Pulling

| Command                            | Description                                       |
|------------------------------------|---------------------------------------------------|
| `git status`                       | Show which files you have changed                 |
| `git add [file-name.txt]`          | Choose file(s) to be tracked (staging)            |
| `git commit -m "[commit message]"` | Commit (save) changes                             |
| `git pull"`                        | Pull recent commits made by others into your local computer.                            |

### Branching & Merging

| Command | Description |
| ------- | ----------- |
| `git branch` | List branches  |
| `git branch -a` | List all branches (local and remote) |
| `git branch [branch name]` | Create a new branch |
| `git branch -d [branch name]` | Delete a branch |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git checkout -b [branch name]` | Create a new branch and switch to it |
| `git checkout -b [branch name] origin/[branch name]` | Clone a remote branch and switch to it |
| `git branch -m [old branch name] [new branch name]` | Rename a local branch |
| `git checkout [branch name]` | Switch to a branch |
| `git checkout -` | Switch to the branch last checked out |
| `git checkout -- [file-name.txt]` | Discard changes to a file |
| `git merge [branch name]` | Merge a branch into the active branch |
| `git merge [source branch] [target branch]` | Merge a branch into a target branch |
