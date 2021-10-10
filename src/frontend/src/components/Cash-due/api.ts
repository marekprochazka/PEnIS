import {AxiosResponse} from "axios";
import {
    ICashDueItemCreate,
    ICashDueListItem,
    IPaidBack,
    URLS} from "@/components/Cash-due/config";
import {api, csrfHeader} from "@/api/axios-base";
import reverse from "django-reverse";

export const fetchCashDueList = async (param: IPaidBack | null): Promise<AxiosResponse<Array<ICashDueListItem>>> => {
    return await api.get(reverse(URLS.cash_due_list), {params: param ? param : {}})
}

export const createCashDueItem = async (data: ICashDueItemCreate) : Promise<null> => {
    return await api.post(reverse(URLS.cash_due_create), data, csrfHeader())
}

export const updateCashDueItem = async (data: IPaidBack, id:string): Promise<null> => {
    return await api.put(reverse(URLS.cash_due_update, id), data, csrfHeader())
}