import {AxiosResponse} from "axios";
import {IShoppingListItem, URLS} from "@/components/Shopping-list/config";
import {api} from "@/api/axios-base";
import reverse from "django-reverse";


export const fetchShoppingList = async (): Promise<AxiosResponse<Array<IShoppingListItem>>> => {
    return await api.get(reverse(URLS.shopping_list))
}