<template>
  <v-card class="mx--center elevation-2 light">
    <v-form>
      <v-container>
        <v-row>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                v-model="formData.requester_name"
                label="Jméno žadatele"
                validate-on-blur
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.sleepover_date_from"
                label="Datum příjezdu"
                validate-on-blur
            >
              <template v-slot:append>
                <DatePicker v-model="formData.sleepover_date_from"/>
              </template>
            </v-text-field>
          </v-col>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.sleepover_date_to"
                label="Datum odjezdu"
                validate-on-blur
            >
              <template v-slot:append>
                <DatePicker v-model="formData.sleepover_date_to"/>
              </template>
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.estimated_arrive_time"
                label="Odhadovaný čas příjezdu"
                validate-on-blur
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_arrive_time"/>
              </template>
            </v-text-field>
          </v-col>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.estimated_leave_time"
                label="Odhadovaný čas odjezdu"
                validate-on-blur
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_leave_time"/>
              </template>
            </v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
import DatePicker from '@/components/utils/Date-picker'
import TimePicker from '@/components/utils/Time-picker'

export default {
  name: 'New-sleepover-request-form',
  data() {
    return {
      formData: {
        requester_name: null,
        sleepover_date_from: null,
        sleepover_date_to: null,
        estimated_arrive_time: null,
        estimated_leave_time: null,
        num_persons: null,
        coitus: false,
        estimated_coitus_time_start: null,
        estimated_coitus_time_end: null,
        accepted: false,
      }
    }
  },
  components: {
    DatePicker,
    TimePicker
  }
}
</script>