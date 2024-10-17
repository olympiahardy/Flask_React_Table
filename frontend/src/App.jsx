import { useState, useEffect } from "react";
import "./App.css";
import InteractionList from "./InteractionList";
import InteractionForm from "./InteractionForm";

function App() {
  const [interactions, setInteractions] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentInteraction, setCurrentInteraction] = useState({});

  useEffect(() => {
    fetchInteractions();
  }, []);

  const fetchInteractions = async () => {
    const response = await fetch("http://127.0.0.1:5000/get_interactions");
    const data = await response.json();
    setInteractions(data.interactions);
    console.log(data.interactions);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentInteraction({});
  };

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
  };

  const openEditModal = (interactions) => {
    if (isModalOpen) return;
    setCurrentInteraction(interactions);
    setIsModalOpen(true);
  };

  const onUpdate = () => {
    closeModal();
    fetchInteractions();
  };

  return (
    <>
      <InteractionList
        interactions={interactions}
        updateInteraction={openEditModal}
        updateCallback={onUpdate}
      />
      <button onClick={openCreateModal}> Upload New Interaction</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <InteractionForm
              existingInteraction={currentInteraction}
              updateCallback={onUpdate}
            />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
