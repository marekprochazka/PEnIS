<template>
  <div class="sleepoverRequestsCalendar__container mt-15">
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

export default {
  name: 'Sleepover-request-calendar',
  data() {
    return {
      start: '2020-01-01',
      weekdays: [1, 2, 3, 4, 5, 6, 0],
      type: 'month',
      events: [
        {
          name: 'Test title',
          start: '2020-01-01 13:30',
          end: '2020-01-04 13:30',
          color: 'pink'
        },
          {
          name: 'Test title',
          start: '2020-01-01',
          end: '2020-01-04',
          color: 'green'
        },
        {
          name: 'Test title',
          start: '2020-01-05 13:30',
          end: '2020-01-05 16:30',
          color: 'pink'
        },
        {
          name: 'Test title',
          start: '2020-01-05 14:30',
          end: '2020-01-05 17:30',
          color: 'green'
        },
      ]
    }
  },
  methods: {}

}
</script>