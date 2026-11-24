# Модуль для оброблення файлу TF16_1 та виведення вмісту TF16_2 (частини б і в)

VOWELS = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouyAEIOUY"
PUNCTUATION = ".,!?;:—-\"()[]{}"


def extract_vowel_words(text):
    # Заміна розділових знаків на пробіли для коректного виділення слів
    for symbol in PUNCTUATION:
        text = text.replace(symbol, " ")

    words = text.split()
    vowel_words = []

    for word in words:
        if word and word[0] in VOWELS:
            vowel_words.append(word)

    return vowel_words


def process_files(source_filename, result_filename):
    # Частина б): читання TF16_1, пошук слів на голосну та запис у TF16_2
    try:
        with open(source_filename, "r", encoding="utf-8") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{source_filename}' не знайдено.")
        return False
    except OSError as error:
        print(f"Помилка відкриття файлу '{source_filename}': {error}")
        return False

    vowel_words = extract_vowel_words(content)

    try:
        with open(result_filename, "w", encoding="utf-8") as result_file:
            for word in vowel_words:
                result_file.write(word + "\n")
        print(f"Знайдено слів на голосну: {len(vowel_words)}. Результат збережено у '{result_filename}'.")
        return True
    except OSError as error:
        print(f"Помилка відкриття або запису файлу '{result_filename}': {error}")
        return False


def print_result_file(result_filename):
    # Частина в): читання вмісту файлу TF16_2 та друк по рядках
    try:
        with open(result_filename, "r", encoding="utf-8") as result_file:
            print(f"\nВміст файлу '{result_filename}':")
            for line in result_file:
                print(line.strip())
        return True
    except FileNotFoundError:
        print(f"Помилка: файл '{result_filename}' не знайдено.")
        return False
    except OSError as error:
        print(f"Помилка відкриття файлу '{result_filename}': {error}")
        return False