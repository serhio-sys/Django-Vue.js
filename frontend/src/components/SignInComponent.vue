<script setup>
import BaseComponent from './BaseComponent.vue'
import Button from './UI/v-button.vue'
import CustomInput from './UI/v-Input.vue'
import { useStore } from 'vuex'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { HTTP } from '../api/axios'
import { handleInput } from '../utils/utils'

const user = ref(useStore().state.user) 
const router = useRouter()
const store = useStore()

if (!user.name === undefined) {
    router.push({ path: "/"})
}
const auth = ref({
    username:"",
    password:""
})

const errors = ref([])


const handleSubmit = async () => {
    if (auth.value.username !== "" && auth.value.password !== ""){
        try{    
            const response = await HTTP.post("/users/auth/token/login/", auth.value)
            console.log(response.data)
            try{
                const user = await HTTP.get("/users/auth/users/me/", {
                    headers:{
                        Authorization: `Token ${response.data?.auth_token}`
                    }
                }) 
                localStorage.setItem("username",user.data?.username)
                localStorage.setItem("id",user.data?.id)
                localStorage.setItem("token",response.data?.auth_token)
                store.dispatch('login',{name:user.data?.username,token:response.data?.auth_token,id:user.data?.id})
                router.push({path: "/"})
            }
            catch(err){
                console.log(err)
            }
        }
        catch(err){
            const data = err.response.data
            errors.value = []   
            Object.keys(data).forEach(element => {
                errors.value.push(data[element][0])
            });
        }   
    }
}

</script>

<template>
  <BaseComponent>
    <div class="content">
        <form @submit.prevent = "handleSubmit" class="form">
            <h1>Sign In</h1>
            <div class="errors" v-if="errors.length > 0">
                <div v-for="err in errors" class="error">{{err}}</div>
            </div>
            <CustomInput :type="'text'" :name="'username'" v-on:input="(e) => handleInput(auth,e)" :placeholder="'Username'" />
            <CustomInput :type="'password'" :name="'password'" v-on:input="(e) => handleInput(auth,e)" :placeholder="'Password'"/>
            <Button>Sign In</Button>
        </form>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">

@import "../scss/variables.scss";
@import "../scss/baseForms.scss";

    
    
</style>
