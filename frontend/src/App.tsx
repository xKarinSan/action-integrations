// ======================== imports ========================
// ======== react imports ========
import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

// ======== component imports ========
import EventList from "./components/EventList";
import CalendarForm from "./components/CalendarForm";
// ======== type imports ========
import { RegisteredEvent } from "./types/EventType";

// ======================== main app ========================
function App() {
    const [events, setEvents] = useState<RegisteredEvent[]>([]);
    const getAllEvents = async () => {
        const response = await axios.get(
            import.meta.env.VITE_APP_BACKEND + "/api/event"
        );
        // console.info("response", response);
        setEvents(response.data.events);
    };
    useEffect(() => {
        getAllEvents();
    }, []);

    const submitEvent = async (submitEvent: RegisteredEvent) => {
        // console.info("submitEvent", submitEvent);
        return axios.post(
            import.meta.env.VITE_APP_BACKEND + "/api/event",
            submitEvent
        );
    };
    return (
        <>
            <CalendarForm
                submitForm={submitEvent}
                refreshFunction={getAllEvents}
            />
            <EventList events={events} />
        </>
    );
}

export default App;
