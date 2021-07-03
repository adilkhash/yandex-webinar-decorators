# Декораторы в Python
- Синтаксический сахар
- Базируются на замыканиях и функциях первого порядка

## Зачем
- Упрощает чтение кода
- Поощряет использование принципа Single Responsibility

## Примеры использования
- [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) для улучшения производительности выполнения "тяжелых" функций
- property, превращает метод в свойство
- login_required в Django для авторизации
- трейсинг вызовов

## План
- Область видимости
- Замыкания, мотивация
- Простейший декоратор, момент выполнения
- Декоратор-таймер
- Декоратор с параметрами и без
- 