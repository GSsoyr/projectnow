import streamlit as st

# Заглавие
st.title("Галерия от любими животни")

# Инициализация на животните (примерни)
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
