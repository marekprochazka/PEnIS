import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme:{
        themes:{
            light:{
                primary: '#00035F',
                secondary: '#2F00D1',
                accent: '#B3B5F5',
                error: '#f44e62',
                warning: '#6F74ED',
                success: '#0eb574'

            }
        }
    }
});
