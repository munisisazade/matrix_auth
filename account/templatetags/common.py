from django import template

register = template.Library()


@register.filter('count_check')
def check(counter):
    if counter % 4 == 1:
        return False
    else:
        return True

    # even_list = [i for i in range(1,counter+1) if i % 2 != 0]
    # index = even_list.index(counter) + 1
    # if index % 2 == 0:
    #     return True
    # else:
    #     return False
    # if counter >= 3:
    #     if counter == 3:
    #         return True
    #
    #     if check(counter - 2) is True:
    #         return False
    #     else:
    #         return True
