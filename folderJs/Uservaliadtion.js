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
/*export const FourElement = (arr) => {
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
};*/
/*export const FiveElement = (par) => {
  if (par.length < 5) {
    return false;
  }
  let newArr = par.replace(/[^0-9?]/g, "");

  let name = newArr.split("");

  let sums = [];
  let sum = 0;
  let iteration = 0;

  name.forEach((item) => {
    if (item != "?") {
      sum = parseInt(item) + parseInt(name[iteration + 4]);
      sums.push(sum);
    }
    iteration += 1;
  });
  return sums;
};*/
/*export const FourElement = (Str) => {
  if (Str.length > 5) {
    return false;
  }

  let newArr = Str.replace(/[^0-9?]/g, "").split("");
  

  let sums = []
  let sum=0
  let iteration = 0

  newArr.forEach((item) => {
if (item!= 0) {
  sum = +item+ +newArr[iteration+4]
  sums.push(sum)
}
iteration+=1

    
  });
  return sums
};
*/

export const sixElement = (str) => {
  let number = 0;//1,3,6,10,15
  for (let i = 1; i <= str; i++) {
    //number+=i
    number = number + i;
  }
  return number;
};
