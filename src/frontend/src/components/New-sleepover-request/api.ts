import {URLS, INewSleepoverRequest, ITypeCoitusProbability} from "@/components/New-sleepover-request/config";
import {api, csrfHeader} from '@/api/axios-base'
import reverse from "django-reverse";
import {AxiosResponse} from "axios";


export const createSleepoverRequest = async (data: INewSleepoverRequest): Promise<null> => {
    return await api.post(reverse(URLS.create), data, csrfHeader())
}



export const fetchTypeCoitusProbabilities = async (): Promise<AxiosResponse<Array<ITypeCoitusProbability>>> => {
    return await api.get(reverse(URLS.probabilitiesList))
}