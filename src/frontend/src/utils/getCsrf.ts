export const getCsrf = (): string => {
    let match = document.cookie.match(new RegExp('(^| )' + 'csrftoken' + '=([^;]+)'));
    let result = ''
    if (match) {
        match.forEach((value: string) => {
            if (value !== ' ' && !value.includes('=')) {
                result = value
            }
        })
    }
    return result
}