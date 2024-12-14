# Краткая выжимка из теории (подробнее см. [здесь](theory.md)):

Терм - символьное представление какого-то объекта: переменная ($x, y$), константа ($\alpha, \beta$), функция (${f(x, y)}$). 
Арность терма - количество переменных от которых он зависит. Если арность 0, терм представляет константу/переменную. Если 1 или больше, терм представляет функцию.
Алгебра термов - это то как термы взаимодействуют друг с другом.

# Предлагаемая реализация:
Написать класс Term, объект которого будет либо константой/переменной, либо функцией с соответствующим ей выражением.
# Примерная реализация с sympy
## Класс Term:
Свойства:
* арность (arity) - int причем $\ge 0$
* обозначение терма (symbol, можно по-другому назвать) - str
	* если терм 0-арный, он является константой, либо переменной. В случае с **константой** примем **допустимыми только строчные буквы греческого алфавита**. Для обозначения **переменных - любые буквы латинского алфавит**а. В обоих случаях могут использоваться нижние индексы, указываются просто как x_1, k_2 и т.д.
	*  если арность задается $\ge 1$, терм представляет функцию. Обозначается **только латинскими буквами**. После буквы в скобках перечисляются переменные, от которых зависит функция.
* выражение, которое обозначает терм (expression) - str. *Задается опционально.*
	* для n-арного это выражение, которым задается эта функция. Количество переменных в выражении = n.
	* дефолтное значение None
	* Если выражение не задано, значит это либо константа/переменная, либо неизвестная функция, соответственно для построения выражений с ними просто используется их символьное обозначение.

Методы:
* Метод создания объекта с заданиям всех обязательных свойств.
* Метод удаления объекта.
* set_arity(n: int) - (пере-)определение арности
* set_symbol(s: str) - (пере-)определение символа терма
* set_expression(s: str) - (пере-)определение выражения функции
* Метод копирования объекта со всеми его свойствами

## Функции

simplify() - берет выражение expression объекта, если он функция, упрощает его и возвращает результат.

# Задачи
Использовать готовую библиотеку конечно круто, но не соответствует заданию, поэтому нужно переделать некоторые моменты самостоятельно.
* [Первая задача](/tasks/task1.md)
* [Вторая задача](/tasks/task2.md)
* [Третья задача](/tasks/task3.md)
* [Четвертая задача](/tasks/task4.md)
