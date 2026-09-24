import pandas as pd
data = {
    "Roll_No": [
        "2420030053", "2420030054", "2420030055", "2420030056", "2420030057",
        "2420030058", "2420030059", "2420030060", "2420030061", "2420030062"
    ],
    "Name": [
        "Yasaswi Kakunuri", "Ali", "Rashed", "Hamza", "Toshana",
        "Sahithi", "Sushmitha", "Nithya", "Dharini", "Fatima"
    ],
    "Age": [19, 20, 19, 20, 21, 19, 19, 19, 20, 19],
    "Section": ["5", "6", "7", "5", "6", "7", "5", "6", "6", "5"],
    "Data_Science": [85, 78, 92, 74, 88, 90, 67, 80, 76, 95],
    "QC": [80, 75, 89, 70, 85, 88, 65, 78, 72, 91],
    "TOC": [82, 77, 90, 73, 86, 89, 66, 79, 74, 93] 
}
df = pd.DataFrame(data)
print(df)
df.to_csv("students.csv")
print("CSV file 'students.csv' is created")applying_operations_on_
