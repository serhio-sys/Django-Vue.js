<script setup>
import { REQUIRE_AUTH_HTTP } from '../api/axios'
import { onMounted, watch, ref } from 'vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import Post from './UI/v-post.vue'
import BaseComponent from './BaseComponent.vue';
import vPaginator from './UI/v-Paginator.vue';
import Button from './UI/v-button.vue';

const store = useStore()
const loaded = ref(false)
const router = useRouter()
const data = ref()
const currentPage = ref(1)
const maxPages = ref()

onMounted(async () => {
  try{
    const response = await REQUIRE_AUTH_HTTP(useStore().state.user.token)
    .get(`/posts/my-posts/?page=${currentPage.value}`)

    data.value = response.data.results
    maxPages.value = response.data.max_page
    currentPage.value = response.data.page
    data.value = response.data.results
    loaded.value = true
  }
  catch(err){
    console.log(err)
  }
})

watch(currentPage, async () => {
  try{
    const response = await REQUIRE_AUTH_HTTP(store.state.user.token)
    .get(`/posts/my-posts/?page=${currentPage.value}`)
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
  <BaseComponent v-if="loaded">
    <div class="body__container">
      <div>
          <h1 style="color: white;">Your posts</h1>
      </div>
      <div class="body__creation__posts" v-if="data.length == 0">
        <Button v-on:click="router.push({path:'/create-post/'})">Create Post</Button>
      </div>  
      <div class="body__posts-container">
          <Post v-if="data.length" v-for="post in data" :key="post.id" @remove="removePost" :post="post"/>
      </div>
    </div>
    <div class="body__paginator-container">
      <vPaginator v-if="data.length > 0" :currentPage="currentPage" :maxPages="maxPages" @changePage="changePage" />
    </div>
  </BaseComponent>
  <div v-else class="lds-default"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
</template>

<style scoped lang="scss">
  @import '../scss/variables.scss';
  @import '../scss/postsList.scss';
  @import '../scss/spinner.scss';
 
</style>
