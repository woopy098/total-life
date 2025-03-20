import React,{useEffect, useState} from "react";
import axios from "axios";


function App() {
  const [appointments,setAppointments]= useState([]);
  const [filteredAppointments, setFilteredAppointments] = useState([]);
  const [startTime,setStartTime] = useState("");
  const [endTime, setEndTime]= useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/appointments/")
    .then((response) => {
      setAppointments(response.data);
      setFilteredAppointments(response.data); 
    })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);


  const filterAppointments = () => {
    if (!startTime || !endTime) {
      setFilteredAppointments(appointments);
      return;
    }

    
    const filtered = appointments.filter((appointment) => {
      const appointmentTime = appointment.appointment_time; 
      return appointmentTime >= startTime && appointmentTime <= endTime;
    });


    setFilteredAppointments(filtered);
  };

  return (
    <div className="container mx-auto p-5">
    <h1 className="text-xl font-bold mb-3">Appointments</h1>

    <div className="flex space-x-4 mb-4">
        <span><strong>Set Appointment Time Range: </strong></span>
        <input
          type="text"
          placeholder="Start Time..."
          className="p-2 border"
          onChange={(e) => setStartTime(e.target.value)}
        />
        <input
          type="text"
          placeholder="End Time..."
          className="p-2 border"
          onChange={(e) => setEndTime(e.target.value)}
        />
        
        <button
          className="p-2 bg-blue-500 text-white rounded"
          onClick={filterAppointments}
        >
          Filter
        </button>
      </div>

 
    <ul className="mt-3">
      {filteredAppointments.length === 0 ? (
          <p>No appointments found in the selected range.</p>
        ) : (
          filteredAppointments.map((appointment) => (
            <li key={appointment.id} className="p-3 border mb-2">
              <div><strong>NAME:</strong> {appointment.patient_name} {appointment.patient_last_name}</div>
              <div><strong>APPOINTMENT TIME:</strong> {appointment.appointment_time}</div>
              <div><strong>STATUS:</strong> {appointment.status}</div>
              <br/>
            </li>
          ))
        )}
    </ul>
    
  </div>
  );
}

export default App;
