import streamlit as st
import random
import time
from datetime import datetime

# App Config
st.set_page_config(page_title="Happy Birthday, Love!", layout="centered")

# Secret Code Protection
password = st.text_input("Enter the secret code", type="password")
if password != "Princess":
    st.warning("Shhh... enter the code right lover boy")
    st.stop()

# Welcome Banner
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>🎉 Happy Birthday My Drama Queen! 🎉</h1>
    <h3 style='text-align: center;'>🌺 Welcome to your Birthday Playground!</h3>
    <p style='text-align: center;'>This isn’t just a page, it's a pocket universe, <br>crafted with laughter, poetry, games, and a truckload of love...</p>
    <p style='text-align: center;'><i>Aaj ka din hai khaas,<br>tere naam likha har ek saans.</i></p>
""", unsafe_allow_html=True)

# Birthday Vachan
st.subheader("📜 Birthday Vachan from Your Wife-in-Progress")
st.markdown("""
- Main kasam khati hoon ki har weekend tujhe khud haath se Biriyani banake khilaungi 🍜
- Main wada karti hoon ki jab tu thak jaye, main teri aankhon mein sapne bharungi 😴💭
- Main pratigya karti hoon ki teri har smile ke liye ek naya joke ready rakhungi 😄
""")

# Rapid Fire Quiz
st.subheader("💘 Rapid Fire: How Well Do You Know Your Ladylove?")
score = 0
if st.radio("Mera sapna honeymoon destination?", ["Maldives", "Shimla", "Switzerland", "Rajasthan"]) == "Switzerland":
    score += 1
if st.radio("What makes me instantly happy?", ["Chocolate", "Your hug", "Dancing", "Long call"]) == "Your hug":
    score += 1
if st.radio("What’s my hidden talent?", ["Rapping", "Writing poetry", "Drawing", "Cooking"]) == "Writing poetry":
    score += 1

if score == 3:
    st.success("Uff... Tu toh meri jaan ka encyclopedia hai! 🔥")
elif score == 2:
    st.info("Not bad! You're on fire! 💖")
else:
    st.warning("Brush up your Eshaa gyaan 😛")

# Birthday Letter from Future Eshaa
st.write("---")
st.subheader("💌 Letter from Future Eshaa")
future_letter = """
Hey cutie patootie,

It's 11th April, 2035. You're now 32 and still somehow more annoying and adorable than ever.  
We're sitting in our cozy little flat, chai in hand, and still laughing at the dumb jokes we made on this very birthday page you’re reading now.

You grew more handsome, more patient, more 'dad-joke' kinda funny.

And me? Still madly, irrevocably, hopelessly in love with you.

So, happy birthday... not just for today, but for all the decades to come. 🥹

Love,  
Your future wifey (who still beats you at every game) 💙
"""
if st.button("Click to read a letter from Future Eshaa 📜"):
    for line in future_letter.split("\n"):
        st.markdown(f"<p style='font-size: 18px'>{line}</p>", unsafe_allow_html=True)
        time.sleep(0.8)
# Spin the Wheel
st.subheader("🎡 Spin the Wheel of Love (Eshaa Style)")
wheel = [
    "You owe me a back massage 😏",
    "Say 'I love you' in 3 languages 💬",
    "Show off your muscles(Yes,right now!!)",
    "Dance for me !!"
]
if st.button("Spin the Wheel for a dare💖"):
    st.success(random.choice(wheel))
    st.balloons()

# If We Were Game
st.subheader("🧠 'If We Were...' Couple Game")
st.markdown("""
- If we were a dish, we'd be — Masala Dosa & Filter Coffee — spicy and soothing 😜
- If we were a movie, we'd be — Jab we Met — dramatic, passionate, and unforgettable 💃🕺
- If we were a song, we'd be — Raabta by Arijit Singh 🎶
""")

# Genie Eshaa's 3 Wishes
st.write("---")
st.subheader("🧞‍♀️ Your 3 Birthday Wishes from Genie Eshaa")
if st.button("Summon Genie Eshaa"):
    wishes = [
        "💖 I grant you infinite patience (for dealing with me!)",
        "🌍 I grant you a world tour with me, hand-in-hand",
        "🎮 I grant you 10 guilt-free hours of watching reels... but only if I get cuddles!"
    ]
    for wish in wishes:
        st.markdown(f"- {wish}")
        time.sleep(1)

# One Day in Our Future Generator
st.subheader("💭 'One Day in Our Future…'")
futures = [
    "...we’ll be lying under the stars on our terrace, wrapped in one blanket.",
    "...you’ll wake up to the smell of chai and me humming old Bollywood songs.",
]
if st.button("Imagine One Day 💫"):
    st.info(random.choice(futures))

# Compliment Storm
st.subheader("💬 Compliment Storm")
compliments = [
    "You make my heart do backflips.",
    "You're my home, my peace, my chaos – all in one.",
    "You age like fine wine. No, scratch that – you're better than wine! 🍷💙"
]
if st.button("Shower Me With Love 💌"):
    for c in compliments:
        st.success(c)
        time.sleep(1)

# Love Riddle Unlock
st.subheader("🧩 Love Riddle Unlock")
answer = st.text_input("I’m not a bird, but I make hearts soar,I’m not a lock, yet I open every door.I can’t be seen, yet I color your view —What am I, that binds me to you??")
if answer.lower() == "love":
    st.success("Correct! Unlock: I adore you more each day ✨")

# Promise of the Day
st.subheader("📝 Promise of the Day")
promises = [
    "I promise to be your warm blanket on the coldest nights.",
    "I promise to dance with you in the kitchen at 2 AM.",
    "I promise to never let our spark fade."
]
if st.button("Reveal Today's Promise 💝"):
    st.markdown(f"🌟 {random.choice(promises)}")

# Love Meter
st.subheader("❤️‍🔥 Love Meter")
if st.button("Test Our Love Compatibility 💘"):
    love_score = random.randint(85, 100)
    st.metric("🔥 Compatibility Score", f"{love_score}%")

# Would You Rather
st.subheader("🤔 Would You Rather")
st.radio("Choose one:", ["Netflix & Chill night 🛋️", "Sunset drive & Cold coffee 🌇"])
st.radio("And this:", ["Candlelight dinner 🍷", "Homemade Maggie with me 💖"])

# Gift of the Day
st.subheader("🎁 Gift of the Day")
gifts = ["One surprise date planned by me 😘", "A song I'll write just for you 🎶", "Unlimited forehead kisses for a week 💋"]
if st.button("Reveal My Gift 🎀"):
    st.success(random.choice(gifts))

# Love Contract
st.subheader("📜 Love Contract")
st.markdown("""
I, the undersigned (Birthday Rockstar), hereby agree to:

1. Build a cozy home library for Eshaa 📚
2. Keep it stocked with endless books she can get lost in 📖
3. Love her with all my heart, especially when she’s being dramatic (which is always 😘)

🖋️ Signed with love: ________
""")
st.subheader("🌠 Manifest-a-Memory")
st.write("Write a memory you want to make with me... it’ll be stored as a wish from the heart 💌")

# Text input for manifesting
new_memory = st.text_input("What shall we manifest today?", key="manifest")

# Store and display
if 'memory_list' not in st.session_state:
    st.session_state.memory_list = []

if st.button("Manifest It 💫") and new_memory:
    timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")
    st.session_state.memory_list.append(f"📝 {new_memory} *(added on {timestamp})*")
    st.success("Manifestation added to our future diary!")

if st.session_state.memory_list:
    st.markdown("### ✨ Our Manifested Memories:")
    for m in reversed(st.session_state.memory_list):
        st.markdown(m)
st.subheader("Get Krishna's Blessings")
krishna_quotes = [
    "Where there is love, there I am.",
    "In every ras of your relationship, remember — I dance too.",
    "Love isn’t just between you two. I’m the string that ties your hearts together."
]
if st.button("Get Krishna’s Blessing 💫"):
    st.success(random.choice(krishna_quotes))
st.subheader("🎨 Love in Doodles")
st.write("Sometimes, words are better drawn than said.")

ascii_arts = [
    r"""
    .-''''-.
   /        \
  |  O    O  |
  |   .----. |
  |  |.----.| 
   \_/      \_/
  You + Me = ❤️
    """,
    r"""
     (•‿•)
    /     \
   |  ❤️  |
    \___/ 
  You're my favorite art 🖌️
    """,
    r"""
      |\_/|
      | @ @   Woof!
      |   <>              _  
      |  _/\------____ ((| |))
      |               `--' |
  ____|_       ___|   |___.'
 /_/_____/____/_______|
 You're doggone adorable 🐶
    """,
    r"""
   ~~~~~~~~~~~~~
   |   I 💙 U   |
   ~~~~~~~~~~~~~
      \   ^__^
       \  (oo)\_______
          (__)\       )\/\
              ||----w |
              ||     ||
 Moo point: I love you 🐄
    """
]

if 'ascii_index' not in st.session_state:
    st.session_state.ascii_index = 0

if st.button("Show Me a Doodle! ✏️"):
    st.session_state.ascii_index = (st.session_state.ascii_index + 1) % len(ascii_arts)

st.code(ascii_arts[st.session_state.ascii_index], language="")


# Birthday Countdown
st.subheader("⏳ Countdown to Next Birthday")
target = datetime(datetime.now().year + 1, 4, 11, 0, 0, 0)
now = datetime.now()
delta = target - now
if delta.total_seconds() > 0:
    st.info(f"Next birthday in {delta.days} days!😎")
else:
    st.success("It's your day today! Let's celebrate! 🎂")

# Footer
st.markdown("<p style='text-align: center;'>Made with 💻 + 💙 + infinite mohabbat, <b>Eshaa</b>.</p>", unsafe_allow_html=True)
st.snow()
