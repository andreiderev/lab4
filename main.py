from file_creator import create_source_file
from file_processor import process_files, print_result_file

SOURCE_FILE = "TF16_1.txt"
RESULT_FILE = "TF16_2.txt"


def main():
    # Частина а): створення текстового файлу TF16_1
    if not create_source_file(SOURCE_FILE):
        return

    # Частина б): пошук слів, що починаються з голосної, та запис у TF16_2
    if not process_files(SOURCE_FILE, RESULT_FILE):
        return

    # Частина в): читання та построковий друк вмісту TF16_2
    print_result_file(RESULT_FILE)


if __name__ == "__main__":
    main()