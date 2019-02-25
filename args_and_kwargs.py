# def blog_posts_3(title, *args, **kwargs):
#     print(title)
#     for arg in args:
#         print(arg)
#     for title, post in kwargs.items():
#         print(title, ':', post)
#
# name = 'this is the title'
#
# blog_posts_3(name,
#              '1', '2', '3',
#              blog_1 = 'I am so awesome',
#              blog_2 = 'Cars are cool.',
#              blog_3 = 'Aww look at my cat.')

import matplotlib.pyplot as plt

def graph_operation(x, y):
    print('function that graphs {} and {}'.format(x, y))
    plt.plot(x,y)
    plt.show()

x = [1,2,3]
y = [2,3,1]
graph_me = [x,y]
graph_operation(*graph_me)
