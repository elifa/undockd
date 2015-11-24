
class DynamicContainer {
    private template = `my
    template
    string`

    constructor() {
        this.template.toString();
    }
}
var template: string = `<button>test</button>`
export default class DateWidget extends HTMLElement {

    applyAuthorStyles = true;

    // Fires when an instance of the element is created.
    createdCallback() {
        /*var root = this.createShadowRoot();
        root.applyAuthorStyles = true;
        root.resetStyleInheritance = true;*/
        this.innerHTML = template;
    };

    // Fires when an instance was inserted into the document.
    attachedCallback() {
        console.error("attachedCallback");
    };

    // Fires when an attribute was added, removed, or updated.
    attributeChangedCallback(attrName: string, oldVal: string, newVal: string) {
        console.error("attributeChangedCallback", attrName, oldVal, newVal);
    };
}
