import Test from "./services/test";
import DateWidget from "./components/DynamicContainer";

document.registerElement('date-widget', DateWidget);

console.log("HEJ");
var element = document.createElement("date-widget");
document.body.appendChild(element);
//div.textContent = new Test().getTest() + " HEJ!!!";
//alert(new Test().getTest());
