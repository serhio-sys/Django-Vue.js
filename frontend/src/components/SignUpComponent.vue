<script setup>
import BaseComponent from './BaseComponent.vue'
import Button from './UI/v-button.vue'

import { useStore } from 'vuex';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { HTTP } from '../api/axios'
import CustomInput from './UI/v-Input.vue'

const user = ref(useStore().state.user) 
const router = useRouter()
if (!user.name === undefined) {
    router.push({ path: "/"})
}
const auth = ref({
    username:"",
    email:"",
    password:"",
    password1:""
})
const autherr = ref({
    username:"",
    email:"",
    password:"",
    password1:""
})
const errors = ref([])

const haveUpperCase = (word) => {
    for (let i = 0; i < word.length; i++) {
      const element = word[i];
      if (element == element.toUpperCase()){
        return true
      }
    }
    return false
}

const checkOnFieldErrors = () => {
  if (autherr.value.username != "" || autherr.value.password != "" || autherr.value.password1 != "" || autherr.value.email != "") {
    return false
  }
  return true
}

const handleInput = (e) => {
    if (e.target.name === "username"){
      autherr.value.username = ""
      if (e.target.value.length < 8) {
        autherr.value.username += "\nLength of username less then 8 symbols"
      }
    }
    if (e.target.name === "email"){ 
      autherr.value.email = ""
      if (!e.target.value.includes("@")){
        autherr.value.email += "\nIncorrect email adress"
      } 
    }
    if (e.target.name === "password"){
      autherr.value.password = ""
      if (e.target.value.length < 8){
        autherr.value.password += "\nLength of password less then 8 symbols"
      }
      if (e.target.value.toLowerCase().includes(auth.value.username.toLowerCase())){
        autherr.value.password += "\nPassword is very similar to username"
      }
      if (!haveUpperCase(e.target.value)){
        autherr.value.password += "\nPassword must have a uppercase letter"
      }
    }
    if (e.target.name === "password1"){  
      autherr.value.password1 = ""
      if (e.target.value !== auth.value.password){
        autherr.value.password1 += "\nRepeated password is not equals"
      }
    }
    auth.value[e.target.name] = e.target.value
}

const handleSubmit = async () => {
    if (auth.value.username !== "" && auth.value.email !== "" && auth.value.password !== "" && checkOnFieldErrors()){
        try{    
            const response = await HTTP.post("users/auth/users/", auth.value)
            if (response.status === 201){
                router.push({ path:"/" })
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
        <h1>Sign Up</h1>
        <div class="errors" v-if="errors.length > 0">
          <div v-for="err in errors" class="error">{{err}}</div>
        </div>
        <CustomInput type="text" name="username" v-on:input="handleInput" placeholder="Username" />
        <div class="field_err" v-if="autherr.username">{{ autherr.username }}</div>
        <CustomInput type="email" name="email" v-on:input="handleInput" placeholder="Email"/>
        <div class="field_err" v-if="autherr.email">{{ autherr.email }}</div>
        <CustomInput type="password" name="password" v-on:input="handleInput" placeholder="Password"/>
        <div class="field_err" v-if="autherr.password">{{ autherr.password }}</div>
        <CustomInput type="password" name="password1" v-on:input="handleInput" placeholder="Repeat password"/>
        <div class="field_err" v-if="autherr.password1">{{ autherr.password1 }}</div>
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
        display: flex;
        color: white;
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
