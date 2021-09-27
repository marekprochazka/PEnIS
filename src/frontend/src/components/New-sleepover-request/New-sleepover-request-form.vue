<template>
  <v-card class="mx--center elevation-2 light">
    <v-form @submit.prevent="sendData" ref="sleepoverForm">
      <v-container>
        <v-row class="mt-3">
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                v-model="formData.requester_name"
                label="Jméno žadatele"
                validate-on-blur
                outlined
                :rules="[rules.required]"
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
                outlined
                :rules="[rules.required]"
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
                v-model="formData.estimated_arrive_time"
                label="Odhadovaný čas příjezdu"
                validate-on-blur
                outlined
                :rules="[rules.required]"
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
          >
            <v-text-field
                readonly
                v-model="formData.sleepover_date_to"
                label="Datum odjezdu"
                validate-on-blur
                outlined
                :rules="[rules.required]"
            >
              <template v-slot:append>
                <DatePicker v-model="formData.sleepover_date_to"/>
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
                :rules="[rules.required]"
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
          >
            <v-text-field
                label="Počet osob"
                v-model="formData.num_persons"
                validate-on-blur
                type="number"
                outlined
                :rules="[rules.required]"
            />
          </v-col>
          <v-col
              cols="12"
              md="3"
          >
            <v-checkbox
                label="Bude sex?"
                v-model="formData.coitus"
            />
          </v-col>
          <v-col v-if="formData.coitus"
                 cols="12" md="6"
          >

            <v-select
                label="Pravděpodobnost sexu"
                v-model="formData.coitus_probability"
                :items="coitus_probabilities"
                :item-text="value => value.description"
                :item-value="value => value"
                outlined
                :rules="formData.coitus ? [rules.required]:[]"
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
                :rules="formData.coitus ? [rules.required]:[]"
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
                :rules="formData.coitus ? [rules.required]:[]"
            >
              <template v-slot:append>
                <TimePicker v-model="formData.estimated_coitus_time_end"/>
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
  </v-card>
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
      coitus_probabilities: null
    }
  },
  async mounted() {
    fetchTypeCoitusProbabilities()
        .then(response => {
          this.coitus_probabilities = response.data
        })
  },

  methods: {
    sendData() {
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
    }
  },

  watch: {
    'formData.coitus': {
      handler(val) {
        if (!val) {
          this.nullizeCoitusVariables()
        }
      }
    }
  },

  components: {
    DatePicker,
    TimePicker
  }
}
</script>