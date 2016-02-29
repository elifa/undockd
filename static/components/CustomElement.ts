export default class CustomElement extends HTMLElement {

  constructor() {
    super();
    console.log(this.constructor);
    //document.registerElement(this.constructor, this);
  };

}
