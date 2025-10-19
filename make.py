import streamlit as st
import requests
from transformers import pipeline

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="Yash Raj Sharma | Samurai AI Resume 🇯🇵",
    page_icon="⚔️",
    layout="wide"
)

# -----------------------------------------------------
# Style – Dark Samurai Theme
# -----------------------------------------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 20% 20%, #0a0a0a 0%, #050505 100%);
    color: #e0e0e0;
    font-family: 'Noto Sans JP', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #0d0d0d;
    border-right: 2px solid #e63946;
}
h1, h2, h3, h4 {
    color: #e63946;
    font-family: 'Noto Serif JP', serif;
}
div.stButton > button {
    background-color: #e63946;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #c72c3a;
}
a {
    color: #e63946;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
hr {
    border: 1px solid #e63946;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Sidebar Info
# -----------------------------------------------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/f/f8/Tokyo_Skyline_at_night_-_Tokyo_Tower.jpg", use_column_width=True)
st.sidebar.title("📄 Contact")
st.sidebar.write("📧 iitian6800@gmail.com")
st.sidebar.write("💼 [GitHub](https://github.com/yashraj-8)")
st.sidebar.write("🌐 [LinkedIn](https://linkedin.com/in/yashraj-8)")
st.sidebar.write("🏫 MIT (MAHE), Bengaluru — CSE")
st.sidebar.markdown("---")
st.sidebar.caption("⚔️ Built by Yash Raj Sharma | Inspired by Japanese Aesthetics 🇯🇵")

# -----------------------------------------------------
# Language Toggle
# -----------------------------------------------------
lang = st.sidebar.selectbox("🌐 Language", ["English", "日本語"])

# -----------------------------------------------------
# Header (Bilingual)
# -----------------------------------------------------
if lang == "English":
    st.title("⚔️ Yash Raj Sharma")
    st.subheader("AI Engineer | Creative Technologist | Future Innovator in Japan 🇯🇵")
    st.markdown("**“Order, Precision, and Soul — The Way of the Coder.”**  \nExploring the fusion of AI, art, and samurai discipline.")
else:
    st.title("⚔️ ヤシュ・ラージ・シャルマ")
    st.subheader("AIエンジニア | クリエイティブ・テクノロジスト | 日本での未来のイノベーター 🇯🇵")
    st.markdown("**「秩序、精密さ、魂 ― それがコーダーの道。」**  \nAIと芸術、そして侍の精神を融合させる旅。")

# -----------------------------------------------------
# GitHub Projects
# -----------------------------------------------------
def fetch_github_repos(yashraj-8):
    url = f"https://api.github.com/users/{yashraj-8}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        repos = sorted(data, key=lambda x: x['stargazers_count'], reverse=True)
        return repos[:5]
    return []

st.header("💻 Projects / プロジェクト")
repos = fetch_github_repos("yashraj-8")

if repos:
    for repo in repos:
        st.markdown(f"### [{repo['name']}]({repo['html_url']})")
        st.write(repo['description'] or "_No description available_")
        st.caption(f"⭐ {repo['stargazers_count']} stars | 🍴 {repo['forks_count']} forks")
else:
    st.warning("⚠️ Unable to fetch GitHub projects. Please check username or internet connection.")

# -----------------------------------------------------
# Skills Section
# -----------------------------------------------------
st.header("🧠 Skills / スキル")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Core 基礎")
    st.write("- Python (Advanced)\n- APIs & Automation\n- Git / CLI / Linux")

with col2:
    st.markdown("### 🤖 AI / ML 人工知能")
    st.write("- Transformers (Hugging Face)\n- Deep Learning (PyTorch / TensorFlow)\n- NLP, Vision, Multimodal AI")

with col3:
    st.markdown("### 🎨 Creative Tech クリエイティブ技術")
    st.write("- Stable Diffusion / ControlNet\n- LangChain / Generative Apps\n- AI-driven Storytelling")

# -----------------------------------------------------
# Mini AI Chatbot (About Me Bot)
# -----------------------------------------------------
st.header("💬 Chat with My AI / 私のAIと話す")

bot_intro_en = """Hello! I’m Yash’s AI twin 🤖. 
Ask me about his skills, projects, goals, or passion for Japan."""
bot_intro_jp = """こんにちは！私はヤシュのAIツインです 🤖。
彼のスキル、プロジェクト、日本への情熱などについて質問してください。"""

if lang == "English":
    st.write(bot_intro_en)
else:
    st.write(bot_intro_jp)

chat_input = st.text_input("💭 Your Question / 質問を入力してください:")

if chat_input:
    try:
        chatbot = pipeline("text-generation", model="gpt2")
        answer = chatbot(f"Yash Raj Sharma is an AI engineer who loves Japan. Question: {chat_input}\nAnswer:", 
                         max_new_tokens=60, do_sample=True, temperature=0.8)[0]['generated_text']
        st.info(answer)
    except Exception as e:
        st.error(f"⚠️ Chatbot unavailable: {e}")

# -----------------------------------------------------
# AI Demo: Sentiment Analysis
# -----------------------------------------------------
st.header("🧪 Sentiment Analyzer / 感情分析")
try:
    analyzer = pipeline("sentiment-analysis")
    text = st.text_area("Enter a sentence / 文を入力:", "Japan blends technology with soul beautifully.")
    if st.button("Analyze / 分析する"):
        result = analyzer(text)[0]
        label_map = {"POSITIVE": "😊 Positive / ポジティブ", "NEGATIVE": "😞 Negative / ネガティブ", "NEUTRAL": "😐 Neutral / ニュートラル"}
        st.success(f"{label_map.get(result['label'], result['label'])} — Confidence: {result['score']:.2f}")
except Exception as e:
    st.error(f"⚠️ Could not load AI model: {e}")

# -----------------------------------------------------
# GitHub Activity
# -----------------------------------------------------
st.header("📊 GitHub Activity / 活動")
st.image(f"https://github-readme-streak-stats.herokuapp.com/?user=yashraj-8&theme=tokyonight", use_column_width=True)

# -----------------------------------------------------
# Footer
# -----------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>🌸 Built with ❤️ & Python by <b>Yash Raj Sharma</b> | Inspired by the Soul of the Samurai 🇯🇵</center>",
    unsafe_allow_html=True
)

