export const URLS = {
    list:'sleepover_form:list',
    accept_status:'sleepover_form:accept_status_update'
}

export interface ITypeCoitusProbability {
    identifier: string,
    description_alt: string,
    id: string
}

export interface INewSleepoverRequestListItem {
    id:string
    requester_name:string,
    sleepover_date_from: string,
    sleepover_date_to: string,
    num_persons: number,
    coitus: boolean,
    accepted: boolean,
    coitus_probability: ITypeCoitusProbability
}

export interface IAcceptStatusData {
    accept_status: string
}