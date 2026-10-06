# Workspace Rules for Adaptive Defense for Multi Agent Systems Capstone

## Git Collaborative Synchronization Protocol
This project has multiple collaborators working simultaneously on the same GitHub repository.

- **Automatic Synchronization Rule:** Whenever you make any modifications, create new files, or delete files in this workspace as part of answering a request or finishing a task, you MUST automatically sync the changes with GitHub before ending your response.
- **Pull-Before-Push Requirement:** Never perform a blind push. Always pull remote updates from collaborators using `git pull --rebase --autostash origin <branch>` before staging, committing, and pushing local work.
- **Fast Execution:** You can execute this in one step by running:
  ```bash
  .agents/skills/git-collaborative-sync/scripts/sync.sh "<descriptive commit message>"
  ```
  Or manually:
  ```bash
  BRANCH=$(git branch --show-current)
  git pull --rebase --autostash origin "$BRANCH"
  git add .
  git commit -m "<concise descriptive message>"
  git push origin "$BRANCH"
  ```
