import { useState } from "react";

export default function App() {
  const [todoList, setTodoList] = useState([
    {
      id: "1",
      title: "Nekruz",
      description: "Hakimzoda",
      complete: false,
    },
    {
      id: "2",
      title: "Ibrohim",
      description: "Davlatov",
      complete: false,
    },
    {
      id: "3",
      title: "Abubakr",
      description: "Rustamov",
      complete: false,
    },
    {
      id: "4",
      title: "Jahonsher",
      description: "Ziyovudinov",
      complete: false,
    },
    {
      id: "5",
      title: "Alisher",
      description: "Roziqov",
      complete: false,
    },
  ]);

  const [addTitle, setAddTitle] = useState("");
  const [addDescription, setAddDescription] = useState("");
  const [addModal, setAddModal] = useState(false);
  const [editModal, setEditModal] = useState(false);
  const [editTitle, setEditTitle] = useState("");
  const [editDescription, setEditDescription] = useState("");
  const [idx, setIdx] = useState(null);

  function handleDelete(id) {
    setTodoList(todoList.filter((todo) => todo.id !== id));
  }

  function add() {
    setTodoList([
      ...todoList,
      {
        title: addTitle,
        description: addDescription,
        id: Date.now(),
        complete: false,
      },
    ]);
    setAddTitle("");
    setAddDescription("");
    setAddModal(false);
  }

  function check(id) {
    setTodoList(
      todoList.map((todo) =>
        todo.id === id ? { ...todo, complete: !todo.complete } : todo
      )
    );
  }

  function handleEdit(todo) {
    setIdx(todo.id);
    setEditTitle(todo.title);
    setEditDescription(todo.description);
    setEditModal(true);
  }

  function edit() {
    setTodoList(
      todoList.map((todo) =>
        todo.id === idx
          ? { ...todo, title: editTitle, description: editDescription }
          : todo
      )
    );
    setEditModal(false);
  }

    const deleteBtn={
    button: { margin: "5px", padding: "5px 10px", cursor: "pointer", backgroundColor:"red", color:"white", border:"none"},
    }
    const addBtn={
    button: { margin: "5px", padding: "5px 10px", cursor: "pointer", backgroundColor:"gray", color:"white", border:"none"},
    }

    const editBtn = {
      button: {
        margin: "5px",
        padding: "5px 10px",
        cursor: "pointer",
        backgroundColor: "green",
        color: "white",
        border: "none",
      },
    };
    
  const styles = {
    container: { padding: "20px", fontFamily: "Arial, sans-serif" },
    button: { margin: "5px", padding: "5px 10px", cursor: "pointer" },
    table: { width: "100%", borderCollapse: "collapse", marginTop: "20px" },
    th: {
      border: "1px solid black",
      padding: "10px",
      backgroundColor: "#f0f0f0",
    },
    td: { border: "1px solid black", padding: "10px", textAlign: "center" },
  };

  return (
    <div style={styles.container}>
      <button style={addBtn.button} onClick={() => setAddModal(true)}>
        Add+
      </button>

      {addModal && (
        <div>
          <input
            value={addTitle}
            onChange={(e) => setAddTitle(e.target.value)}
            type="text"
            placeholder="Title"
          />
          <input
            value={addDescription}
            onChange={(e) => setAddDescription(e.target.value)}
            type="text"
            placeholder="Description"
          />
          <button style={styles.button} onClick={() => setAddModal(false)}>
            Cancel
          </button>
          <button style={styles.button} onClick={add}>
            Save
          </button>
        </div>
      )}

      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>ID</th>
            <th style={styles.th}>Title</th>
            <th style={styles.th}>Description</th>
            <th style={styles.th}>Completed</th>
            <th style={styles.th}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {todoList.map((todo) => (
            <tr
              key={todo.id}
              style={{
                textDecoration: todo.complete ? "line-through" : "none",
              }}
            >
              <td style={styles.td}>{todo.id}</td>
              <td style={styles.td}>{todo.title}</td>
              <td style={styles.td}>{todo.description}</td>
              <td style={styles.td}>
                <input
                  type="checkbox"
                  checked={todo.complete}
                  onChange={() => check(todo.id)}
                />
              </td>
              <td style={styles.td}>
                <button
                  style={deleteBtn.button}
                  onClick={() => handleDelete(todo.id)}
                >
                  Delete
                </button>
                <button style={editBtn.button} onClick={() => handleEdit(todo)}>
                  Edit
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {editModal && (
        <div>
          <input
            type="text"
            value={editTitle}
            onChange={(e) => setEditTitle(e.target.value)}
          />
          <input
            type="text"
            value={editDescription}
            onChange={(e) => setEditDescription(e.target.value)}
          />
          <button style={styles.button} onClick={() => setEditModal(false)}>
            Cancel
          </button>
          <button style={styles.button} onClick={edit}>
            Save
          </button>
        </div>
      )}
    </div>
  );
}
