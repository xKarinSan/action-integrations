// ======================== imports ========================
// ======== vitest imports ========
import { screen } from "@testing-library/react";
import { describe, it, expect, test } from "vitest";

// ======== component imports ========

// ======================== test cases ========================
// case: No events
describe("No events", () => {
    it("Empty placeholder shows", () => {
        // expect(screen.getAllByTestId("noevents-placeholder").length).toBe(1);
    });
});

// === example test case ===
export function multiply(a, b) {
    return a * b;
}

test("multiplys 1 * 2 to equal 3", () => {
    expect(multiply(1, 2)).toBe(2);
});

describe("multiply function test", () => {
    it("correct multiplication", () => {
        expect(multiply(1, 2)).toBe(2);
    });
    it("in correct multiplication", () => {
        expect(multiply(1, 2)).not.toBe(3);
    });
});
