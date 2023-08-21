<script setup>
import BaseComponent from './BaseComponent.vue'
import Button from './UI/v-button.vue'

import { useStore } from 'vuex'
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { HTTP } from '../api/axios'

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


const handleInput = (e) => {
    auth.value[e.target.name] = e.target.value
}

const handleSubmit = async () => {
    if (auth.value.username !== "" && auth.value.password !== ""){
        try{    
            const response = await HTTP.post("users/auth/token/login/", auth.value)
            console.log(response.data)
            try{
                const user = await HTTP.get("users/auth/users/me/", {
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
            <input type="text" name="username" v-on:input="handleInput" placeholder="Username"/>
            <input type="password" name="password" v-on:input="handleInput" placeholder="Password"/>
            <Button>Sign In</Button>
        </form>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">

@import "../scss/variables.scss";
    @keyframes anim{
        0%{
            background-size: 0% 2px;
        }
        100%{
            background-size: 100% 2px;
        }
    }
    .content{
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .form{
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        max-width: 300px;
        gap: 0.5em;
        input{
            color: gray;
            background: transparent;
            background-image: linear-gradient(currentcolor,currentcolor);
            background-repeat: no-repeat;
            background-size: 100% 2px;
            outline: none;
            border: none;
            font-size: 18px;    
            padding: 0.3em 0.5em;
            transition: all ease-in 300ms;
            background-position: 0% 100%;
        }
        input:focus{
            background-image: linear-gradient(to right, white,lightgray);
            background-size: 100% 2px;
            animation: anim 400ms 1;
            color: white;
        }
    }
    .errors{
        padding: 0.4em 1em;
        width: calc(400px - 2em);
        color: red;
        text-align: center;
    }
    
</style>
