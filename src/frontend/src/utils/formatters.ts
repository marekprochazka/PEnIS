export const getFormattedMonth = (month:number, year:number): string => {
    const event = new Date(Date.UTC(year, month-1))
    const options = { year: 'numeric', month: 'long'};
    return event.toLocaleDateString('cs-CZ', options)
}