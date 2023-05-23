# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент 
# по номеру строки и столбца. Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
 
def print_operation_table(operation,num_rows, num_columns):
    for i in range(1,num_rows+1):
        for j in range(1,num_columns+1):
            print(f"{operation(i,j)} ", end = "")
            if operation(i,j) < 10:
                print("  ", end = "") 
            else:
                print(" ", end = "")
 
        print()
        
print_operation_table(lambda x,y: x*y,6,6)