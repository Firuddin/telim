//Task:1
/*export const FirstElement = (Num) => {
  let factorial = 1;
  for (let i = 1; i <= Num; i++) {
    factorial *= i;
  }
  return factorial;
};

*/
//Task2
/*export const NewElement = (name)=>{
 let hello = name.split("")
 let newWord = hello.reverse()
 let common = newWord.join("")
return common
}*/

//Task3
/*export const ThreeElement =(param)=>{
  return param.split("").reverse("").join("")
}*/

//Task4
export const FourElement = (arr) => {
  let set1 = arr[0].split(",");
  let set2 = arr[1].split(",");
  let select = [];

  set2.forEach((item) => {
    if (set1.includes(item)) {
      select.push(item);
    }
  });

  if (select !== 0) {
    return select.toString();
  } else {
    return false;
  }
};