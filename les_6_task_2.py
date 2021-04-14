import time


def countdown(function_to_decorate):
    def the_wrapper_around_the_original_function():
        time.sleep(3)
        function_to_decorate()
    return the_wrapper_around_the_original_function


@countdown
def nowtime():
    print(time.strftime('%H:%M'))


nowtime()
