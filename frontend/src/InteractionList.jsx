import React from "react";

const InteractionList = ({
  interactions,
  updateInteraction,
  updateCallback,
}) => {
  const onDelete = async (rowId) => {
    try {
      const options = {
        method: "DELETE",
      };

      const response = await fetch(
        `http://127.0.0.1:5000/delete_interactions/${rowId}`,
        options
      );
      if (response.status == 200) {
        updateCallback();
      } else {
        console.error("Failed to delete");
      }
    } catch (error) {
      alert(error);
    }
  };
  return (
    <div>
      <h2>Interactions</h2>
      <table>
        <thead>
          <tr>
            <th>Interaction Name</th>
            <th>Tissue Type</th>
            <th>Dataset Name</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {interactions.map((interaction) => (
            <tr key={interaction.rowId}>
              <td>{interaction.interactionName}</td>
              <td>{interaction.tissueName}</td>
              <td>{interaction.datasetName}</td>
              <td>
                <button onClick={() => updateInteraction(interaction)}>
                  Update
                </button>
                <button onClick={() => onDelete(interaction.rowId)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default InteractionList;
