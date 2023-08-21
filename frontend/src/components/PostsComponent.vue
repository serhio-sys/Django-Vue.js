<script setup>
import BaseComponent from './BaseComponent.vue'
import { HTTP } from '../api/axios'
import { onMounted, ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { RouterLink } from 'vue-router';

const store = useStore()
const router = useRouter()
const data = ref([])
const currentpage = ref(1)

onMounted(async () => {
  try{
    const response = await HTTP.get(`posts/?page=${currentpage.value}`)
    data.value = response.data.results  
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
            <div class="post__head">
              <img v-if="post.image" class="post__image" />
              <img src="../../public/bg.png" class="post__image" v-else/> 
              <div class="post__name">{{ post.name }}</div>
            </div>
            <div class="post__desc">{{ post.desc }}</div>
            <router-link class="post__readmore" :to="{name:'Home'}">Read More</router-link>
            <div class="post__footer">
              <div class="post__likes">{{ post.likes }}</div>
              <button class="post__like-btn">Like</button>
            </div>
          </article>
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
      margin-top: 2em;
      color: white;

    }
  }
  .post{
    display: flex;
    flex-direction: column;
    background-image: linear-gradient(to top,rgba(255, 166, 0, 0.473),rgba(3, 166, 3, 0.522));
    padding: 0.4em;
    gap: 0.2em;
    cursor: pointer;
    &__head{
      position: relative;
      width: 200px;
      height: 250px;
      overflow: hidden;
      transition: all ease 500ms;
    }
    &__image{
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
      top:0;
      left:0;
      object-position: center;
      transition: all 300ms;
    }
    &__head:hover{
      transform: scale(1.15,1.15);
    }
    &__head:hover .post__name{
      top: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    &__name{
      position: absolute;
      top: -85%;
      left: 0;
      z-index: 2;
      width: 100%;
      height: calc(100% - 1em);
      text-align: center;
      display: flex;
      align-items: flex-end;
      justify-content: center;
      font-family: $fontES;
      letter-spacing: 0.1em;
      font-style: italic;
      padding: 0.5em 0;
      background-image: linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6));
      transition: all ease 300ms;
    }
    &__desc{
      font-family: $fontR;
      font-style: italic;
      height: 50px;
      overflow: hidden;
      width: 100%;
    }
    &__footer{
      display: flex;
      margin-top: 1em;
      flex-direction: row-reverse;
      justify-content: center;
      align-items: center;
      gap: 1em;
    }
    &__like-btn{
      outline: none;
      border-radius: 0.4em;
      border: none;
      background-color: green;
      color: white;
      border: 2px solid white;
      font-size: 18px;
      padding: 0.3em;
      width: 100px;
      cursor: pointer;
      transition: 300ms ;
    }
    &__readmore{
      text-align: center;
      color: white;
      text-decoration: none;
      transition: all ease 300ms;
    }
    &__readmore:hover{
      transform: scale(1.2,1.2);
      color: $colorGrey;
    }
    &__like-btn:hover{
      background-color: rgba(0, 0, 0, 0.6);
    }
  }
</style>
