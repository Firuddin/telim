export const userValidation = (str) => {
  if (str.length >= 4 && str.length <= 25 && (/[a-zA-Z]/).test(str.slice(0,1))&&(/^\w+$/).test(str)) {
    return true;
  }else{
    return false
  }
};

