if __name__ == '__main__':
    n = int(input())  
    arr = list(map(int, input().split())) # This checks the input then splits it then makes it into a list
    if 2<= n <=10 and all(-100 <= score <= 100 for score in arr): # conditions based in the instructions, score will also be a variable name
        uniqueScores = list(set(arr)) # we will remove duplicates using set then make them into a list again
        uniqueScores.sort(reverse = True) # descending order since reverse, sorting them highest to lowest
        if len(uniqueScores) > 1: #checking if there are more uniquq scores
            print(uniqueScores[1]) # [1] because runner up, and basically second highest
        
        else:
            print("No Score")
