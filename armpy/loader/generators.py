from inspect import signature

def generate_function(
        func_name,
        trans_name,
        arguments=None,
    ):
    builtin_func = globals()['__builtins__'][func_name]
    
    if arguments is None:
        return builtin_func

    try:
        origin_args_str = str(signature(builtin_func)).strip('()')
    except:
        return builtin_func
    
    new_args = origin_args_str
    for old, new in arguments.items():
        new_args = new_args.replace(old, new)
    
    
    new_args.replace('\n', '\\n')
    origin_args = origin_args_str.split(',')
    
    call_args_list = []
    for arg in origin_args:
        tmp = arg.strip().split('=')
        match tmp:
            case ['*args'] | ['**kwargs']:
                call_args_list.append(tmp[0])
            case [arg_name, str()] | [str(arg_name)]:
                call_args_list.append(f"{arg_name}={arguments.get(arg_name, arg_name)}")
    call_args = ', '.join(call_args_list)
    
    new_function_str = (
        f"def {trans_name}({new_args}):\n"
        f"    return {builtin_func.__name__}({call_args})\n"
    )
    
    code = compile(new_function_str, __name__, 'exec')
    exec(code)
    return locals()[trans_name]
