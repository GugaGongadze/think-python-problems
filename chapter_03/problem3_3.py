def draw_grid():
    draw_top()
    draw_body()
    draw_body()
    draw_body()
    draw_body()
    draw_middle()
    draw_body()
    draw_body()
    draw_body()
    draw_body()
    draw_bottom()

def draw_top():
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')

def draw_middle():
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')

def draw_bottom():
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')

def draw_body():
    print('| ' + ' ' * 8 + '|' + ' ' * 8 + ' |')

def draw_4x4_grid():
    draw_4x4_top()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_middle()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_middle()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_middle()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_body()
    draw_4x4_bottom()

def draw_4x4_body():
    print('| ' + ' ' * 8 + '|' + ' ' * 8 + ' |' + ' ' * 8 + ' |' + ' ' * 8 + ' |')

def draw_4x4_top():
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')

def draw_4x4_middle():
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')

def draw_4x4_bottom():
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')



