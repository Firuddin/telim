export const FirstFactorial = (str) => {
  let Factorial = 2;
  for (let i = 2; i <= str; i++) {
    Factorial *= i;
  }
  return Factorial;
};
