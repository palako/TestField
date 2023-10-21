// Unit tests for Calculator class

const Calculator = require('./calculator');

const calculator = new Calculator();

// Test addition
const result1 = calculator.add(2, 3);
console.log('Addition:', result1);

// Test subtraction
const result2 = calculator.subtract(5, 2);
console.log('Subtraction:', result2);
