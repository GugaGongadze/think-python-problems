def eval_loop():
    last_eval = ''
    while True:
        user_input = input('What expression would you like to evaluate?\n')
        if user_input == 'done':
            return last_eval
        else:
            print(eval(user_input))
            last_eval = eval(user_input)

