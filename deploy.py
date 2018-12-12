import os
import time
from git import Remote
from git import Repo
from github import Github

G = Github()
DEPLOY_PATH = '/var/www/html'

repo = G.get_repo("andrearizzello/Auto_Deploy")
if os.path.isdir(DEPLOY_PATH):
	print('Directory detected')
	repo2 = Repo(DEPLOY_PATH)
else:
	print('Directory not detected, cloning...')
	repo2 = Repo.clone_from(repo.git_url, DEPLOY_PATH)

repo3 = Remote(repo2, 'origin')
while 1:
	print('Asking for new data...')
	newData = repo3.pull()
	if newData[0].old_commit is not None and newData[0].commit != newData[0].old_commit:
		print('New commit found, file downloaded!')
	time.sleep(5)
