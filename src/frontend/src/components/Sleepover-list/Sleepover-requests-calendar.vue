<template>
  <div class="sleepoverRequestsCalendar__container mt-5">

    <v-row>
      <v-col cols="12" md="3"/>
      <v-col cols="12" md="6">
        <v-text-field readonly outlined :value="formattedSelectedDate" class="input--center">
          <template v-slot:prepend-inner>
            <v-icon @click="monthUpdate('down')">mdi-arrow-left-bold</v-icon>
          </template>
          <template v-slot:append>
            <v-icon @click="monthUpdate('up')">mdi-arrow-right-bold</v-icon>
          </template>
        </v-text-field>
      </v-col>
      <v-col cols="12" md="3"/>
    </v-row>
    <v-calendar
        ref="calendar"
        :weekdays="weekdays"
        :type="type"
        locale="cs-CZ"
        :start="start"
        :events="events"
        event-overlap-mode="column"
    >

    </v-calendar>
  </div>
</template>

<script>

import {getFormattedMonth} from "@/utils/formatters";
import {getTodayString} from "@/utils/today";
import {fetchSleepoverRequestCalendarList} from "@/components/Sleepover-list/api";

export default {
  name: 'Sleepover-request-calendar',
  data() {
    return {
      start: '2020-01-01',
      weekdays: [1, 2, 3, 4, 5, 6, 0],
      type: 'month',
      events: [],
      selectedYear: 2021,
      selectedMonth: 4,
    }
  },
  async mounted() {
    await this.assignTodayVariables()
    await this.getSleepoverRequests()
  },
  computed: {
    formattedSelectedDate() {
      return getFormattedMonth(this.selectedMonth, this.selectedYear)
    }
  },
  methods: {
    assignTodayVariables() {
      this.start = getTodayString()
      this.selectedYear = parseInt(this.start.split('-')[0])
      this.selectedMonth = parseInt(this.start.split('-')[1])
    },
    getSleepoverRequests() {
      fetchSleepoverRequestCalendarList({year: this.selectedYear, month: this.selectedMonth})
          .then(response => {
            this.events = response.data
          })
    },
    increaseMonth() {
      if (this.selectedMonth === 12) {
        this.selectedMonth = 1
        this.selectedYear += 1
      } else {
        this.selectedMonth += 1
      }
      this.start = `${this.selectedYear}-${this.selectedMonth}-01`
    },
    decreaseMonth() {
      if (this.selectedMonth === 1) {
        this.selectedMonth = 12
        this.selectedYear -= 1
      } else {
        this.selectedMonth -= 1
      }
      this.start = `${this.selectedYear}-${this.selectedMonth}-01`
    },
    monthUpdate(direction) {
      if (direction === 'up') {
        this.increaseMonth()
      } else {
        this.decreaseMonth()
      }
      this.getSleepoverRequests()
    }
  }

}
</script>