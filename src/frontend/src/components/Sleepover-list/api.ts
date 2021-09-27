import {AxiosResponse} from "axios";
import {INewSleepoverRequestListItem, URLS} from "@/components/Sleepover-list/config";
import {api} from "@/api/axios-base";
import reverse from "django-reverse";

export const fetchSleepoverRequestList = async (): Promise<AxiosResponse<Array<INewSleepoverRequestListItem>>> => {
    return await api.get(reverse(URLS.list))
}