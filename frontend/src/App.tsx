// ======================== imports ========================
// ======== react imports ========
import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

// ======== component imports ========
import EventList from "./components/EventList";

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
    ]);
    return (
        <>
            <EventList events={events} />
        </>
    );
}

export default App;
