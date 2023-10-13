CREATE TABLE IF NOT EXISTS properties
(
    id             SERIAL PRIMARY KEY,
    student_id     INTEGER,
    property_type  TEXT,
    property_value TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id)
);

INSERT INTO properties (student_id, property_type, property_value)
VALUES (1, 'Ріст', '180 см'),
       (1, 'Освіта', 'Бакалавр'),
       (2, 'Спортивні досягнення', 'Чемпіон з плавання'),
       (2, 'Спеціалізація', 'Інженер'),
       (3, 'Художній стиль', 'Сучасний'),
       (3, 'Учасник об`єднання', 'Студентська рада'),
       (4, 'Груповий лідер', 'Технічний гурток'),
       (4, 'Волонтерська діяльність', 'Допомога ветеранам'),
       (5, 'Активна участь', 'Волейбольна команда'),
       (5, 'Наукова робота', 'Дослідження в області інформатики'),
       (6, 'Хобі', 'Фотографія'),
       (6, 'Мови', 'Англійська, Французька'),
       (7, 'Любимий предмет', 'Математика'),
       (7, 'Захоплення', 'Робототехніка'),
       (8, 'Комп`ютерні навички', 'Програмування, Веб - дизайн'),
       (8, 'Місце роботи', 'IT-компанія'),
       (9, 'Спорт', 'Баскетбол'),
       (9, 'Публікації', 'Статті в газетах'),
       (10, 'Музичний інструмент', 'Скрипка'),
       (10, 'Інтереси', 'Класична музика, Живопис ');