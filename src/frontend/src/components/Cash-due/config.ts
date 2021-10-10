export const URLS = {
    cash_due_list: 'shopping:cash_due_list',
    cash_due_create: 'shopping:cash_due_create',
    cash_due_update: 'shopping:cash_due_update'
}

export interface IPaidBack {
    paid_back: boolean
}

export interface ICashDueListItem {
    id: string,
    description: string,
    user: string,
    money_amount: string,
    paid_back: boolean
}

export interface ICashDueItemCreate {
    description: string,
    user: string,
    money_amount: string
}