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
    useToast,
} from "@chakra-ui/react";

// ======== type imports ========
import { RegisteredEvent } from "../types/EventType";

// ======== asset imports ========

// ======================== main app ========================
function CalendarForm({
    submitForm,
    refreshFunction,
}: {
    submitForm: (event: RegisteredEvent) => Promise<any>;
    refreshFunction: () => Promise<void>;
}) {
    const toast = useToast({
        position: "top",
        duration: 3000,
        isClosable: true,
    });

    //  =========== helper functions ===========
    const resetToDefault = () => {
        setChosenDateTime(formattedFormDate(new Date()));
        setEventName("");
    };
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
        await submitForm(newEvent)
            .then(async (res: any) => {
                console.info("res", res);
                if (res && res.data) {
                    toast({
                        title: res.data.message,
                        status: "success",
                    });
                    resetToDefault();
                } else {
                    toast({
                        title: "Something went wrong, try again later",
                        status: "error",
                    });
                }
            })
            .then(async () => {
                await refreshFunction();
            })
            .catch((err) => {
                console.warn("err", err);
                toast({
                    title: "Something went wrong, try again later",
                    status: "error",
                });
            });
    };

    const cancelSubmission = () => {
        console.warn("back to default");
        resetToDefault();
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
