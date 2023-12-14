// ======================== imports ========================
// ======== react imports ========
import { useState } from "react";

// ======== chakraUI imports ========
import {
    Card,
    Heading,
    Input,
    FormLabel,
    Button,
    FormControl,
} from "@chakra-ui/react";

// ======== type imports ========
import { RegisteredEvent } from "../types/EventType";

// ======== asset imports ========
import NotFound from "../assets/notfound.gif";

// ======================== main app ========================
function CalendarForm({
    submitForm,
}: {
    submitForm: (event: RegisteredEvent) => void;
}) {
    //  =========== helper functions ===========
    const formattedFormDate = (inputDate: Date) => {
        const year = inputDate.getFullYear();
        const month = inputDate.getMonth() + 1;
        const day = inputDate.getDate();
        const hour = inputDate.getHours();
        const minute = inputDate.getMinutes();
        return `${year}-${month}-${day}T${hour >= 10 ? hour : "0" + hour}:${
            minute >= 10 ? minute : "0" + minute
        }`;
    };

    const submitEvent = async () => {
        // submits the event
        const dateTimestamp = Math.floor(
            new Date(chosenDateTime).getTime() / 1000
        );

        const newEvent: RegisteredEvent = {
            id: "",
            name: eventName,
            event_date: dateTimestamp,
        };
        await submitForm(newEvent);
    };

    const cancelSubmission = () => {
        // this resets to default
        console.warn("back to default");
    };
    //  =========== states ===========
    const [chosenDateTime, setChosenDateTime] = useState<string>(
        formattedFormDate(new Date())
    );
    const [eventName, setEventName] = useState<string>("");

    return (
        <Card
            border={"10px red"}
            background={"white"}
            width={["90%", "60%"]}
            margin={"10px auto"}
            padding={"10px"}
        >
            <Heading as={"h3"} fontWeight={"normal"}>
                Add Event
            </Heading>

            <FormControl>
                <FormLabel>Event Date:</FormLabel>
                <Input
                    type={"datetime-local"}
                    value={chosenDateTime}
                    onChange={(e) => setChosenDateTime(e.target.value)}
                />
                <br />
                <FormLabel>Event Name:</FormLabel>
                <Input
                    type={"text"}
                    value={eventName}
                    onChange={(e) => {
                        setEventName(e.target.value);
                    }}
                />
            </FormControl>
            <Button
                margin={"10px"}
                onClick={submitEvent}
                background={"#5773ff"}
                color={"white"}
            >
                Submit
            </Button>
            <Button
                margin={"10px"}
                onClick={cancelSubmission}
                background={"#f66868"}
                color={"white"}
            >
                Cancel
            </Button>
            {/* </FormControl> */}
        </Card>
    );
}

export default CalendarForm;
