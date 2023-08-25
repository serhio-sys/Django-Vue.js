<script setup>
import { defineProps, ref } from 'vue'
import { RouterLink } from 'vue-router';
import { useStore } from "vuex"
import { HTTP } from '../../api/axios';


const store = useStore()
const props = defineProps({
    post:Object
})
const user = store.state.user
const post = ref(props.post)
const toggleBody = ref(false)
console.log(post.value.liked)

const sizeUpFunction = (e) => {
  e.target.parentNode.parentNode.classList.toggle("open")
  e.target.parentNode.classList.toggle("open__post")
  if (toggleBody.value) {  
    document.querySelector("body").style.overflow = "visible"
  }
  else{  
    document.querySelector("body").style.overflow = "hidden"
  }
  window.scroll({
        top: 0,
        left: 0,
        behavior: "smooth",
    });
  toggleBody.value = !toggleBody.value
  e.target.parentNode.parentNode.querySelector('.post__readmore').classList.toggle("hide")
  
}

const LikeHandler = async (e) => {
    try{
        const response = await HTTP.post(`posts/like/${post.value.id}/`,{},{
            headers:{
                Authorization: `Token ${user.token}`
            }
        })
        if (response.status == 200){
            if (post.value.liked.includes(user.name)){
                post.value.liked = post.value.liked.filter(item=>{
                    return item != user.name
                })
                post.value.likes--
            }
            else{
                post.value.liked.push(user.name)
                post.value.likes++
            }
        }
    }
    catch(err){
        console.log(err)
    }
}

</script>
<template>
    <article class="post">
        <div v-on:click="sizeUpFunction" class="post__head">
            <img v-if="post.image" class="post__image" />
            <img v-else src="../../../public/bg.png" class="post__image" /> 
            <div class="post__name">{{ post.name }}</div>
        </div>
        <div class="post__desc">{{ post.desc }}</div>
        <router-link class="post__readmore" :to="{name:'Home'}">Read More</router-link>
        <div class="post__footer">
            <div class="post__likes">{{ post.likes }}</div>
            <div v-if="post.author != user.id">
                <button v-if="!post.liked.includes(user.name)" v-on:click="LikeHandler" class="post__like-btn">Like</button>
                <button v-else v-on:click="LikeHandler" class="post__like-btn">Unlike</button>
            </div>
            <div v-else>
                Likes:
            </div>    
        </div>
        <div style="text-align: center;margin-top: 1em;">
          {{ new Date(post.created).toUTCString() }}
        </div>
    </article>
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
@keyframes anim {
    0%{
        transform: scale(1,1);
    }
    50%{
        transform: scale(1.1,1.1);
    }
    100%{
        transform: scale(1,1);
    }
}
.post{
    display: flex;
    flex-direction: column;
    border-radius: 0.4em;
    background-color: #d4ff009e;
    padding: 0.8em 0.4em;
    gap: 0.2em;
    cursor: pointer;
    &__head{
    transition: all ease-in 100ms;
      position: relative;
      width: 250px;
      height: 300px;
      overflow: hidden;
      border-radius: 0.4em;
    }
    &__image{
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
      top:0;
      left:0;
      object-position: center;
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
      text-align: center;
      width: 100%;
    }
    &__footer{
      display: flex;
      margin-top: 1em;
      flex-direction: row-reverse;
      justify-content: center;
      align-items: center;
      gap: 0.4em;
    }
    &__like-btn{
      animation: anim 400ms 1;
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
  .overflow_disable{
    overflow: hidden;
  }
  
  .open{
    position: absolute;
    top:50%;
    left: 50%;
    transform: translate(-50%,-50%);
    z-index: 100;
    width: calc(100% - 0.8em);
    height: 100vh;
    transition: all ease-in 100ms;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.6);
    &__post{
      width: 50%;
      height: 60%;
    }
  }
  .hide{
    display: none;
  }

</style>