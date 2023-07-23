print("==Task 1==")
def findAndPrint(messages):
    for x in messages:
        if "18 years" in messages[x]:
            print(x)
        if "college student" in messages[x]:
            print(x)
        if "legal age" in messages[x]:
            print(x)
        if "vote" in messages[x]:
            print(x)


findAndPrint({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
});

print("==Task 2==")
def calculate_sum_of_bonus(data):
    USD_TO_TWD_EXCHANGE_RATE = 30
    MAX_TOTAL_BONUS_TWD = 10000

    def calculate_bonus(salary, performance, role):
        bonus = 0

        if role == "Engineer":
            if performance == "above average":
                bonus = salary * 0.07
            elif performance == "average":
                bonus = salary * 0.06
            else:
                bonus = salary * 0.05
        elif role == "CEO":
            if performance == "above average":
                bonus = salary * 0.09 
            elif performance == "average":
                bonus = salary * 0.08 
            else:
                bonus = salary * 0.07 
        elif role == "Sales":
            if performance == "above average":
                bonus = salary * 0.05 
            elif performance == "average":
                bonus = salary * 0.04 
            else:
                bonus = salary * 0.03 

        return bonus

    total_bonus_twd = 0

    for employee in data["employees"]:
        salary = employee["salary"]
        if isinstance(salary, str):
            if "USD" in salary:
                salary = int(salary.replace("USD", ""))
                salary = salary * 30
            elif "," in salary:
                salary = int(salary.replace(",", ""))
        bonus_twd = calculate_bonus(salary, employee["performance"], employee["role"])
        total_bonus_twd += bonus_twd

    print("Total bonus in TWD:", total_bonus_twd)

calculate_sum_of_bonus({
    "employees": [
        {
            "name":"John",
            "salary":"1000USD",
            "performance":"above average",
            "role":"Engineer"
        },
        {
            "name":"Bob",
            "salary":60000,
            "performance":"average",
            "role":"CEO"
        },
        {
            "name":"Jenny",
            "salary":"50,000",
            "performance":"below average",
            "role":"Sales"
        }
    ]
})

print("==Task 3==")
def func(*data):
    # 第二字元的出现次數
    second_char_counts = {}
    # 紀錄名字第二個字出现次數為1的名字
    names_with_second_char_once = []

    
    for string in data:
      
        if len(string) >= 2:
            second_char = string[1]
            
            second_char_counts[second_char] = second_char_counts.get(second_char, 0) + 1

    
    #for char, count in second_char_counts.items():
        #print(f"第二個字元 '{char}' 出現次數: {count}")

    
    for name in data:
        if len(name) > 1 and second_char_counts.get(name[1], 0) == 1:
            names_with_second_char_once.append(name)

    
    if names_with_second_char_once:
        #print("名字第二個字出現次數為1的名字:")
        for name in names_with_second_char_once:
            print(name)
    else:
        print("沒有")

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

print("==Task 4==")

def get_number(index):
    if index == 0:  # 如果索引號為0
        return 0
    elif index % 2 == 0:  # 如果索引號是偶數
        return (3 * index) // 2
    else:  # 如果索引號是奇數
        return (3 * (index - 1) // 2) + 4


print(get_number(1))   # 輸出：4
print(get_number(5))   # 輸出：10
print(get_number(10))  # 輸出：15

get_number(1) # print 4
get_number(5) # print 10 
get_number(10) # print 15