---
name: git-collaborative-sync
description: >-
  Use this skill whenever files in the workspace are added, updated, or removed,
  or when the user requests syncing or pushing changes to Git. Ensures safe collaborative
  synchronization by pulling the latest remote commits first (with rebase and autostash),
  committing local modifications, and pushing to the remote repository.
---

# Git Collaborative Sync Skill

This skill ensures that all changes made in the workspace are safely and automatically synchronized with the remote Git repository (`origin`), avoiding merge conflicts with team collaborators.

## Workflow Overview

Because this repository has multiple collaborators, you must **never blind-push**. Always pull latest updates with rebase before pushing.

```
Local Changes Detected
         │
         ▼
git pull --rebase --autostash origin <branch>
         │
         ▼
git add .
         │
         ▼
git commit -m "<concise descriptive message>"
         │
         ▼
git push origin <branch>
```

---

## Instructions

Whenever you modify, create, or delete any files in the workspace, execute the collaborative sync routine:

### Option 1: Execute the Helper Script (Recommended)

Run the included sync script directly:

```bash
.agents/skills/git-collaborative-sync/scripts/sync.sh "<descriptive commit message>"
```

### Option 2: Execute Git Commands Manually

If running manually via shell:

1. **Identify the current active branch:**
   ```bash
   BRANCH=$(git branch --show-current)
   ```

2. **Pull upstream commits from collaborators first (with autostash):**
   ```bash
   git pull --rebase --autostash origin "$BRANCH"
   ```

3. **Stage and commit your changes:**
   ```bash
   git add .
   git commit -m "<concise message describing what was changed>"
   ```

4. **Push commits to the remote repository:**
   ```bash
   git push origin "$BRANCH"
   ```

5. **Verify synchronization status:**
   ```bash
   git status
   ```

---

## Conflict Handling

If `git pull --rebase` reports a conflict:
1. Inspect the conflicting files using `git status` and view the conflict markers.
2. Carefully resolve the conflict while preserving both collaborator intent and recent local work.
3. Stage the resolved files with `git add <file>` and run `git rebase --continue`.
4. Push once the rebase completes cleanly.
