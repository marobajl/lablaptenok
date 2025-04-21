import xml.etree.ElementTree as ET
from pathlib import Path

def validate_xml(xml_file, xsd_file):
    """Валидация XML по XSD схеме"""
    try:
        from lxml import etree
        xmlschema = etree.XMLSchema(etree.parse(xsd_file))
        xml_doc = etree.parse(xml_file)
        if xmlschema.validate(xml_doc):
            print("XML документ валиден по XSD схеме")
            return True
        else:
            print("XML документ не валиден по XSD схеме:")
            print(xmlschema.error_log)
            return False
    except ImportError:
        print("Для валидации необходимо установить модуль lxml")
        return False
    except Exception as e:
        print(f"Ошибка при валидации: {e}")
        return False

def process_library(xml_file):
    """Обработка XML файла библиотеки"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Вывод всех книг
        print("\nСписок всех книг в библиотеке:")
        total_price = 0
        book_count = 0
        
        for book in root.findall('book'):
            book_id = book.get('id')
            title = book.find('title').text
            author = book.find('author').text
            year = book.find('year').text
            genre = book.find('genre').text
            price = float(book.find('price').text)
            
            print(f"\nID: {book_id}")
            print(f"Название: {title}")
            print(f"Автор: {author}")
            print(f"Год: {year}")
            print(f"Жанр: {genre}")
            print(f"Цена: {price:.2f}")
            
            total_price += price
            book_count += 1
        
        if book_count > 0:
            avg_price = total_price / book_count
            print(f"\nСредняя цена книги: {avg_price:.2f}")
        
        filter_genre = input("\nВведите жанр для фильтрации (оставьте пустым чтобы пропустить): ")
        if filter_genre:
            print(f"\nКниги в жанре '{filter_genre}':")
            found = False
            for book in root.findall('book'):
                if book.find('genre').text.lower() == filter_genre.lower():
                    print(f"- {book.find('title').text} ({book.find('year').text})")
                    found = True
            if not found:
                print("Книг в указанном жанре не найдено.")
        
        # Фильтрация по году
        filter_year = input("\nВведите год для фильтрации (оставьте пустым чтобы пропустить): ")
        if filter_year:
            try:
                year = int(filter_year)
                print(f"\nКниги изданные в {year} году:")
                found = False
                for book in root.findall('book'):
                    if int(book.find('year').text) == year:
                        print(f"- {book.find('title').text} ({book.find('genre').text})")
                        found = True
                if not found:
                    print(f"Книг изданных в {year} году не найдено.")
            except ValueError:
                print("Некорректный год. Введите целое число.")
                
    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}")
    except FileNotFoundError:
        print(f"Файл {xml_file} не найден")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

def main():
    xml_file = "library.xml"
    xsd_file = "library.xsd"
    
    if not Path(xml_file).exists():
        print(f"Файл {xml_file} не найден!")
        return
    if not Path(xsd_file).exists():
        print(f"Файл {xsd_file} не найден!")
        return
    
    if validate_xml(xml_file, xsd_file):
        process_library(xml_file)

if __name__ == "__main__":
    main()