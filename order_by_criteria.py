from entry import entry
import operator

# Dict de operaciones para llamarlas más tarde 
ops = {
    '=' : operator.eq,
    '<' : operator.lt,
    '>' : operator.gt,
    '>=' : operator.ge,
    '<=' : operator.le,
}


# Recibimos valores y operadores para regresar booleano
def eval_expr(value1, operator, value2):
    return ops[operator](value1, value2)


# Ordenamiento por inserción
def insert_sort_by_priority(my_list):
    for indice in range(1, len(my_list)):
        valor_actual = my_list[indice]
        posicion_actual = indice

        while posicion_actual > 0 and\
            my_list[posicion_actual - 1]['priority']\
            < valor_actual['priority']:
            my_list[posicion_actual] = my_list[posicion_actual - 1]
            posicion_actual -= 1

        my_list[posicion_actual] = valor_actual
    return my_list


# Ordenamiento por inserción
def insert_sort_by_id(my_list):
    for indice in range(1, len(my_list)):
        valor_actual = my_list[indice]
        posicion_actual = indice

        while posicion_actual > 0 and\
            my_list[posicion_actual - 1]['cost']\
            < valor_actual['cost']:
            my_list[posicion_actual] = my_list[posicion_actual - 1]
            posicion_actual -= 1

        my_list[posicion_actual] = valor_actual
    return my_list


# Función principal
def order_by_criteria(criteria=[('weight', '=', 3)], entry=entry):
    if len(criteria) == 1:
        key = criteria[0][0]
        condition = criteria[0][1]
        value = criteria[0][2]
        unprocessed_entry = []
        processed_entry = []
        
        for data in entry:
            if eval_expr(data[key], condition ,value):
                processed_entry.append(data)
            else:
                unprocessed_entry.append(data)

        #processed_entry = insert_sort_by_id(processed_entry)
        processed_entry = insert_sort_by_priority(processed_entry)
        return processed_entry + unprocessed_entry
    
    #Preparado para una segunda tupla, en caso de necesitar más, se debe de crear una función incluso con recursividad
    elif len(criteria) == 2:
        key = criteria[0][0]
        condition = criteria[0][1]
        value = criteria[0][2]
        key1 = criteria[1][0]
        condition1 = criteria[1][1]
        value1 = criteria[1][2]
        pre_processed_entry = []
        processed_entry = []
        pre_processed_entry1 = []
        processed_entry1 = []
        
        for data in entry:
            if eval_expr(data[key], condition ,value):
                processed_entry.append(data)
            else:
                pre_processed_entry.append(data)

        for data in processed_entry:
            if eval_expr(data[key1], condition1, value1):
                processed_entry1.append(data)
            else:
                pre_processed_entry1.append(data)

        processed_entry1 = insert_sort_by_priority(processed_entry1)

        processed_entry = insert_sort_by_priority(processed_entry)
        return processed_entry1 + pre_processed_entry1 + processed_entry + pre_processed_entry


if __name__ == '__main__':
    my_list = order_by_criteria()
    for i in my_list:
        print(i)