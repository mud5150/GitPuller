This is working with a POST from Azure DevOps commit webhook. 
The webhook is configured to POST the full resource when a new commit is pushed.
The `new_commit` method will then pull these changes to sync locally.