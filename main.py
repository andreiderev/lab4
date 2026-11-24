from file_creator import create_source_file

SOURCE_FILE = "TF16_1.txt"
RESULT_FILE = "TF16_2.txt"


def main():
    # Етап а): створення початкового файлу TF16_1 (реалізовано тімлідом)
    if not create_source_file(SOURCE_FILE):
        return

    # TODO (Басанець Олександр): підключити модуль оброблення файлу (частина б)
    # TODO (Басанець Олександр): підключити функцію виведення результату (частина в)


if __name__ == "__main__":
    main()