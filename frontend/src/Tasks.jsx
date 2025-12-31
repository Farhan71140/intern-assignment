import { useState, useEffect } from "react";
import API from "./api";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const fetchTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data);
  };

  const createTask = async () => {
    await API.post("/tasks", { title, description });
    setTitle("");
    setDescription("");
    fetchTasks();
  };

  const updateTask = async (id) => {
    await API.put(`/tasks/${id}`, { title, description });
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await API.delete(`/tasks/${id}`);
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <h2>Tasks Dashboard</h2>
      <input placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
      <button onClick={createTask}>Add Task</button>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <b>{task.title}</b> - {task.description}
            <button onClick={() => updateTask(task.id)}>Update</button>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}