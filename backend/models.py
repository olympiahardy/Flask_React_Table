# This will contain all of the database models

# Imports the database instance we defined in the config.py file and gives us access to the database
from config import db

# Now we make a class that inherits from the database model but using python code
class Interaction(db.Model):
    # This is setting up entries in the database so we have row id that we set as the primary key meaning it must be a unique integer value
    row_id = db.Column(db.Integer, primary_key = True)
    # This is a field that we set nullable to false meaning it must be entered
    interaction_name = db.Column(db.String(80), unique=False, nullable=False)
    tissue_name = db.Column(db.String(80), unique=False, nullable=False)
    dataset_name = db.Column(db.String(80), unique=False, nullable=False)

    # This function that takes all the fields and converts it into a python dictionary to a json to pass to the API back and forth 
    # Note here that we assign our JSON variables in camelcase which means we have a lowercase variable name followed by a capitalised second word
    # That is the convention for JSON as opposed to snakecase which is convention in Python e.g. python = row_id JSON = rowID
    def to_json(self):
        return {
            "rowId":self.row_id,
            "interactionName":self.interaction_name,
            "tissueName":self.tissue_name,
            "datasetName":self.dataset_name,
        }
