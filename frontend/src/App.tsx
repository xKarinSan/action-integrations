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
    const [events, setEvents] = useState<RegisteredEvent[]>([
        // {
        //     id: "1",
        //     name: "idk",
        //     event_date: Math.floor(new Date().getTime() / 1000),
        // },
        // {
        //     id: "2",
        //     name: "testt",
        //     event_date: Math.floor(new Date().getTime() / 1000),
        // },
        // {
        //     id: "3",
        //     name: "1234",
        //     event_date: Math.floor(new Date().getTime() / 1000),
        // },
    ]);
    useEffect(() => {
        setEvents([]);
    }, []);

    const submitEvent = async (submitEvent: RegisteredEvent) => {
        // console.info("submitEvent", submitEvent);
        // console.info("env variable",import.meta.env.VITE_APP_BACKEND);
        await axios.post("http://localhost:8000/api/event", submitEvent);
    };
    return (
        <>
            <EventList events={events} />
            <CalendarForm submitForm={submitEvent} />
        </>
    );
}

export default App;
