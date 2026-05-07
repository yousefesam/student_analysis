# اختياري لو مش عايز GUI
from controller.analysis_service import Controller
from service.analysis_service import AnalysisService
from strategies.multithread_strategy import MultiThreadStrategy

controller = Controller()
students = controller.load_data("data/students.csv")

service = AnalysisService(MultiThreadStrategy())
result = service.run(students)

print(result)