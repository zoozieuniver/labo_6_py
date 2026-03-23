n = int(input("Enter size of matrix (NxN): "))

matrix = []

print()
#values for matrix
for i in range (n):
    row = []
    for j in range(n):
        print("Element[",i,"][",j,"]: ")
        number = int(input("Enter value: "))
        row.append(number)
    matrix.append(row)
    
print()
print("Original Matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

#this values for checking sums    
row_sums=[]
col_sums=[]
#cycle for empty values
for i in range(n):
    row_sums.append(0)
    col_sums.append(0)
sum_main=0
sum_sec=0

#cycle for sums
for i in range(n):
    for j in range(n):
        row_sums[i] += matrix[i][j]
        col_sums[j] += matrix[i][j]
        
        if i == j:
            sum_main += matrix[i][j]
        if i + j == n - 1:
            sum_sec += matrix[i][j]
            
target_sum = 0 #our goal
if n >= 3:
    if row_sums[0] == row_sums[1]:
        target_sum = row_sums[0]
    elif row_sums[0] == row_sums[2]:
        target_sum = row_sums[0]
    else:
        target_sum = row_sums[1]
else: #if n*n = 2*2 for example
    target_sum = row_sums[0]
    
#coordinates where "bad number" is
bad_row = -1
bad_col = -1
#error counters for future results
error_count_rows = 0
error_count_cols = 0

for i in range(n):
    if row_sums[i] != target_sum:
        error_count_rows +=1
        if error_count_rows == 0:
            bad_row = i
    
    if col_sums[i] != target_sum:
        error_count_cols +=1
        if error_count_cols:
            bad_col=1
        
#checking our errors

if error_count_rows == 0 and error_count_cols == 0:
    if sum_main == target_sum and sum_sec == target_sum:
        print()
        print("Matrix is perfect!")
    else:
        print()
        print("Matrix is ok, but it seems there's a problem with diagonals")

elif error_count_cols == 1 and error_count_rows == 1:
    #cycle which fixes our bad number
    while row_sums[bad_row] != target_sum:
        
        if row_sums[bad_row] < target_sum:
            matrix[bad_row][bad_col] += 1
            row_sums[bad_row] += 1

        else:
            matrix[bad_row][bad_col] -= 1
            row_sums[bad_row] -= 1

    #calculating diagonals again just in case if actually everything ok
    sum_main = 0
    sum_sec = 0
    
    for i in range(n):
        sum_sec += matrix[i][n-1-i]
        sum_main += matrix[i][i]
        
    print()
    print ("There's an 1 error!")
    
    if sum_main == target_sum and sum_sec == target_sum:
        print("Now yours matrix is fixed!")
    else:
        print("It seems that diagonals not the same value as rows and columns")
        
else:
    print()
    print("There's too much errors to fix, it can't be magic square")
    
print()
print("FINAL RESULTS")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()