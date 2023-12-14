// ======================== imports ========================
// ======== react imports ========
import { useState } from "react";

// ======== chakraUI imports ========
import { Card, Container, Heading, Image, Text } from "@chakra-ui/react";

// ======== type imports ========
import { RegisteredEvent } from "../types/EventType";

// ======== asset imports ========
import NotFound from "../assets/notfound.gif";

// ======================== main app ========================
function EventList({ events }: { events: RegisteredEvent[] }) {
    //  =========== helper functions ===========
    const formattedDate = (timestampDate: number) => {
        console.log("[formattedDate] timestampDate", timestampDate);
        const date = new Date(timestampDate * 1000);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        const hour = date.getHours();
        const minute = date.getMinutes();
        const second = date.getSeconds();
        return `${day}/${month}/${year} ${hour}:${minute}:${second}`;
    };
    return (
        <Card border={"10px red"} background={"white"} width={["90%", "60%"]}>
            <Heading as={"h2"}>Event List</Heading>
            <>
                {events && events.length > 0 ? (
                    <Container data-testid="eventlist-container">
                        {events.map((event: RegisteredEvent) => {
                            const { id, name, event_date } = event;
                            console.info("event", event);
                            return (
                                <Card
                                    key={id}
                                    background={"#5773ff"}
                                    margin={"10px"}
                                    color={"white"}
                                >
                                    <Heading
                                        as={"h4"}
                                        size={"lg"}
                                        textAlign={"left"}
                                        padding={"5px 5px 5px 20px"}
                                        // paddingLeft={"20px"}
                                    >
                                        Name: {name}
                                    </Heading>
                                    <Text
                                        textAlign={"left"}
                                        padding={"5px 5px 5px 20px"}
                                    >
                                        Date: {formattedDate(event_date)}
                                    </Text>
                                </Card>
                            );
                        })}
                    </Container>
                ) : (
                    <Card
                        id="noevents-placeholder"
                        background={"#f66868"}
                        padding={"20px"}
                        margin={"15px"}
                        data-testid="noevents-placeholder"
                    >
                        <Image
                            src={NotFound}
                            alt={"No events found"}
                            width={"50px"}
                            margin={"10px auto"}
                        />
                        <Heading as={"h6"} size={"sm"} color={"white"}>
                            No events found
                        </Heading>
                    </Card>
                )}
            </>
        </Card>
    );
}

export default EventList;
