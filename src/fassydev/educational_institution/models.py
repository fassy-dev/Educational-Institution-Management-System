from .managers import load_data, save_data
from .utils import validate_id, normalize_input


class EducationalInstitution:
    def __init__(self, name, address, inst_type, license_number, email="yakrutoi228@ya.ru"):
        self.name = name
        self.address = address
        self.type = inst_type
        self.license_number = license_number
        self.email = email

        data = load_data()
        self.students = data["students"]
        self.teachers = data["teachers"]

    def update_license(self, new_license):
        self.license_number = new_license

    def __str__(self):
        return (f"Учреждение: {self.name} | Адрес: {self.address} | Email: {self.email}\n"
                f"Всего студентов: {len(self.students)} | Всего учителей: {len(self.teachers)}")


class TeachersManagement(EducationalInstitution):
    @property
    def teacher_count(self):
        return len(self.teachers)

    def hire_teacher(self, teacher_id, full_name):
        tid = normalize_input(teacher_id)
        name = normalize_input(full_name)

        if not validate_id(tid):
            raise ValueError("ID учителя не может быть пустым")
        if tid in self.teachers:
            raise ValueError(f"Учитель с ID {tid} уже существует")

        self.teachers[tid] = name
        save_data(self.students, self.teachers)
        return True

    def fire_teacher(self, teacher_id):
        tid = normalize_input(teacher_id)
        if tid in self.teachers:
            del self.teachers[tid]
            save_data(self.students, self.teachers)
            return True
        return False


class StudentsManagement(TeachersManagement):
    @property
    def student_count(self):
        return len(self.students)

    def enroll_student(self, student_id, full_name):
        sid = normalize_input(student_id)
        name = normalize_input(full_name)

        if not validate_id(sid):
            raise ValueError("ID студента не может быть пустым")
        if sid in self.students:
            raise ValueError(f"Студент с ID {sid} уже существует")

        self.students[sid] = name
        save_data(self.students, self.teachers)
        return True

    def expel_student(self, student_id):
        sid = normalize_input(student_id)
        if sid in self.students:
            del self.students[sid]
            save_data(self.students, self.teachers)
            return True
        return False
