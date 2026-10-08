import sys, json, subprocess, re, os

data = json.load(sys.stdin)
cmd = data.get('tool_input', {}).get('command', '')

if not (re.search(r'git push.*(?:master|main)', cmd) or cmd.strip() == 'git push'):
    sys.exit(0)

today = subprocess.check_output(['date', '+%d/%m/%Y']).decode().strip()
repo = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip()

try:
    raw = subprocess.check_output(
        ['git', '-C', repo, 'diff', '--name-only', 'origin/master..HEAD'],
        stderr=subprocess.DEVNULL
    ).decode().strip()
    changed_set = set(raw.splitlines()) if raw else set()
except subprocess.CalledProcessError:
    changed_set = set()

def update_date_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(r'\*\*Date:\*\* \d{2}/\d{2}/\d{4}', f'**Date:** {today}', content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

files_to_stage = []

readme = os.path.join(repo, 'README.md')
if update_date_in_file(readme):
    files_to_stage.append('README.md')

for rel in ['ethics/ethics.md', 'basics/basics.md', 'tactics/tactics.md']:
    if rel in changed_set:
        abs_path = os.path.join(repo, *rel.split('/'))
        if os.path.exists(abs_path) and update_date_in_file(abs_path):
            files_to_stage.append(rel)

if files_to_stage:
    subprocess.run(['git', '-C', repo, 'add'] + files_to_stage)
    names = ', '.join(os.path.basename(f) for f in files_to_stage)
    subprocess.run(['git', '-C', repo, 'commit', '-m', f'Update date to {today} in {names}'])
