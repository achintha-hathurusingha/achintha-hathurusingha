import os
from github import Github, Auth
from datetime import datetime, timedelta
import pytz

# ==========================================
# CONFIGURATION
# ==========================================
USERNAME = "achintha-hathurusingha"

# GIF CONFIGURATION (served from this profile repo)
GIF_URL = f"https://raw.githubusercontent.com/{USERNAME}/{USERNAME}/main/gif3%20(1).gif"

REPOS = {
    "rhel-automation-scripts": {"goal": 4, "label": "RHEL Scripts"},
    "infrastructure-playground": {"goal": 3, "label": "Infra Playground"},
    "k8s-lab-experiments": {"goal": 5, "label": "K8s Labs"},
    "engineering-journal": {"goal": 7, "label": "Eng Journal"},
}

# ==========================================
# 1. HEADER SECTION
# ==========================================
HEADER_TOP = f"""<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,5,30&height=280&section=header&text=Achintha%20Rukshan&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=DevOps%20%7C%20Cloud%20%7C%20Infrastructure%20Engineer&descAlignY=54&descSize=20"/>
</div>

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=2E64FE&center=true&vCenter=true&width=520&lines=Building+Resilient+Infrastructure;Automating+The+Boring+Stuff;Exploring+RHEL%2C+VMware+%26+Kubernetes;Trainee+Infra+Engineer+%40+MillenniumIT+ESP" alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username={USERNAME}&label=Profile%20Views&color=2E64FE&style=for-the-badge" alt="profile views" />
</div>

<br/>

<div align="center">
  <a href="https://www.linkedin.com/in/achintha-rukshan-583671344/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="mailto:achinthar456@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="mailto:hathurusinghahar.22@uom.lk">
    <img src="https://img.shields.io/badge/UoM_Email-005a9c?style=for-the-badge&logo=minutemailer&logoColor=white" />
  </a>
  <a href="https://kodekloud.com/">
    <img src="https://img.shields.io/badge/KodeKloud-2E64FE?style=for-the-badge&logo=kubernetes&logoColor=white" />
  </a>
</div>

<br/>

<div align="center">

### About Me

I am a **DevOps &amp; Infrastructure enthusiast** and an Electronic &amp; Telecommunication Engineering undergraduate at the **University of Moratuwa**. I currently work as a **Trainee Infrastructure Engineer at MillenniumIT ESP**, focused on Enterprise Linux, Virtualization, and Cloud-native tooling.

I enjoy turning manual operations into automated, resilient systems &mdash; from **6DOF Robotic Arm control** and **Conveyor Belt inspection** to **Kubernetes lab platforms** and **RHEL automation**.

- Currently deepening: **Kubernetes, Terraform, and Platform Engineering**
- Ask me about: **RHEL &middot; VMware vSphere &middot; Docker &middot; Ansible**
- Reach me: **achinthar456@gmail.com**

</div>

---
"""

# ==========================================
# 2. ARSENAL SECTION
# ==========================================
ARSENAL_HTML = f"""
### The Arsenal

<table border="0">
  <tr>
    <td width="55%" valign="top">
      <br/>
      <h4 align="left">Infrastructure &amp; Virtualization</h4>
      <p>
        <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white" />
        <img src="https://img.shields.io/badge/VMware-607078?style=flat-square&logo=vmware&logoColor=white" />
        <img src="https://img.shields.io/badge/Red_Hat-EE0000?style=flat-square&logo=red-hat&logoColor=white" />
        <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
      </p>
      <h4 align="left">DevOps &amp; Automation</h4>
      <p>
        <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
        <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" />
        <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
        <img src="https://img.shields.io/badge/Ansible-000000?style=flat-square&logo=ansible&logoColor=white" />
        <img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" />
      </p>
      <h4 align="left">Observability &amp; CI/CD</h4>
      <p>
        <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" />
        <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" />
        <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" />
      </p>
      <h4 align="left">Scripting &amp; Languages</h4>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" />
        <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" />
        <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" />
      </p>
    </td>
    <td width="45%" valign="middle" align="center">
        <img src="{GIF_URL}" width="100%" alt="Coding Gif"/>
    </td>
  </tr>
</table>

---
"""

# ==========================================
# 3. STATS SECTION
# ==========================================
FOOTER_HTML = f"""
### GitHub Analytics

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&count_private=true&hide_border=true&title_color=2E64FE&icon_color=2E64FE&text_color=c9d1d9&bg_color=0d1117" alt="stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&langs_count=8&hide_border=true&title_color=2E64FE&text_color=c9d1d9&bg_color=0d1117" alt="top langs" />
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=dark&hide_border=true&background=0d1117&ring=2E64FE&fire=2E64FE&currStreakNum=2E64FE&currStreakLabel=2E64FE" alt="streak stats" />
</div>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username={USERNAME}&theme=onedark&no-frame=true&no-bg=true&margin-w=4&column=7" alt="trophies" />
</div>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}&theme=react-dark&hide_border=true&bg_color=0d1117&color=2E64FE&line=2E64FE&point=ffffff&area=true" alt="activity graph" width="95%" />
</div>

<br/>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,5,30&height=120&section=footer"/>
</div>
"""

# ==========================================
# LOGIC: CALCULATE STATS
# ==========================================

def get_modern_tracker():
    token = os.getenv('GH_TOKEN')
    if not token:
        raise ValueError("GH_TOKEN is missing")

    auth = Auth.Token(token)
    g = Github(auth=auth)
    user = g.get_user(USERNAME)

    now = datetime.now(pytz.utc)
    start_of_week = now - timedelta(days=now.weekday())
    start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

    html_blocks = []
    total_commits = 0

    print(f"Fetch start: {start_of_week.strftime('%Y-%m-%d')}")

    for repo_name, config in REPOS.items():
        try:
            repo = user.get_repo(repo_name)
            repo_url = repo.html_url
            count = repo.get_commits(since=start_of_week, author=USERNAME).totalCount

            goal = config['goal']
            label = config['label'].replace(" ", "%20")
            total_commits += count

            if count >= goal:
                color = "2ea44f"
            elif count > 0:
                color = "e3b341"
            else:
                color = "b60205"

            block = f"""
<div style="margin-bottom: 8px;">
  <a href="{repo_url}" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/{label}-2E64FE?style=for-the-badge&logo=github&logoColor=white" height="28" />
  </a>
  <img src="https://img.shields.io/badge/Commits-{count}%2F{goal}-{color}?style=for-the-badge" height="28" />
</div>
"""
            html_blocks.append(block)

        except Exception as e:
            print(f"Error {repo_name}: {e}")
            html_blocks.append(f"<p>{repo_name}: data unavailable</p>")

    return "\n".join(html_blocks), total_commits

# ==========================================
# WRITE TO FILE
# ==========================================

if __name__ == "__main__":
    tracker_content, total = get_modern_tracker()

    now_str = datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M UTC")

    velocity_section = f"""
<div align="center">
  <h3>Weekly Engineering Velocity</h3>
  <p><i>Last updated: {now_str}</i></p>

  <div align="center" style="margin: auto;">
    {tracker_content}
  </div>
</div>
"""

    badge_html = f'\n<p align="center"><img src="https://img.shields.io/badge/Total_Weekly_Commits-{total}-2E64FE?style=for-the-badge&logo=github&logoColor=white" /></p>\n'

    full_readme = HEADER_TOP + "\n" + ARSENAL_HTML + "\n" + velocity_section + "\n" + badge_html + "\n" + FOOTER_HTML

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(full_readme)

    print("README.md successfully rebuilt.")
