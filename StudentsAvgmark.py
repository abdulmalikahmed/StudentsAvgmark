# انشاء كيو يقوم بترتيب المصفوفة تصاعديا
def sortQueuedes(input):
    tmpQueuedes = []
    while (len(input) > 0):
     
        # pop out للعنصر الاول
        tmp = input[-1]
        input.pop()
 
        # في حال ان العنصر المؤقت في الكيو غير فارغ والعنصر التالي اصغر من العنصر المؤقت
        
        while (len(tmpQueuedes) > 0 and tmpQueuedes[-1] <tmp) :
         
            # pop من العنصر المؤقت في الكيو 
            # اضافتة الى العناصر المدخلة في الكيو
            input.append(tmpQueuedes[-1])
            tmpQueuedes.pop()
         
        # اضافة العنصر المؤقت الى الكيو المؤقت
        tmpQueuedes.append(tmp)
     
    return tmpQueuedes
 
def sortArrayUsingQueuedes(arr, n):
 
    # اضافة عناصر المصفوفة الى الكيو
    input = []
    i = 0
    while ( i < n ):
        input.append(arr[i])
        i = i + 1
         
    # ترتيب عناصر الكيو المؤقت
    tmpQueuedes = sortQueuedes(input)
    i = 0
     
    # اضافة العناصر من الكيو الى المصفوفة تنازليا
    while (i < n):
        arr[i] = tmpQueuedes[-1]
        tmpQueuedes.pop()
        i = i + 1
         
    return arr
def sortQueueasc(input):
    tmpQueue = []
    while (len(input) > 0):
     
        # pop out للعنصر الاول
        tmp = input[-1]
        input.pop()
 
        # في حال ان العنصر المؤقت في الكيو غير فارغ والعنصر التالي اصغر من العنصر المؤقت
        
        while (len(tmpQueue) > 0 and tmpQueue[-1] >tmp) :
         
            # pop من العنصر المؤقت في الستاك 
            # اضافتة الى العناصر المدخلة في الستاك
            input.append(tmpQueue[-1])
            tmpQueue.pop()
         
        # اضافة العنصر المؤقت الى الكيو المؤقت
        tmpQueue.append(tmp)
     
    return tmpQueue
 
def sortArrayUsingQueueasc(arr, n):
 
    # اضافة عناصر المصفوفة الى الستاك
    input = []
    i = 0
    while ( i < n ):
        input.append(arr[i])
        i = i + 1
         
    # ترتيب عناصر الكيو المؤقت
    tmpQueue = sortQueueasc(input)
    i = 0
     
    # اضافة العناصر من الستاك الى المصفوفة تصاعديا
    while (i < n):
        arr[i] = tmpQueue[-1]
        tmpQueue.pop()
        i = i + 1
         
    return arr

 # انشاء ستاك مؤقت
def sortStack(input):
    tmpStack = []
    while (len(input) > 0):
     
        # pop out للعنصر الاول
        tmp = input[-1]
        input.pop()
 
        # في حال ان العنصر المؤقت في الستاك غير فارغ والعنصر التالي اصغر من العنصر المؤقت
        
        while (len(tmpStack) > 0 and tmpStack[-1] < tmp):
         
            # pop من العنصر المؤقت في الستاك 
            # اضافتة الى العناصر المدخلة في الستاك
            input.append(tmpStack[-1])
            tmpStack.pop()
         
        # اضافة العنصر المؤقت الى الستاك المؤقت
        tmpStack.append(tmp)
     
    return tmpStack
 
def sortArrayUsingStacks(arr, n):
 
    # اضافة عناصر المصفوفة الى الستاك
    input = []
    i = 0
    while ( i < n ):
        input.append(arr[i])
        i = i + 1
         
    # ترتيب عناصر الستاك المؤقت
    tmpStack = sortStack(input)
    i = 0
     
    # اضافة العناصر من الستاك الى المصفوفة تنازليا
    while (i < n):
        arr[i] = tmpStack[-1]
        tmpStack.pop()
        i = i + 1
         
    return arr
# انشاء مصفوفة وتعريف متغير لقياس طول المصفوفة
savg = [ ]
#يمكن اختيار عدد الطلاب او طول المصفوفة بادخال الرقم المرغوب به
n = int(input("Enter number of elements : "))
# انشاء حلقة تكرار تقوم بتعريف متغير يسمح للمستخدم بادخال عناصر المصفوفة
while(len(savg)!=n):
 ele = [int(input("enter the student mark : "))]
 savg.append(ele)
 # استدعاء الستاك وترتيب عناصر المصفوفة
savg = sortArrayUsingStacks(savg, n)
print("the average marks sort by Stack : ",savg)
savg = sortArrayUsingQueueasc(savg, n)
print("the average marks sort by Queueasc : ",savg)
savg = sortArrayUsingQueuedes(savg,n)
print("the average marks sort by Queuedes : ",savg)