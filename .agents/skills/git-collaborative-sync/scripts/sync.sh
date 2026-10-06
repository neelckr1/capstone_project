#!/usr/bin/env bash
set -euo pipefail

# Determine current branch
BRANCH=$(git branch --show-current || echo "main")
COMMIT_MSG="${1:-Auto-sync: update project files}"

echo "🔄 Checking git status on branch: $BRANCH..."

# Check if there are any uncommitted or untracked changes
CHANGES=$(git status --porcelain)

# 1. Pull latest changes from collaborators using rebase with autostash
echo "⬇️ Pulling latest changes from origin/$BRANCH..."
git pull --rebase --autostash origin "$BRANCH" || {
  echo "⚠️ Warning: Failed to rebase or merge cleanly. Please resolve conflicts."
  exit 1
}

# 2. Check if we have local changes to stage and commit
if [ -n "$CHANGES" ]; then
  echo "📝 Staging changes..."
  git add .
  
  # Check if anything is staged to commit
  if ! git diff --cached --quiet; then
    echo "💾 Committing changes with message: '$COMMIT_MSG'..."
    git commit -m "$COMMIT_MSG"
  else
    echo "ℹ️ No staged differences to commit."
  fi
else
  echo "ℹ️ Working tree is clean, no new local changes to commit."
fi

# 3. Check if local branch is ahead of remote and needs pushing
LOCAL_HASH=$(git rev-parse HEAD)
REMOTE_HASH=$(git rev-parse "origin/$BRANCH" 2>/dev/null || echo "")

if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
  echo "⬆️ Pushing commits to origin/$BRANCH..."
  git push origin "$BRANCH"
  echo "✅ Successfully pushed to origin/$BRANCH!"
else
  echo "✅ Everything is already up to date with origin/$BRANCH."
fi
