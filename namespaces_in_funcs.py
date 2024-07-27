def test_function():
    def inner_function():
        print("Я в облости видимости test_function")
    inner_function()


#inner_function() - не получилось, так как эта функция находится в области видимости test_function

test_function()

