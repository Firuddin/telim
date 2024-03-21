/*let yenisetir = "\r\n";
let cash = 1000;
let metin =
  "1-cash goruntuleme" +
  yenisetir +
  "2 -pul cekmek" +
  yenisetir +
  " 3 -pul yatirmaq" +
  yenisetir +
  "4 -çxaris" +
  yenisetir;
("zehmet olmasa bir deger secin");

let secim = prompt(metin);
switch (secim) {
  case "1":
    alert("senin cashin 1000 azn-dir");
    break;
  case "2":
    let cekilecekpul = +prompt("cekmek istediyiniz mebleq");
    if (cekilecekpul <= cash) {
      cash = cash - cekilecekpul;
      alert("balansinizda" + cash + "Azn qaldi");
    } else {
      alert(
        "cekilecek mebleq balansinizdaki mebleqden coxdur!" +
          yenisetir +
          "cash:" +
          cash +
          "" +
          "cekilenpul:" +
          cekilecekpul
      );
    }
    break;
  case "3":
    let pulYatirmaq = +prompt("yatiracaqiniz mebleq");
    cash = cash + pulYatirmaq;
    alert("sizin yatirdiqiniz mebleğ:" + pulYatirmaq + "umumi olaraq:" + cash);
    break;
  case "4":
    let cixaris = prompt("cixaracaqiniz mebleqi daxil edin");
    if (cash < cixaris) {
      alert("balansinizda kifayet qeder vesait yoxdur");
    } else {
      cash = cash - cixaris;
      alert(
        "cixaracqiniz mebleq:" + cixaris + "balansinizda qalan mebleq :" + cash
      );
    }
  default:
    alert("zehmet olmasa 1 ile 4 arasinda bir reqem daxil edin");
}

let yeniSetr = "\r\n"
let cash = 1000
let metn = 
"1-Balansindaki mebleq" +
yeniSetr+
"2-Cekilecek mebleq"+
yeniSetr+
"3-yatirilacaq mebleq"

let  secim = prompt(metn)
switch (secim) {
  case "1":
    alert("senin Cash-in:" + cash+ "azn-dir")
    break;
    case "2":
    let cixarilacaqPul = +prompt("cekeceyiniz mebleqi daxil edin")
    if (cixarilacaqPul>cash) {
      alert("sizin balansinizda bu qeder mebleq movcud deyil");
    }else{
      cash= cash-cixarilacaqPul
      alert("balansinizda:"+cash+"azn pul qaldi")
    }
    case "3":
      let yatirilacaqMebleq = +prompt("zehmet olmasa yatiracaqiniz mebleqi daxil edin")
if (yatirilacaqMebleq>0) {
  cash=cash+yatirilacaqMebleq
  alert("balansinizdaki mebleq:"+cash +"azn-dir")
}else{
  alert("zehmet olmasa duz emelli pul yatirin")
}
  default:
    alert("reqem secmediz")
    break;
}

let  name = 7>5
console.log(typeof name);*/

import { userValidation } from "./easy/1_userValidation.js";
console.log(userValidation("u_helo_world123"));
