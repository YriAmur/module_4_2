def test_function():
    def inner_function():
        print('Я в области видимости функции test_funcyion')

    inner_function()# При вызове функции inner_function() внутри функции inner_function() ничего не происходит
# inner_function() при вызове функции inner_function() внутри функции test_function() - выдаёт ошибку
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()# При вызове функции test_function() внутри функции test_function() - всё работает

