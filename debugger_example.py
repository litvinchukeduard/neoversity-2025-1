'''
Нехай в нас є список з продуктів

['Apples', 'Oranges', 'Eggs']

'Eggs'
'''

def element_index(element_list: list[str], desired_element: str) -> int:
    '''
    Fucntion to find the index of the element
    '''
    # return element_list.index(element) + 1
    # for element in element_list:
    #     if element == desired_element:
    #         return element_list.index(element)
    # for i in range(len(element_list)):
    #     if element_list[i] == desired_element:
    #         return i
        
    # return -1

    for i, element in enumerate(element_list):
        if element == desired_element:
            return i + 1
        
    return -1

print(element_index(['Apples', 'Oranges', 'Eggs'], 'Eggs'))
