<script setup>
import { REQUIRE_AUTH_HTTP } from '../api/axios'
import { onMounted, watch, ref } from 'vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import Post from './UI/v-post.vue'
import BaseComponent from './BaseComponent.vue';
import vPaginator from './UI/v-Paginator.vue';

const store = useStore()
const router = useRouter()
const maxPages = ref()
const data = ref([])
const currentPage = ref(1)

onMounted(async () => {
  try{
    const response = await REQUIRE_AUTH_HTTP(store.state.user.token).get(`/posts/liked/?page=${currentPage.value}`)
    data.value = response.data.results
    maxPages.value = response.data.max_page
    currentPage.value = response.data.page
  }
  catch(err){
    console.log(err)
  }
})


watch(currentPage, async () => {
  try{
    const response = await REQUIRE_AUTH_HTTP(store.state.user.token).get(`/posts/liked/?page=${currentPage.value}`)
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
      <h1 style="color: white;">Liked</h1>
      <div class="body__posts-container">
        {{ console.log(data) }}
        <Post v-if="data.length" @remove="removePost" :key="post.id" v-for="post in data" :post="post"/>
        <div v-else>You don`t have liked posts.</div>
      </div>
      <div class="body__paginator-container">
          <vPaginator v-if="data.length > 0" :currentPage="currentPage" :maxPages="maxPages" @changePage="changePage" />
      </div>
    </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
  @import '../scss/variables.scss';
  @import '../scss/postsList.scss';
</style>
