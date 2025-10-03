from student import Student
from performance import RealPerformance, DesiredPerformance
from student_data import StudentData
from data_saver import JsonSaver, XmlSaver, CsvSaver

if __name__ == "__main__":
	student = Student("Sirenko Oleksandr Serhiyovich", "PDM51", "2000-01-01")
	subjects = ["Math", "Physics", "Programming"]
	real_scores = [80, 85, 90]
	desired_scores = [95, 95, 100]
	desired_average = 98

	real_perf = RealPerformance(subjects, real_scores)
	desired_perf = DesiredPerformance(subjects, desired_scores, desired_average)

	student_data = StudentData(student, real_perf, desired_perf)
	data_dict = student_data.get_data_dict()

	full_name_parts = student.full_name.split()[0]
	group = student.group_number
	work_number = "SR2" 
	base_filename = f"{full_name_parts}_{group}_{work_number}"

	json_saver = JsonSaver()
	json_saver.save(data_dict, f"{base_filename}.json")

	xml_saver = XmlSaver()
	xml_saver.save(data_dict, f"{base_filename}.xml")

	csv_saver = CsvSaver()
	csv_saver.save(data_dict, f"{base_filename}.csv")