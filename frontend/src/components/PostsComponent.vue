<script setup>
import BaseComponent from './BaseComponent.vue'
import { HTTP } from '../api/axios'
import { onMounted, ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore()
const router = useRouter()
const data = ref([])

onMounted(async () => {
  try{
    const response = await HTTP.get("posts/")
    data.value = response.data
    console.log(data.value)
  }
  catch(err){
    console.log(err)
  }
})


</script>

<template>
  <BaseComponent>
    <div class="body__container">
      <div class="body__creation__posts" v-if="store.state.user.name">
        <Button v-on:click="router.push({path:'/create-post/'})">Create Post</Button>
      </div>
      <div class="body__posts-container">
          <article v-for="post in data" class="post">
            {{ post.name }}
          </article>
      </div>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
  .body{
    &__container{
    }
    &__posts-container{
      margin-top: 1em;
      color: white;
    }
  }
</style>
