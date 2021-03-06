<template>
    <v-form @submit.prevent="sendData" ref="sleepoverForm">
      <v-container>
        <v-row class="mt-1">
          <v-col
              cols="12"
              md="6"
              class="input--required"
              dense
          >
            <v-text-field
                v-model="formData.requester_name"
                label="Jméno žadatele"
                validate-on-blur
                outlined
                :rules="[rules.required]"
                dense
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="6"
              class="input--required"
          >
            <v-text-field
                readonly
                v-model="formData.sleepover_date_from"
                label="Datum příjezdu"
                validate-on-blur
                outlined
                :rules="pickerRules"
                dense
            >
              <template v-slot:append>
                <DatePicker v-model="formData.sleepover_date_from" :allowed-dates="disablePastDates"/>
              </template>
            </v-text-field>
          </v-col>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.estimated_arrive_time"
                label="Odhadovaný čas příjezdu"
                validate-on-blur
                outlined
                dense
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_arrive_time"/>
              </template>
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="6"
              class="input--required"
          >
            <v-text-field
                readonly
                v-model="formData.sleepover_date_to"
                label="Datum odjezdu"
                validate-on-blur
                outlined
                :rules="pickerRules"
                dense
            >
              <template v-slot:append>
                <DatePicker v-model="formData.sleepover_date_to" :allowed-dates="disableDatesBeforeDateFrom"/>
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
                outlined
                dense
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_leave_time"/>
              </template>
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="3"
              class="input--required"
          >
            <v-text-field
                label="Počet osob"
                v-model="formData.num_persons"
                validate-on-blur
                type="number"
                outlined
                :rules="[rules.required]"
                dense
            />
          </v-col>
          <v-col
              cols="12"
              md="3"
          >
            <v-checkbox
                label="Bude sex?"
                v-model="formData.coitus"
                dense
            />
          </v-col>
          <v-col v-if="formData.coitus"
                 cols="12" md="6" class="input--required"
          >

            <v-select
                label="Pravděpodobnost sexu"
                v-model="formData.coitus_probability"
                :items="coitus_probabilities"
                :item-text="value => value.description"
                :item-value="value => value"
                outlined
                :rules="formData.coitus ? [rules.required]:[]"
                dense
            />
          </v-col>
        </v-row>
        <v-row v-if="formData.coitus">
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.estimated_coitus_time_start"
                label="Odhadovaný čas začátku sexu"
                validate-on-blur
                outlined
                dense
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_coitus_time_start"/>
              </template>
            </v-text-field>
          </v-col>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                readonly
                v-model="formData.estimated_coitus_time_end"
                label="Odhadovaný čas konce sexu"
                validate-on-blur
                outlined
                dense
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_coitus_time_end"
                            :allowed-hours="(val) => disableTimeBeforeCoitusStart(val, 'hr')"
                            :allowed-minutes="(val) => disableTimeBeforeCoitusStart(val, 'min')"
                />
              </template>
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="12"
          >
            <v-textarea
                v-model="formData.note"
                label="Poznámka"
                validate-on-blur
                outlined
                dense
                rows="1"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              md="3"/>
          <v-col
              cols="12"
              md="6"
          >
            <v-btn type="submit" color="primary" block>Odeslat žádost</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
</template>

<script>
import DatePicker from '@/components/utils/Date-picker'
import TimePicker from '@/components/utils/Time-picker'
import {createSleepoverRequest, fetchTypeCoitusProbabilities} from "@/components/New-sleepover-request/api";
import rules from '@/utils/rules'

export default {
  name: 'New-sleepover-request-form',
  data() {
    return {
      rules: {
        ...rules
      },
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
        coitus_probability: null,
        note: null,
      },
      coitus_probabilities: null,
      pickerRules: [],
      lastPickedHour: null
    }
  },
  async mounted() {
    fetchTypeCoitusProbabilities()
        .then(response => {
          this.coitus_probabilities = response.data
        })
  },

  computed: {
    today() {
      let today = new Date();
      let month = today.getMonth() + 1
      return today.getFullYear() + '-' + ('00' + month).slice(-2) + '-' + today.getDate();
    }
  },

  methods: {
    sendData() {
      this.pickerRules = [rules.required]
      console.log(this.pickerRules)
      if (this.$refs.sleepoverForm.validate()) {
        this.formData.coitus_probability = this.formData.coitus_probability ? this.formData.coitus_probability.id : null
        createSleepoverRequest(this.formData)
            .then(() => {
              this.$router.push({name: 'Sleepovers-list'})
            })
      }

    },
    nullizeCoitusVariables() {
      this.formData.coitus_probability = null
      this.formData.estimated_coitus_time_start = null
      this.formData.estimated_coitus_time_end = null
    },
    disableDatesBeforeDateFrom(val) {
      if (this.formData.sleepover_date_from !== '') {
        return val >= this.formData.sleepover_date_from
      }
      return true
    },
    disablePastDates(val) {
      return val >= this.today
    },
    disableTimeBeforeCoitusStart(val, type) {
      if (this.formData.estimated_coitus_time_start) {
        if (type === 'min') {
          if (this.lastPickedHour > parseInt(this.formData.estimated_coitus_time_start.split(':')[0])) {
            return true
          } else {
            return val >= this.formData.estimated_coitus_time_start.split(':')[1]
          }
        } else if (type === 'hr') {
          this.lastPickedHour = val
          return val >= this.formData.estimated_coitus_time_start.split(':')[0]
        }
      }
    }
  },

  watch: {
    'formData.coitus': {
      handler(val) {
        if (!val) {
          this.nullizeCoitusVariables()
        }
      }
    },
    'formData.sleepover_date_from': {
      handler() {
        this.pickerRules = []
      }
    },
    'formData.sleepover_date_to': {
      handler() {
        this.pickerRules = []
      }
    }
  },

  components: {
    DatePicker,
    TimePicker
  }
}
</script>