export const URLS = {
    list:'sleepover_form:list',
    create:'sleepover_form:create',
}

export interface INewSleepoverRequest {
    requester_name:string,
    sleepover_date_from: string,
    sleepover_date_to: string,
    estimated_arrive_time: string,
    estimated_leave_time: string,
    num_persons: number,
    coitus: boolean,
    estimated_coitus_time_start: string,
    estimated_coitus_time_end:string,
    accepted: boolean,
}

export interface INewSleepoverRequestListItem {
    id:string
    requester_name:string,
    sleepover_date_from: string,
    sleepover_date_to: string,
    num_persons: number,
    coitus: boolean,
    accepted: boolean,
}