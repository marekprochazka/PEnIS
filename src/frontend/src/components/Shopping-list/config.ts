export const URLS = {
    shopping_list: 'shopping:list',
    urgencies_list: 'shopping:urgencies_list',
    shopping_create: 'shopping:create',
    shopping_update: 'shopping:update'
}

export interface ITypeUrgency {
    identifier: string,
    description: string,
    id: string
}

export interface IShoppingListItem {
    id: string,
    description: string,
    quantity: string,
    urgency: ITypeUrgency,
    bought: boolean
}

export interface IShoppingItemCreate {
    description: string,
    quantity: string,
    urgency: string
}

export interface IBoughtParam {
    bought: boolean
}