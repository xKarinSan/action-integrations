// ======================== imports ========================
// ======== react imports ========
import { useState } from "react";

// ======== chakraUI imports ========
import { Card, Text } from "@chakra-ui/react";

// ======== type imports ========
import { RegisteredEvent } from "../types/EventType";

// ======================== main app ========================

function EventList({ events }: { events: RegisteredEvent[] }) {
    return (
        <Card border={"10px red"} background={"red"}>
            <Text>Event List</Text>
            {events && events.length > 0 ? (
                <>
                    {events.forEach((event: RegisteredEvent) => {
                        const { id, name } = event;
                        console.info("event", event);
                        // alert(name)
                        return (
                            <Card key={id}>
                                <Text>{name}</Text>
                            </Card>
                        );
                    })}
                </>
            ) : (
                <>
                    <Card id="noevents-placeholder">
                        <Text>No events found</Text>
                    </Card>
                </>
            )}
        </Card>
    );
}

export default EventList;
