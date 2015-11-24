export default interface IComponent {

  name : string;
  template : string;

  onAttach(): void;
  onDetach(): void;
  onChange(): void;

}
