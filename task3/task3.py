# !!! Это задание не получилось решить, но я решила оставить его в репозитории
import json

def fill_values(tests_structure, values):
    for test in tests_structure.get('tests', []):
        test_id = test.get('id')
        if test_id in values:
            test['value'] = values[test_id]  # Добавляем значение из values.json
    return tests_structure

def generate_report(values_path, tests_path, report_path):
    try:
        # Читаем значения из файла values.json
        with open(values_path, 'r', encoding = 'utf-8') as f:
            values = json.load(f)

        # Читаем структуру тестов из файла tests.json
        with open(tests_path, 'r', encoding = 'utf-8') as f:
            tests_structure = json.load(f)

        # Заполняем структуру значениями
        report_data = fill_values(tests_structure, values)

        # Сохраняем отчет в reports.json
        with open(report_path, 'w', encoding = 'utf-8') as f:
            json.dump(report_data, f, indent = 4, ensure_ascii = False)

        print(f"Отчет успешно сгенерирован и сохранен в {report_path}")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


generate_report('values.json', 'tests.json', 'reports.json')
