def finding_dublicates_indices():
    given_array = [1, 2, 5, 6, 47, 8, 9, 4, 4, 47,5,5]
    result = []

    for i in range(len(given_array)):
        for j in range(i + 1, len(given_array)):
            if given_array[i] == given_array[j]:
                result.append((given_array[i], i, j))

    for value, index1, index2 in result:
      print(f"Value {value} found at postions {index1} and {index2} .")
        #saveresult={}
        #saveresult.append(value, )


def repeated_numbers(array):
    result=[]
    result1=[]
    for n,i in enumerate(array):
        if i in array[:n]:
            result.append(i)
    print(result)

    #\\different way of re-writing the code to find duplicates, not using enumerate
    for i in range(len(array)):
        for j in range(i):
            if array[i] == array[j]:
                result1.append(array[i])
        
    return result
    
if __name__=="__main__":

    list1= [1,2,3,565,4,6,8,565,8,1,4]
    x=repeated_numbers(list1)
    

    print("The maximum value within the provided list is.:",max(list1),
        "\nThe minimum value within the provided list is.:",min(list1),
        "\nThe total number of elements in the provided list is.:",len(list1),
        "\nThe avg number of the given list is:",sum(list1) / (len(list1)),
        "\nThe recurring or duplicated elements within the provided list are.:", x)