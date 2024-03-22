export const UserValidation = (str) => {
 if (str.length>=4 && str.length<=25 && (/[a-zA-Z]/).test(str.slice(0,1))&&(/^\w+$/).test(str.slice(0))&& (/[a-zA-Z0-9]/).test(str.length-1)) {
  return true
 }else{
  return false
 }
};
