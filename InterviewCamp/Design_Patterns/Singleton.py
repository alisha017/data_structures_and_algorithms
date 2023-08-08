# class School:
#     def __init__(self):
#         self.__name = ""
#
#     def class_activity(self):
#         db = Connection()
#         db.connect()
#         db.query("abc")
#
#     def inter_class_activity(self):
#         db = Connection()
#         db.connect()
#         db.query("xyz")
#
#     def build_connection(self, conn:Connection):
#
# # builder
# class Main_School_Runner:
#     def __init__(self):
#         self.my_school = School()
#
#     def activities(self):
#         class_Activity = self.my_school.class_activity()
#         inter = self.my_school.inter_class_activity()
#
#
# class Principal:
#     def __init__(self, name: str, school: School):
#         self.__name = name
#         self._school = school
#         self.__id = 9
#
#
# class Teacher:
#     def __init__(self, name):
#         self.__name = name
#
#
# class School_Activity:
#     def __init__(self, name):
#         self.__name = name
#
#
# # database connection lib
# class Connection:
#     _instances = {}
#
#     def __call__(self, *args, **kwargs):
#         self.__db = Activity_Db
#         if self not in self._instances:
#             instance = super().__call__(*args, **kwargs)
#             self._instances[self] = instance
#         return self._instances[self]
#
#     def __init__(self, usename, password, port):
#         self.
#
#     def connect(self):
#         pass
#
#     def query(self, query_key):
#         return self.__db.get_activity(query_key)
#
#
# # mock database
# class Activity_Db:
#     def __init__(self):
#         self.activity = {
#             "abc": "teacher",
#             "xyz": "principal"
#         }
#
#     def get_activity(self, activity):
#         return self.activity[activity]
