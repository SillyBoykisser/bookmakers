from models.table_model import Table
from services.data_base_services.data_base_manager_service import DataBaseManager

Petr = UserScheme(1, "'Petr'")
Ivan = UserScheme(2, "'Ivan'")
Masha = UserScheme(3, "'Masha'")

user_table = Table("users", UserScheme)

db_manager: DataBaseManager = DataBaseManager("../data_base.db", user_table)

db_manager.create_table()
db_manager.insert(Petr)
db_manager.insert(Ivan)
db_manager.insert(Masha)
db_manager.update("id", 4, "id = 1")
db_manager.update("name", f"'Masha2'", "name = 'Masha'")
print(db_manager.select())
print(db_manager.select("id = 4"))
db_manager.delete("id = 2")
db_manager.drop_table()
