
create_tasks = """ 
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    ) 
 """

# CRUD CREATE - READ - UPDATE - DELETE 

# CREATE
insert_task = "INSERT INTO tasks (task) VALUES (?)"

# READ
select_tasks = 'SELECT id, task FROM tasks'

# UPDATE 
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

# DELETE 
delete_task = 'DELETE FROM tasks WHERE id = ?'