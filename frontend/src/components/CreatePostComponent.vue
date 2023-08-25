<script setup>
import BaseComponent from './BaseComponent.vue'
import { useStore } from 'vuex'
import { ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router'
import Input from './UI/v-Input.vue'
import vTextarea from './UI/v-Textarea.vue'
import { HTTP } from '../api/axios'


const router = useRouter()
const errors = ref([])
const user = ref(useStore().state.user) 
const data = ref({
  name:"",
  desc:"",
  author:user.value.id,
  image:null
})

const handleSubmit = async () => {
  console.log(data.value)
  if (data.value.name != "" && data.value.desc != ""){
        try{    
            const response = await HTTP.post("posts/create/", data.value, {
              headers:{
                Authorization: `Token ${user.value.token}`
              }
            })
            if (response.status === 201){
                router.push({ path:"/" })
            }
            console.log(response)
        }
        catch(err){
            console.log(err)
        }   
    }
}

const handleInput = (e) => {
    data.value[e.target.name] = e.target.value
}


</script>



<template>
  <BaseComponent>
    <div class="content">
        <form @submit.prevent = "handleSubmit" class="form" enctype="multipart/form-data">
            <h1>Creating Post</h1>
            <div class="errors" v-if="errors.length > 0">
                <div v-for="err in errors" class="error">{{err}}</div>
            </div>
            <Input type="text" v-on:input="handleInput" name="name" placeholder="Name"/>
            <Input type="file" v-on:input="handleInput" name="image" placeholder="Image" />
            <vTextarea name="desc" v-on:input="handleInput" placeholder="Decription" />
            <Button>Create Post</Button>
        </form>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
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
    }
    .errors{
        padding: 0.4em 1em;
        width: calc(400px - 2em);
        color: red;
        text-align: center;
    }
</style>
