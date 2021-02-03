import streamlit as st
import random

def main():
	index = random.randint(0, len(affirmations) - 1)
	st.title(affirmations[index])

affirmations = [
	"I strive to make the most of today.",
	"I practice accepting people around me without repressing my feelings.",
	"I cultivate the willingness to vocalise my feelings on things that matter to me."
]


if __name__ == '__main__':
    main()