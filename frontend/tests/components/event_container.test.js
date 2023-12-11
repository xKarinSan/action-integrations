// ======================== imports ========================
// ======== vitest imports ========
import {describe, it,expect, test } from "vitest";

// ======== component imports ========

// ======================== test cases ========================




// === example test case ===
export function multiply(a, b) {
    return a * b
  }

  
  test('multiplys 1 * 2 to equal 3', () => {
    expect(multiply(1, 2)).toBe(2)
  })

describe("multiply function test",()=>{
    it("correct multiplication",()=>{
        expect(multiply(1, 2)).toBe(2)
    });
    it("in correct multiplication",()=>{
        expect(multiply(1, 2)).not.toBe(3)
    });
});