from grading import avgrage_score

def build_report(student_name, score, status):
    report= f"""Student Performance Report
--------------------------
Student Name: {student_name}
Score: {score}
Status: {status}
"""
    return report

def score_report(score_array):
    report= f"""Score Report 
--------------------------
Average Score: {avgrage_score(score_array)}
Highest Score: {max(score_array)}
Lowest Score:" {min(score_array)}
"""
    return report

def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ','_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    return filename
