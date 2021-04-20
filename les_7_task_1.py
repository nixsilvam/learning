def list_function(f_t_d):
    def the_wrapper(x):
        f_t_d(x)
        return x.split()
    return the_wrapper


@list_function
def return_string(x):
    return x


inp = input('Enter a string: ')
print(return_string(inp))
