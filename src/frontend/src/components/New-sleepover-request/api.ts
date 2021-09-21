import {URLS, INewSleepoverRequest} from "@/components/New-sleepover-request/config";
import {api} from '@/api/axios-base'
import reverse from "django-reverse";


export const createSleepoverRequest = (data: INewSleepoverRequest): Promise<null> => {
    return api.post(reverse(URLS.list), data)
}