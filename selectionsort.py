
def selectionsort(array,n):
    for index in range(n):
        min = index
        for j in range(index+1,n):
            if (array[j]<array[min]):
                min = j

        (array[index],array[min])= (array[min],array[index])
        
def main():
    arr_size = int(input("Enter size of array:\n"))
    
    arr=[]
    for i in range(arr_size):
        value = int(input("Enter value:\n"))
        arr.append(value)
        
        
    print("Unsorted Array: {} \n".format(arr))
    n = len(arr)
    selectionsort(arr,n)
    print("Sorted Array: {} \n".format(arr))
    
if __name__ == "__main__":
    main()