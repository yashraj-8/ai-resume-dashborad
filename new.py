import streamlit as st
import requests
import locale
from transformers import pipeline

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Yash Raj Sharma | AI Resume Dashboard",
    page_icon="⚔️",
    layout="wide"
)

# ---------- AUTO LANGUAGE DETECTION ----------
try:
    loc = locale.getdefaultlocale()[0]
    if loc and "JP" in loc.upper():
        auto_lang = "日本語 (Japanese)"
    else:
        auto_lang = "English"
except:
    auto_lang = "English"

# ---------- SIDEBAR LANGUAGE TOGGLE ----------
lang = st.sidebar.selectbox("🌐 Language / 言語", ["English", "日本語 (Japanese)"], index=0 if auto_lang == "English" else 1)

# ---------- CUSTOM CSS ----------
samurai_style = """
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #0d0d0d 0%, #1b1b1b 60%, #000000 100%);
    color: white;
}
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #111111, #0d0d0d);
}
h1, h2, h3, h4 {
    font-family: 'Noto Sans JP', sans-serif;
    color: #e63946;
    letter-spacing: 1px;
}
a {
    color: #fca311 !important;
    text-decoration: none;
}
a:hover {
    color: #ffb703 !important;
}
textarea, input {
    background-color: #1b1b1b !important;
    color: white !important;
    border-radius: 8px !important;
}
</style>
"""
st.markdown(samurai_style, unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/1/1a/Tokyo_Metropolitan_Government_Building_2019.jpg",
    use_container_width=True
)
st.sidebar.title("📩 Contact Info / 連絡先")
st.sidebar.markdown("**Name / 名前:** Yash Raj Sharma")
st.sidebar.markdown("**Email / メール:** iitian6800@gmail.com")
st.sidebar.markdown("**GitHub:** [yashraj-8](https://github.com/yashraj-8)")
st.sidebar.markdown("**LinkedIn:** [Yash Raj Sharma](https://www.linkedin.com/in/yashraj-sharma-a05812375)")
st.sidebar.markdown("---")
st.sidebar.caption("Inspired by Japan 🇯🇵 | Dark Samurai Theme ⚔️")

# ---------- HEADER ----------
if lang == "English":
    st.title("⚔️ Yash Raj Sharma")
    st.subheader("AI Engineer | Creative Technologist | Future Innovator in Japan 🇯🇵")
    st.write("Aspiring AI engineer passionate about Transformers, generative AI, and creative technology.")
else:
    st.title("⚔️ ヤシュ・ラジ・シャルマ")
    st.subheader("AIエンジニア | クリエイティブテクノロジスト | 日本の未来のイノベーター 🇯🇵")
    st.write("トランスフォーマー、生成AI、そして創造的テクノロジーに情熱を注ぐAIエンジニア。")

# ---------- FETCH GITHUB PROJECTS ----------
import requests

def fetch_github_repos(yashraj):
    url = f"https://api.github.com/users{yashraj}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"Repositories of {yashraj}:")
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print(f"Failed to fetch repos for {yashraj}. Status code: {response.status_code}")
        return repos[:5]
    return []

repos = fetch_github_repos("yashraj-8")

if lang == "English":
    st.header("💻 Top GitHub Projects")
else:
    st.header("💻 人気のGitHubプロジェクト")

for repo in repos:
    st.markdown(f"### [{repo['name']}]({repo['html_url']})")
    if repo['description']:
        st.write(repo['description'])
    st.caption(f"⭐ {repo['stargazers_count']} | 🍴 {repo['forks_count']}")

# ---------- SKILLS ----------
if lang == "English":
    st.header("🧠 Skills")
else:
    st.header("🧠 スキル")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### ⚙️ Core / 基礎")
    st.write("- Python\n- Data Structures\n- APIs\n- Git & CLI")

with col2:
    st.markdown("### 🤖 AI / 機械学習")
    st.write("- Transformers (Hugging Face)\n- PyTorch / TensorFlow\n- NLP / Vision\n- LangChain")

with col3:
    st.markdown("### 🎨 Creative Tech / クリエイティブ技術")
    st.write("- Generative AI\n- Streamlit Dashboards\n- Creative Coding")

# ---------- AI CHATBOT ----------
if lang == "English":
    st.header("🧠 Mini AI Chatbot")
    st.write("Chat with a small AI model (offline transformer).")
else:
    st.header("🧠 ミニAIチャットボット")
    st.write("軽量AIモデルと会話してみよう。")

chatbot = pipeline("text-generation", model="distilgpt2")

user_input = st.text_area("💬 " + ("Type your message here:" if lang == "English" else "メッセージを入力してください："))
if st.button("Send" if lang == "English" else "送信"):
    if user_input:
        with st.spinner("Thinking like a Samurai... 🥋" if lang == "English" else "サムライのように考えています... 🥋"):
            response = chatbot(user_input, max_length=60, do_sample=True, top_k=50)[0]["generated_text"]
            st.success(response)
    else:
        st.warning("Please enter a message first." if lang == "English" else "メッセージを入力してください。")

# ---------- FOOTER ----------
st.markdown("---")
if lang == "English":
    st.markdown("💬 *Built with ❤️ and Python by Yash Raj Sharma*")
else:
    st.markdown("💬 *愛とPythonで作られた — ヤシュ・ラジ・シャルマ*")
