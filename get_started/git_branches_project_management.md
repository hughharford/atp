# AIM: to explain how git branches are used in the project to project manage

### Each branch represents an approach, or line of thinking
Objectives:
- Each git branch is targeted, clear and undertaken reasonably quickly
- Branches are named clearly so that visitors and contributors easily understand
- Branches work in different .ipynb notebooks to avoid conflicts
- Once merged, branches are kept, not deleted, to provide a record/notebook
- Branch understanding or success is brought across to master
- Git branch 'master' still reads as the best, and most current view

### This approach seems to be effective, still early days
Notes:
- Findable notes, provided online or appropriate branch locally for offline
- Use these two to merge branch back in. 
- - git checkout master
- - git merge <branch_name>  
- Aim to work in separate files to prevent conflicts


### Very happy with this approach
Notes:
- Working on more than 1 thing at once is a bit more complex
- Researching data efforts, when that should be on a different branch incurs overhead
- - Requires 'git stash' on one branch, go across, flip back and then 'git stash apply'

