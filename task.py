import uuid
import time

class Task():
  """Representation of a task
  
  Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
  def __init__(self, name, priority = 1, dueDate = None ):
      self.name = name
      self.priority = priority
      self.unique_id = uuid.uuid4()
      self.created = time.time()
      self.due_date= dueDate
      self.completed = None 

  def __str__(self):
     name = self.name
     priority = self.priority
     unique_id = self.unique_id
     created = self.created
     due_date = self.due_date
     completed = self.completed
     string = f"{name}\n {priority}\n {unique_id}\n"
     return string