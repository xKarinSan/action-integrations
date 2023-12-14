// ======================== imports ========================
// ======== vitest imports ========
import { render,screen } from "@testing-library/react";
import { describe, it, expect, test } from "vitest";
import EventList from "../../components/EventList";

// ======== component imports ========
// import {EventList}
// ======================== test cases ========================
// case: No events
describe("No events", () => {
    it("Empty placeholder shows when empty", () => {
        render(<EventList events={[]} />);
        expect(screen.queryAllByTestId("noevents-placeholder").length).toBe(1);
        expect(screen.queryAllByTestId("eventlist-container").length).toBe(0);
    });
});

// === example test case ===
// export function multiply(a:Number, b:Number) {
//     return a * b;
// }

// test("multiplys 1 * 2 to equal 3", () => {
//     expect(multiply(1, 2)).toBe(2);
// });

// describe("multiply function test", () => {
//     it("correct multiplication", () => {
//         expect(multiply(1, 2)).toBe(2);
//     });
//     it("in correct multiplication", () => {
//         expect(multiply(1, 2)).not.toBe(3);
//     });
// });
