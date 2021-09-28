import {AxiosResponse} from "axios";
import {IAcceptStatusData, INewSleepoverRequestListItem, URLS} from "@/components/Sleepover-list/config";
import {api, csrfHeader} from "@/api/axios-base";
import reverse from "django-reverse";

export const fetchSleepoverRequestList = async (): Promise<AxiosResponse<Array<INewSleepoverRequestListItem>>> => {
    return await api.get(reverse(URLS.list))
}

export const updateAcceptStatus = async (data: IAcceptStatusData, id:string): Promise<null> => {
    return await api.post(reverse(URLS.accept_status, id), data, csrfHeader())
}