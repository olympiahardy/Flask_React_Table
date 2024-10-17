import { useState } from "react";

const InteractionForm = ({ existingInteraction = {}, updateCallback }) => {
  const [interactionName, setInteractionName] = useState(
    existingInteraction.interactionName || ""
  );
  const [tissueName, setTissueName] = useState(
    existingInteraction.tissueName || ""
  );
  const [datasetName, setDatasetName] = useState(
    existingInteraction.datasetName || ""
  );

  const updating = Object.entries(existingInteraction).length !== 0;

  const onSubmit = async (e) => {
    e.preventDefault();

    const data = {
      interactionName,
      tissueName,
      datasetName,
    };

    const url =
      "http://127.0.0.1:5000/" +
      (updating
        ? `update_interaction/${existingInteraction.rowId}`
        : "create_interactions");
    const options = {
      method: updating ? "PATCH" : "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };

    const response = await fetch(url, options);

    if (response.status !== 201 && response.status !== 200) {
      const data = await response.json;
      alert(data.message);
    } else {
      updateCallback();
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="interactionName">Interaction Name:</label>
        <input
          type="text"
          id="interactionName"
          value={interactionName}
          onChange={(e) => setInteractionName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="tissueName">Tissue Type:</label>
        <input
          type="text"
          id="tissueName"
          value={tissueName}
          onChange={(e) => setTissueName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="datasetName">Dataset Name:</label>
        <input
          type="text"
          id="datasetName"
          value={datasetName}
          onChange={(e) => setDatasetName(e.target.value)}
        />
      </div>
      <button type="submit"> {updating ? "Update" : "Create"} </button>
    </form>
  );
};

export default InteractionForm;
