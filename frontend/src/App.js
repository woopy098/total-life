import React,{useEffect, useState} from "react";
import axios from "axios";


function App() {
  const [appointments,setAppointments]= useState([]);
  const [filter, setFilter]= useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/appointments/")
      .then((response) => setAppointments(response.data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="container mx-auto p-5">
    <h1 className="text-xl font-bold mb-3">Appointments</h1>

    <input
      type="text"
      placeholder="Filter by Time..."
      className="p-2 border"
      onChange={(e) => setFilter(e.target.value)}
    />

    <ul className="mt-3">
      {appointments
        .filter((a) => a.appointment_time.includes(filter))
        .map((appointment) => (
          <li key={appointment.id} className="p-3 border mb-2">
              NAME: {appointment.patient_name} {appointment.patient_last_name} APPOINTMENT TIME:{appointment.appointment_time} STATUS:{appointment.status}
          </li>
        ))}
    </ul>
  </div>
  );
}

export default App;
