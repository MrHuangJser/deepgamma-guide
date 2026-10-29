"""Adapt canonical Markdown to Starlight without editing research sources."""
from pathlib import Path
import json, re, shutil
ROOT = Path(__file__).resolve().parent.parent
BASE = '/deepgamma-guide/'
DEST = ROOT / 'src/content/docs/generated'
if DEST.exists(): shutil.rmtree(DEST)
files = sorted((ROOT/'guides').glob('*.md')) + [ROOT/'research'/n for n in ['market-foundations.md','web-desktop-differences.md','evidence-and-media.md','coverage-and-unknowns.md']]
files = [p for p in files if p.name != 'web-exclusive.md']
routes = {}
for p in files:
 name = p.stem
 if re.match(r'^(0[1-9]|1[0-4])-',name): group='indicators'
 elif p.parent.name=='guides' and name.startswith('web-') and name!='web-platform': group='web'
 else: group=p.parent.name
 routes[p.resolve()] = f'generated/{group}/{name}'
for p in files:
 lines=p.read_text().splitlines();title=lines[0].lstrip('# ');body='\n'.join(lines[1:])
 def link(m):
  target=m.group(1)
  if target.startswith(('https:', 'http:', '#', 'mailto:')): return m.group(0)
  path,sep,anchor=target.partition('#'); resolved=(p.parent/path).resolve()
  if resolved in routes: url=BASE+routes[resolved]+'/'
  elif resolved==ROOT/'README.md':url=BASE
  elif resolved==ROOT/'guides/web-exclusive.md':url=BASE+'generated/web/web-dynamic-walls/'
  elif resolved==ROOT/'DeepGamma完整手册.md':url=BASE+'downloads/DeepGamma完整手册.md'
  else:
   try:url=BASE+resolved.relative_to(ROOT).as_posix()
   except ValueError:return m.group(0)
  return ']('+url+('#'+anchor if sep else '')+')'
 body=re.sub(r'\]\(([^)\n]+)\)',link,body)
 # A static, accessible reading flow replaces the sole Mermaid source diagram.
 body=re.sub(r'```mermaid\n.*?```', '> **分析路径**\n> 核对数据与坐标 → 整体环境 → 局部集中 → 时间变化 → 新增流量 → 实际价格反应 → 波动空间 → 风险与复盘',body,flags=re.S)
 order=int(p.name[:2]) if p.name[:2].isdigit() else 50
 front='---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\nsidebar:\n  order: '+str(order)+'\n---\n'
 out=ROOT/'src/content/docs'/Path(routes[p.resolve()]+'.md');out.parent.mkdir(parents=True,exist_ok=True);out.write_text(front+'\n'+body+'\n')
public=ROOT/'public';public.mkdir(exist_ok=True)
shutil.copytree(ROOT/'assets',public/'assets',dirs_exist_ok=True)
(public/'downloads').mkdir(exist_ok=True)
shutil.copy2(ROOT/'DeepGamma完整手册.md',public/'downloads/DeepGamma完整手册.md')
(public/'research').mkdir(exist_ok=True)
for p in (ROOT/'research').glob('*.json'):shutil.copy2(p,public/'research'/p.name)
# Keep the original source manifest available as evidence, but outside the search corpus.
print(f'Prepared {len(files)} pages, assets and downloadable handbook.')
