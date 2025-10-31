student =['A','B','C','D','E']
marks=[80,70, 90,60,75]
student_houres=[5,4,6,3,4.5]
n=len(marks)
# arithmetic mean
mean=sum(marks)/n
#median
sorted_marks=sorted(marks)
if n%2==1:
    median=sorted_marks[n//2]
else:
    median=(sorted_marks[n//2-1]+sorted_marks[n//2])/2 
    mode= None
    freq={}
    for m in marks:
        freq[m]=freq.get(m,0)+1
    max_freq=max(freq.values())
    if max_freq > 1:
        mode=[k for k,v in freq.items() if v==max_freq] 
    else:
        mode=" No Mode ( all uniqu)"
        # Geometric Mean
    product=1
    for m in marks:
        product *=m 
    geometric_mean=product**(1/n)
    # Harmonic Mean
    reciprocal_sum =0
    for m in marks:
        reciprocal_sum +=1/m
    harmonic_mean=n/reciprocal_sum
     # weighted mean
    weighted_marks=0
    
    for i in range(n):
        weighted_sum +=marks[i]*study_hours[i]
        weigthed_mean =weighted_sum/sum(study_hours)

        # range
        range_value = max(marks)-min(marks)
        # Mean Deviation
        mean_deviation = sum(abs(m - mean) for m in marks) / n
        # Variance
        variance = sum((m - mean) ** 2 for m in marks) / n
        # Standard Deviation
        std_dev = maths .sqrt(variance)
        # quartile deviation
        q1_index = n // 4
        q3_index = 3 * n // 4
        q1 = sorted_marks[q1_index]
        q3 = sorted_marks[q3_index]
        quartile_deviation = (q3 - q1) / 2  
        # Coefficient of Variation
        coeff_variation = (std_dev / mean) * 100
        # standard error
        standard_error = std_dev / math.sqrt(n)
        printf("===TYPES OF AVERAGE==")
        print(f"Arithmetic Mean: {mean :.2f}")
        print(f"Median: {median }")
        print(f"Mode: {mode }")
        print(f"Geometric Mean: {geometric_mean :.2f}")
        print(f"Harmonic Mean: {harmonic_mean :.2f}")
        print(f"Weighted Mean: {weighted_mean :.2f}")
        print(f"Range: {range_value }")
        print(f"Mean Deviation: {mean_deviation :.2f}")
        print(f"Variance: {variance :.2f}")
        print(f"Standard Deviation: {std_dev :.2f}")
        print(f"Quartile Deviation: {quartile_deviation :.2f}")
        print(f"Coefficient of Variation: {coeff_variation :.2f}%")
        print(f"Standard Error: {standard_error :.2f}")
        
    


     



    

    



    