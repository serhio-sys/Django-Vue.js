<script setup>
import BaseComponent from './BaseComponent.vue'
import { useStore } from 'vuex'
import { ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router'
import Input from './UI/v-Input.vue'
import vTextarea from './UI/v-Textarea.vue'
import { REQUIRE_AUTH_HTTP } from '../api/axios'
import { handleInput } from '../utils/utils'


const router = useRouter()
const errors = ref([])
const formImage = ref()
const user = ref(useStore().state.user) 
const data = ref({
  name:"",
  desc:"",
  author:user.value.id
})

const handleSubmit = async () => {
  let formData = new FormData()
  formData.append("name",data.value.name)
  formData.append("desc",data.value.desc)
  formData.append("author",data.value.author)
  formData.append("image",formImage.value)
  if (data.value.name != "" && data.value.desc != ""){
        try{    
            const response = await REQUIRE_AUTH_HTTP(user.value.token).post("/posts/create/", formData)
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

const onChange = (event) => {
    formImage.value = event.target.files[0]
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
            <Input type="text" v-on:input="(e) => handleInput(data,e)" name="name" placeholder="Name"/>
            <Input type="file" v-on:change="onChange" name="image" placeholder="Image" />
            <vTextarea name="desc" v-on:input="(e) => handleInput(data,e)" placeholder="Decription" />
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
