import regex from "./regex";

export default {
    required: (value:string) => !!value || 'Toto pole je vyžadováno',
    isValidDecimal: (value:string) => value.length > 0 ? ((!!value.match(regex.decimal) || !!value.match(/^[0-9]+$/)) || 'Pouze číselné hodnoty') : true,
    isValidInteger: (value:string) => value.length > 0 ? (!!value.match(regex.integer) || 'Pouze číselné hodnoty bez mezer') : true,
    isValidEmail: (value:string) => value.length > 0 ? (!!value.match(regex.email)) || 'Hodnota musí být email' : true,
}