<script setup>
import BaseComponent from './BaseComponent.vue'
import { HTTP } from '../api/axios'
import { onMounted, ref, watch } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex'
import Post from './UI/v-post.vue'
import vPaginator from './UI/v-Paginator.vue'

const store = useStore()
const router = useRouter()
const data = ref()
const currentPage = ref(1)
const maxPages = ref()

onMounted(async () => {
  try{
    const response = await HTTP.get(`/posts/?page=${currentPage.value}`)
    maxPages.value = response.data.max_page
    currentPage.value = response.data.page
    data.value = response.data.results
  }
  catch(err){
    console.log(err)
  }
})

watch(currentPage, async () => {
  try{
    const response = await HTTP.get(`/posts/?page=${currentPage.value}`)
    maxPages.value = response.data.max_page
    currentPage.value = response.data.page
    data.value = response.data.results
  }
  catch(err){
    console.log(err)
  }
})

const removePost = (id) => {
    data.value = data.value.filter(item => {
        return item.id != id
    })
    return true
}

const changePage = (event) => {
    currentPage.value = Number(event.target.innerHTML)
}

</script>

<template>
  <BaseComponent>
    <div class="body__container">
      <div class="body__creation__posts" v-if="store.state.user.name">
        <Button v-on:click="router.push({path:'/create-post/'})">Create Post</Button>
      </div>
      <div class="body__posts-container">
          <Post v-for="post in data" :key="post.id" @remove="removePost" :canRemove="true" :post="post"/>
      </div>
      <div class="body__paginator-container">
          <vPaginator :currentPage="currentPage" :maxPages="maxPages" @changePage="changePage" />
      </div>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
  @import '../scss/variables.scss';
  @import '../scss/postsList.scss';

</style>
