<script setup>
import BaseComponent from './BaseComponent.vue'
import { HTTP } from '../api/axios'
import { onMounted, ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import Post from './UI/v-post.vue'

const store = useStore()
const router = useRouter()
const data = ref()
const currentpage = ref(1)

onMounted(async () => {
  try{
    const response = await HTTP.get(`posts/?page=${currentpage.value}`)
    data.value = response.data.results
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
          <Post v-for="post in data"  :post="post"/>
      </div>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
  @import '../scss/variables.scss';

  .body{
    &__container{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
    &__posts-container{
      display: flex;
      gap: 2em;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 2em;
      color: white;

    }
  }
  
 
</style>
