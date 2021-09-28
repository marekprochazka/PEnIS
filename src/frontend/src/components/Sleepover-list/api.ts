import {AxiosResponse} from "axios";
import {
    IAcceptStatusData,
    ICalendarListQueryParams, ISleepoverRequestCalendarListItem,
    ISleepoverRequestListItem,
    URLS
} from "@/components/Sleepover-list/config";
import {api, csrfHeader} from "@/api/axios-base";
import reverse from "django-reverse";

export const fetchSleepoverRequestList = async (): Promise<AxiosResponse<Array<ISleepoverRequestListItem>>> => {
    return await api.get(reverse(URLS.list))
}

export const updateAcceptStatus = async (data: IAcceptStatusData, id: string): Promise<null> => {
    return await api.post(reverse(URLS.accept_status, id), data, csrfHeader())
}

export const fetchSleepoverRequestCalendarList = async (params: ICalendarListQueryParams): Promise<AxiosResponse<Array<ISleepoverRequestCalendarListItem>>> => {
    return await api.get(reverse(URLS.calendar_list), {params: params})
}