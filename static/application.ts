import Test from "./test.ts";

var div = document.createElement("div");
document.body.appendChild(div);
div.textContent = new Test().test;
