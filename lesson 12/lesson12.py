import logging
from time import asctime

# DEBUG -  найнижчий рівень налаштування. Найчастіше використовується розробниками бібліотек
# INFO - рівень інформування. Він створений для надання повідомленнь про коретну роботу об'єктів
# WARNING - рівень застережень. Повідомлює про можливу неправильну роботу
# ERROR - рівень помилок, якщо сповіщають про неправильну роботу якогось шматочка коду
# CRITICAL - рівень критичних помилок, повідомлення про серйозну помилку

logging.basicConfig(level=logging.DEBUG,filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s:%(message)s")
# filename - рядок зі шляхом до файлу , у який записується інформація
# filemode - "а" - інформація буде дописуватися. "w" буде повністю перезаписуватися
# format - форматування тексту, як буде зберігатися інформація
logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")