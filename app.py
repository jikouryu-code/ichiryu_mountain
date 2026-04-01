import streamlit as st

# ==========================================
# 一龍聖典 - 風の巻：販売用最終データ
# (十干・十二支・蔵干・五行・十二運 全網羅)
# ==========================================

DATA = {
    "JP": {
        "title": "一龍聖典",
        "vol": "- 風の巻 -",
        "sub": "四柱推命・基礎事典：【天】の理",
        "categories": {
            "🍃 十干（じっかん：魂の本質）": {
                "甲 (きのえ)": "【木陽：天空を貫く大樹】向上心に溢れる大黒柱。信念という根を深く張り、真っ直ぐに空を目指す宿命です。",
                "乙 (きのと)": "【木陰：風に舞う草花】柔軟性と忍耐力の象徴。仲間と協力し、踏まれても立ち上がる強さを持っています。",
                "丙 (ひのえ)": "【火陽：万物を照らす太陽】圧倒的な存在感。公明正大な生き方で周囲を明るく照らす光の先導者。",
                "丁 (ひのと)": "【火陰：闇を照らす灯火】内面に激しい情熱を秘めた知性。誰かの道を優しく照らす心の救世主。",
                "戊 (つちのえ)": "【土陽：威風堂々たる名山】包容力と安定感の守護者。どっしりと構え、多くの人を惹きつける徳の主。",
                "己 (つちのと)": "【土陰：慈愛の田園】万物を育む育成の天才。地道な努力を積み重ね、人を生かすことで自らも輝きます。",
                "庚 (かのえ)": "【金陽：変革を告げる刀剣】決断力とスピード。自分を厳しく磨き、古い価値観を打ち破る英雄の宿命。",
                "辛 (かのと)": "【金陰：輝きの宝石】高貴なる美意識。試練を磨きに変え、至高の価値を放つ審美の守護者。",
                "壬 (みずのえ)": "【水陽：奔流する大海】自由を愛する開拓者。時代の波を読み解き、大海原を渡る知略の英雄。",
                "癸 (みずのと)": "【水陰：心に染み入る雨】静かな努力で不可能を可能にする持続力。人々の心を潤す癒やしの賢者。"
            },
            "🐾 十二支（じゅうにし：魂のサイクル）": {
                "子 (ね)": "【始まりの滴】繁栄の種。静寂の中で知恵を絞り、新しい流れを創り出す知性の象徴。",
                "丑 (うし)": "【忍耐の土壌】着実な歩み。じっくりと実力を蓄え、揺るぎない大成を掴む土台の時期。",
                "寅 (とら)": "【芽吹きの咆哮】圧倒的な生命力。猛虎の如き行動力で新しい世界へ飛び出す勇気の主。",
                "卯 (う)": "【飛躍の和合】軽やかな跳躍。愛嬌と調和を武器に、障害をふわりと乗り越える幸運の使者。",
                "辰 (たつ)": "【変革の昇龍】強運と権威。大きな理想を掲げ、現実をダイナミックに変えゆく覇者の運命。",
                "巳 (み)": "【再生の洞察】不屈の精神。脱皮を繰り返し、美しく生まれ変わる再生と知恵の象徴。",
                "午 (うま)": "【陽光の疾走】光り輝く行動。自由を愛し、情熱を燃やして世界を駆け抜ける開拓者の魂。",
                "未 (ひつじ)": "【情愛の和】穏やかな守護。献身的に周囲を支え、和やかな世界を築き上げる平和の象徴。",
                "申 (さる)": "【多才の閃き】知恵の策士。機転と柔軟な発想で、どんな難局も遊び心で突破する才能。",
                "酉 (とり)": "【先見の果実】鋭い審美眼。本質を見抜く完璧な仕事ぶりが、周囲の絶大な信頼を生みます。",
                "戌 (いぬ)": "【忠義の守護】誠実と正義。一度信じた信念や恩義を生涯守り抜く、信頼のブランド。",
                "亥 (い)": "【邁進の覚悟】一途な邁進。迷いなく突き進む純粋な強さが、奇跡を起こす源となります。"
            },
            "🔑 蔵干（ぞうかん：十二支の本音）": {
                "子の蔵干 (癸)": "純粋な水の知恵。一途な想いと、冷静に物事を見通す深い洞察力を内に秘めています。",
                "丑の蔵干 (癸・辛・己)": "湿った土の忍耐。粘り強さの中に、鋭い感性と万物を育てる慈愛が同居しています。",
                "寅の蔵干 (戊・丙・甲)": "春の胎動。新しいことを始める勇気と、太陽のような情熱、揺るぎない信念を宿しています。",
                "卯の蔵干 (乙)": "柔らかな生命力。人当たりの良さの裏に、どんな環境でも生き抜く強かな芯の強さがあります。",
                "辰の蔵干 (乙・癸・戊)": "変幻自在の理想。高い志を持ちながら、現実的な計算と繊細な感性を使い分ける智謀家です。",
                "巳の蔵干 (戊・庚・丙)": "燃える情熱。社交的な顔の裏に、自らを厳しく磨き上げる刃のような決断力を秘めています。",
                "午の蔵干 (丙・己・丁)": "真夏の輝き。圧倒的な熱量で周囲を動かし、目的を達成するための献身的な知性を持ちます。",
                "未の蔵干 (丁・乙・己)": "晩夏の安らぎ。穏やかな調和の中に、情熱を絶やさず仲間を守り抜く粘り強さを秘めています。",
                "申の蔵干 (己・壬・庚)": "秋の訪れ。多才な知恵と、大海のような自由な発想、物事を完結させる鋭い決断力の塊です。",
                "酉の蔵干 (辛)": "研ぎ澄まされた美。一点の曇りもない純粋な美意識と、至高の価値を追求する完璧主義を宿します。",
                "戌の蔵干 (辛・丁・戊)": "守護の土徳。誠実な信念を守るために、内なる情熱を燃やし続ける不屈の防衛本能を持ちます。",
                "亥の蔵干 (甲・壬)": "冬の生命。静寂の中に大きな夢を抱き、未知の世界へ漕ぎ出す大海の如き知略を秘めています。"
            }
        }
    },
    "EN": {
        "title": "Ichiryu Seiten",
        "vol": "- Vol. Wind -",
        "sub": "Logic of Heaven: 10 Stems & 12 Branches",
        "categories": {
            "🍃 10 Heavenly Stems": {
                "甲 (Kinoe)": "[Wood-Yang / The Tree] Strong conviction and growth. Destined to reach for the sky.",
                "乙 (Kinoto)": "[Wood-Yin / The Flower] Resilience and flexibility. Flourishing through cooperation.",
                "丙 (Hinoe)": "[Fire-Yang / The Sun] Overwhelming presence. A leader who lights up the world.",
                "丁 (Hinoto)": "[Fire-Yin / The Flame] Intellectual passion. A savior who lights the path in the dark.",
                "戊 (Tsuchinoe)": "[Earth-Yang / The Mountain] Stability and tolerance. Attracting many with dignity.",
                "己 (Tsuchinoto)": "[Earth-Yin / The Field] Nurturing talent. Shining by helping others grow.",
                "庚 (Kanoe)": "[Metal-Yang / The Sword] Decision and speed. A hero who breaks old values.",
                "辛 (Kanoto)": "[Metal-Yin / The Jewel] High aesthetic sense. Turning trials into brilliance.",
                "壬 (Mizunoe)": "[Water-Yang / The Ocean] Freedom and exploration. A hero of intelligence and waves.",
                "癸 (Mizunoto)": "[Water-Yin / The Rain] Persistence through quiet effort. A sage of healing."
            },
            "🐾 12 Earthly Branches": {
                "子 (Ne)": "[Rat / The Seed] Prosperity. Intelligence that creates new flows in silence.",
                "丑 (Ushi)": "[Ox / The Soil] Steady progress. Building a foundation through accumulation.",
                "寅 (Tora)": "[Tiger / The Roar] Overwhelming vitality. Courage to leap into a new world.",
                "卯 (U)": "[Rabbit / The Leap] Harmony and charm. A messenger of luck who lightly overcomes obstacles.",
                "辰 (Tatsu)": "[Dragon / The Dragon] Fortune and authority. Changing reality dynamically.",
                "巳 (Mi)": "[Snake / The Insight] Indomitable spirit. Symbol of rebirth and wisdom.",
                "午 (Uma)": "[Horse / The Gallop] Shining action. The soul of a pioneer who runs with passion.",
                "未 (Hitsuji)": "[Goat / The Peace] Gentle protection. A symbol of peace who builds a harmonious world.",
                "申 (Saru)": "[Monkey / The Wit] Strategic mind. Talent to break through difficulty with playfulness.",
                "酉 (Tori)": "[Rooster / The Foresight] Sharp aesthetics. Perfect work that sees through the essence.",
                "戌 (Inu)": "[Dog / The Loyalty] Sincerity and justice. A brand of trust that protects convictions.",
                "亥 (I)": "[Boar / The Resolve] Pure momentum. The source of miracles through strength."
            }
        }
    }
}

# --- ページ設定 ---
st.set_page_config(page_title="Ichiryu Seiten - Wind", layout="centered")

# 言語状態
if 'lang' not in st.session_state:
    st.session_state.lang = "JP"

# デザインCSS
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stMarkdown, .stText, h1, h2, h3, p { color: #D4AF37 !important; text-align: center; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; width: 100%; }
    .stExpander { background-color: #1a1a1a; border: 1px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# 言語切替
if st.button("Language Switch (JP/EN)"):
    st.session_state.lang = "EN" if st.session_state.lang == "JP" else "JP"

L = DATA[st.session_state.lang]

# タイトル表示
st.title(L["title"])
st.subheader(L["vol"])
st.markdown(f"**{L['sub']}**")

# コンテンツ
for cat_name, items in L["categories"].items():
    with st.expander(cat_name):
        for word, desc in items.items():
            st.markdown(f"### {word}")
            st.write(desc)
            st.markdown("---")

st.sidebar.write("Ichiryu龍 監修")
st.sidebar.write("天地聖典：風の巻")