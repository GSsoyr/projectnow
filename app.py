import streamlit as st
import random

# Заглавие
st.title("Галерия от любими животни")

# Инициализация
if "animals" not in st.session_state:
    st.session_state.animals = [
        {"name": "Крава", "image": "https://via.placeholder.com/300?text=Крава", "description": "Млечна крава, дава много мляко."},
        {"name": "Овца", "image": "https://via.placeholder.com/300?text=Овца", "description": "Пухкава овца, дава вълна."},
        {"name": "Кон", "image": "https://via.placeholder.com/300?text=Кон", "description": "Бърз кон, обича да тича."}
    ]

# --- Добавяне на животно ---
st.header("Добави ново животно")
name = st.text_input("Име на животното")
description = st.text_area("Описание")
image_url = st.text_input("URL на картинка")

if st.button("Добави"):
    if name and description and image_url:
        st.session_state.animals.append({"name": name, "image": image_url, "description": description})
        st.success(f"{name} е добавено!")
    else:
        st.warning("Попълнете всички полета!")

# --- Премахване на животно ---
if st.session_state.animals:
    st.header("Премахни животно")
    remove_name = st.selectbox("Изберете животно за премахване", [a["name"] for a in st.session_state.animals])
    if st.button("Премахни"):
        st.session_state.animals = [a for a in st.session_state.animals if a["name"] != remove_name]
        st.success(f"{remove_name} е премахнато!")

# --- Интересни допълнения ---
if st.session_state.animals:
    st.header("Интерактивни функции")

    # Брояч
    st.write(f"Общо животни в галерията: {len(st.session_state.animals)}")

    # Случайно животно
    if st.button("Покажи случайно животно"):
        animal = random.choice(st.session_state.animals)
        st.subheader(animal["name"])
        st.image(animal["image"], use_column_width=True)
        st.write(animal["description"])

    # Филтър по име
    search_name = st.text_input("Търсене по име на животно")
    if search_name:
        filtered = [a for a in st.session_state.animals if search_name.lower() in a["name"].lower()]
        if filtered:
            st.write(f"Намерени животни: {len(filtered)}")
            for animal in filtered:
                st.subheader(animal["name"])
                st.image(animal["image"], use_column_width=True)
                st.write(animal["description"])
        else:
            st.info("Няма животни с това име.")

# --- Визуализация на галерията ---
st.header("Галерия")
if st.session_state.animals:
    for i in range(0, len(st.session_state.animals), 3):
        cols = st.columns(3)
        for idx, animal in enumerate(st.session_state.animals[i:i+3]):
            with cols[idx]:
                st.subheader(animal["name"])
                st.image(animal["image"], use_column_width=True)
                st.write(animal["description"])
else:
    st.info("Таблица е празна. Добавете животно!")
