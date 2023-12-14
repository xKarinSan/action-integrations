// ======================== imports ========================
// ======== vitest imports ========
import { render, screen } from "@testing-library/react";
import { describe, it, expect, beforeEach, afterEach } from "vitest";

// ======== component imports ========
import EventList from "../../components/EventList";

// ======== type imports ========
import { RegisteredEvent } from "../../types/EventType";

// ======================== helper functions ========================
const renderEventContainer = (events: RegisteredEvent[]) => {
    render(<EventList events={events} />);
};

// ======================== setup & teardown ========================
// ======== setup ========
beforeEach(() => {
    console.log("OK");
});

// ======== teardown ======
afterEach(() => {
    console.log("DONE");
});
// ======================== test cases ========================
// case: No events

describe("No events", () => {
    beforeEach(() => {
        renderEventContainer([]);
    });
    // render(<EventList events={[]} />);
    it("Empty placeholder shows when empty", () => {
        expect(screen.queryAllByTestId("noevents-placeholder").length).toBe(1);
    });
    it("Event container should not render when there are no events", () => {
        expect(screen.queryAllByTestId("eventlist-container").length).toBe(0);
    });
});

// case: Have events
describe("Have events", () => {
    beforeEach(() => {
        renderEventContainer([
            {
                id: "1",
                name: "idk",
                event_date: Math.floor(new Date().getTime() / 1000),
            },
        ]);
    });
    it("Empty placeholder should not show when have events", () => {
        expect(screen.queryAllByTestId("noevents-placeholder").length).toBe(0);
    });
    it("Container should show when have events", () => {
        expect(screen.queryAllByTestId("eventlist-container").length).toBe(1);
    });
});
