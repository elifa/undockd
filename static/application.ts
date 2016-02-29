import Test from "./services/test";
import DateWidget from "./components/DynamicContainer";

//document.registerElement('date-widget', DateWidget);
new DateWidget();
console.log("HEJ!!!!!");
var element = document.createElement("DateWidget");
document.body.appendChild(element);
//div.textContent = new Test().getTest() + " HEJ!!!";
//alert(new Test().getTest());
