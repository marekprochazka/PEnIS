import {AxiosResponse} from "axios";
import {
    IBoughtParam,
    IShoppingItemCreate,
    IShoppingListItem,
    ITypeUrgency,
    URLS
} from "@/components/Shopping-list/config";
import {api, csrfHeader} from "@/api/axios-base";
import reverse from "django-reverse";


export const fetchShoppingList = async (param: IBoughtParam | null): Promise<AxiosResponse<Array<IShoppingListItem>>> => {
    return await api.get(reverse(URLS.shopping_list), {params: param ? param : {}})
}

export const fetchUrgenciesList = async (): Promise<AxiosResponse<Array<ITypeUrgency>>> => {
    return await api.get(reverse(URLS.urgencies_list))
}

export const createShoppingItem = async (data: IShoppingItemCreate): Promise<null> => {
    return await api.post(reverse(URLS.shopping_create), data, csrfHeader())
}

export const updateShoppingItem = async (data: IBoughtParam, id:string): Promise<null> => {
    return await api.put(reverse(URLS.shopping_update, id), data, csrfHeader())
}