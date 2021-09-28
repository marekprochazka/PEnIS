export const URLS = {
    shopping_list: 'shopping:list'
}

export interface ITypeUrgency {
    identifier: string,
    description: string
}

export interface IShoppingListItem {
    id: string,
    description: string,
    quantity: string,
    urgency: ITypeUrgency,
    bought: boolean
}