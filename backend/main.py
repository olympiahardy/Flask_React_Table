from flask import request, jsonify
from config import app, db
from models import Interaction

# So this creates a new route, defines a new endpoint for the route and also contains a decorator
# This means that we only want to use the GET method for this particular URL
@app.route("/get_interactions", methods=["GET"])
# Here we can write a function that specifies how we are handling the GET request that is sent to the above route
# This fetches the interactions that we have in the database that calls our Interaction class we define in models.py
# Because this is creating a Python object we can use the lambda function that iterates through the dictionary for each interaction and creates a map object
# Then we convert this into a list and return a json object that the frontend can handle 
def get_interactions():
    interaction = Interaction.query.all()
    json_interactions = list(map(lambda x: x.to_json(), interaction))
    return jsonify({"interactions": json_interactions})

# Now lets do it for creating interactions
@app.route("/create_interactions", methods=["POST"])

# First we define our variables and pass in the json variables we need for the Interaction class we defined in models.py
def create_interactions():
    interaction_name = request.json.get("interactionName")
    tissue_name = request.json.get("tissueName")
    dataset_name = request.json.get("datasetName")
# Then we specify an if statement to check that all the required fields are satisfied and if not we can output a message that details the error
    if not interaction_name or not tissue_name or not dataset_name:
        return (
            jsonify({"message": "You must specify an interaction, type of tissue and your dataset name"}),
            400,
        )
# We can then construct an Interaction object    
    new_interaction = Interaction(interaction_name = interaction_name, tissue_name = tissue_name, dataset_name = dataset_name)
    try:
        db.session.add(new_interaction) # this gets the Interaction object ready to be added to the database session, when this is run the object is in a 'staging area' so its not fully existing yet as such
        db.session.commit() # So to fully write it to the database we need to commit it, so anything that is in the session gets added permanently to our database 
    except Exception as e: # When we are adding to the database errors can occur so we wrap it in a try-except block and if there is an exception it will output a message and the error code 
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Interaction created!"}), 201

@app.route("/update_interaction/<int:interaction_id>", methods = ["PATCH"])
def update_contact(interaction_id):
    interaction = Interaction.query.get(interaction_id)

    if not interaction:
        return jsonify({"message": "Interaction not found!"}), 404
    
    data = request.json
    interaction.interaction_name = data.get("interactionName", interaction.interaction_name)
    interaction.tissue_name = data.get("tissueName", interaction.tissue_name)
    interaction.dataset_name = data.get("datasetName", interaction.dataset_name)

    db.session.commit()

    return jsonify({"message": "Interaction updated!"}), 200

@app.route("/delete_interactions/<int:interaction_id>", methods=["DELETE"])
def delete_contact(interaction_id):
    interaction = Interaction.query.get(interaction_id)

    if not interaction:
        return jsonify({"message": "Interaction not found!"}), 404
    
    db.session.delete(interaction)
    db.session.commit()

    return jsonify({"message": "Interaction deleted!"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # This instanciates the database or what we defined in models.py, so we're spinning up the database if it doesn't exist already

    app.run(debug=True)

