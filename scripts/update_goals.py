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
    "mcp-vcenter-agent": {"goal": 5, "label": "MCP vCenter Agent"},
    "Computer_Vision_Projects": {"goal": 3, "label": "Computer Vision"},
    "langchain-rag-tutorial": {"goal": 3, "label": "LangChain RAG"},
    "Cudalicious-anomaly-detection": {"goal": 3, "label": "Anomaly Detection"},
}

# ==========================================
# 1. HEADER SECTION
# ==========================================
HEADER_TOP = f"""<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=280&section=header&text=Achintha%20Rukshan&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI%2FML%20Engineer%20%7C%20Computer%20Vision%20%7C%20Cloud%20%26%20MLOps&descAlignY=54&descSize=18"/>
</div>

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=8A2BE2&center=true&vCenter=true&width=560&lines=Building+%26+Deploying+ML+Models;Computer+Vision+%26+Deep+Learning;From+Notebook+to+Cloud+in+Production;MLOps+%7C+LLMs+%7C+Cloud-Native+AI" alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username={USERNAME}&label=Profile%20Views&color=8A2BE2&style=for-the-badge" alt="profile views" />
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
  <a href="https://huggingface.co/">
    <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  </a>
</div>

<br/>

<div align="center">

### About Me

I am an **AI/ML Engineer** and Electronic &amp; Telecommunication Engineering undergraduate at the **University of Moratuwa**, currently a **Trainee Infrastructure Engineer at MillenniumIT ESP**. I work at the intersection of **Machine Learning and Cloud** &mdash; I don't just train models in notebooks, I take them all the way to **production: containerized, deployed, and monitored on the cloud.**

- Focus: **Computer Vision, Deep Learning, and LLM / RAG systems**
- Shipping with: **PyTorch &middot; FastAPI &middot; Docker &middot; AWS &middot; Kubernetes**
- Exploring: **MLOps &mdash; CI/CD for models, experiment tracking, scalable inference**
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
      <h4 align="left">AI / Machine Learning</h4>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
        <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" />
        <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" />
        <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" />
        <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" />
      </p>
      <h4 align="left">Computer Vision &amp; Deep Learning</h4>
      <p>
        <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />
        <img src="https://img.shields.io/badge/YOLO-00FFFF?style=flat-square&logo=yolo&logoColor=black" />
        <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" />
        <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" />
        <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" />
        <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" />
      </p>
      <h4 align="left">Cloud &amp; MLOps</h4>
      <p>
        <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white" />
        <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
        <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
        <img src="https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white" />
        <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" />
        <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" />
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
  <img height="165" src="https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&count_private=true&hide_border=true&title_color=8A2BE2&icon_color=8A2BE2&text_color=c9d1d9&bg_color=0d1117" alt="stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&langs_count=8&hide_border=true&title_color=8A2BE2&text_color=c9d1d9&bg_color=0d1117" alt="top langs" />
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=dark&hide_border=true&background=0d1117&ring=8A2BE2&fire=8A2BE2&currStreakNum=8A2BE2&currStreakLabel=8A2BE2" alt="streak stats" />
</div>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username={USERNAME}&theme=onedark&no-frame=true&no-bg=true&margin-w=4&column=7" alt="trophies" />
</div>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}&theme=react-dark&hide_border=true&bg_color=0d1117&color=8A2BE2&line=8A2BE2&point=ffffff&area=true" alt="activity graph" width="95%" />
</div>

<br/>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer"/>
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
    <img src="https://img.shields.io/badge/{label}-8A2BE2?style=for-the-badge&logo=github&logoColor=white" height="28" />
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
  <h3>Weekly Build Velocity</h3>
  <p><i>Last updated: {now_str}</i></p>

  <div align="center" style="margin: auto;">
    {tracker_content}
  </div>
</div>
"""

    badge_html = f'\n<p align="center"><img src="https://img.shields.io/badge/Total_Weekly_Commits-{total}-8A2BE2?style=for-the-badge&logo=github&logoColor=white" /></p>\n'

    full_readme = HEADER_TOP + "\n" + ARSENAL_HTML + "\n" + velocity_section + "\n" + badge_html + "\n" + FOOTER_HTML

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(full_readme)

    print("README.md successfully rebuilt.")
