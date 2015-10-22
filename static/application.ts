import Test from "./services/test";

console.log("HEJ");
var div = document.createElement("div");
document.body.appendChild(div);
div.textContent = new Test().getTest() + " HEJ!!!";
//alert(new Test().getTest());
