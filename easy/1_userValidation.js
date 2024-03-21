export const userValidation = (str) => {
  if (str.length >= 4 && str.length <= 25) {
    return true;
  }else{
    return false
  }
};

