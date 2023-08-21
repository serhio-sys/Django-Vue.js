<script setup>
import BaseComponent from './BaseComponent.vue'
import { useStore } from 'vuex'
import { ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router'

const route = useRouter()
const errors = ref([])
const user = ref(useStore().state.user) 

const handleSubmit = async () => {

}

</script>

<template>
  <BaseComponent>
    <div class="content">
        <form @submit.prevent = "handleSubmit" class="form">
            <h1>Creating Post</h1>
            <div class="errors" v-if="errors.length > 0">
                <div v-for="err in errors" class="error">{{err}}</div>
            </div>
            <input type="text" name="name" placeholder="Name"/>
            <input type="image" name="image" placeholder="Image" />
            <textarea name="desc" placeholder="Decription"></textarea>
            <Button>Sign In</Button>
        </form>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
  
</style>
