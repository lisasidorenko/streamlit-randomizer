import random
import streamlit as st
import os

# Имя файла, в котором будет храниться список оставшихся слов
FILE_NAME = "remaining_words.txt"

# Начальный список слов
words = ["Кринж", "Радость", "Грусть", "Страх", "Отвращение", "Удивление", 
         "Брезгливость", "Смущение", "Зависть", "ЧСВ", "Ностальгия", "Навязчивость"]

# Функция для чтения оставшихся слов из файла
def load_words():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            remaining_words = file.read().splitlines()
    else:
        remaining_words = words.copy()  # Если файла нет, используем исходный список слов
        save_words(remaining_words)  # Сохраняем его в файл
    return remaining_words

# Функция для сохранения оставшихся слов в файл
def save_words(remaining_words):
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(remaining_words))

# Основная функция приложения
def main():
    st.title("Рандомайзер эмоций")
    st.write("Нажмите на кнопку, чтобы получить случайную эмоцию. Каждая эмоция выпадает только один раз для всех пользователей.")

    # Загружаем список оставшихся слов
    remaining_words = load_words()

    # Проверяем, есть ли оставшиеся слова
    if remaining_words:
        # Используем состояние для хранения информации о том, выбрано ли слово
        if 'word_chosen' not in st.session_state:
            st.session_state.word_chosen = False
            st.session_state.selected_word = ""  # Инициализируем переменную для выбранного слова

        # Если слово еще не выбрано, показываем кнопку
        if not st.session_state.word_chosen:
            if st.button("Выбрать случайную эмоцию"):
                # Выбираем случайное слово и удаляем его из списка
                st.session_state.selected_word = random.choice(remaining_words)
                remaining_words.remove(st.session_state.selected_word)
                save_words(remaining_words)  # Сохраняем обновлённый список в файл

                # Устанавливаем состояние выбора слова в True
                st.session_state.word_chosen = True
            # Выводим выбранное слово
                st.success(f"Твоя эмоция: {selected_word}")
        else:
            st.warning("Уго! Обязательно запомни свою эмоцию, ведь тебе ещё нужно презентовать её в субботу!;)")
            st.info(f"Твоя эмоция: {st.session_state.selected_word}")
    else:
        st.warning("Упс, кажется эмоций больше не осталось:(")

if __name__ == "__main__":
    main()
