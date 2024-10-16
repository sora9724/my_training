def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() # Функция работает

inner_function() # Функция не может быть вызванна
test_function() # Функция работает
