import sys, json, subprocess, re, os

data = json.load(sys.stdin)
cmd = data.get('tool_input', {}).get('command', '')

if not (re.search(r'git push.*(?:master|main)', cmd) or cmd.strip() == 'git push'):
    sys.exit(0)

today = subprocess.check_output(['date', '+%d/%m/%Y']).decode().strip()
repo = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip()
readme = os.path.join(repo, 'README.md')

with open(readme, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'\*\*Date:\*\* \d{2}/\d{2}/\d{4}', f'**Date:** {today}', content)

if new_content != content:
    with open(readme, 'w', encoding='utf-8') as f:
        f.write(new_content)
    subprocess.run(['git', '-C', repo, 'add', 'README.md'])
    subprocess.run(['git', '-C', repo, 'commit', '-m', f'Update README date to {today}'])
