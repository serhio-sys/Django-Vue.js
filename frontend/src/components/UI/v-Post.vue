<script setup>
import { defineProps, defineEmits, ref } from 'vue'
import { RouterLink } from 'vue-router';
import { useStore } from "vuex"
import { HTTP } from '../../api/axios';


const store = useStore()
const props = defineProps({
    post:Object
  })
const emit = defineEmits(['remove'])
const user = store.state.user
const post = ref()

if (props.post instanceof Array){
   post.value = props.post
}
else{
   post.value = Array(props.post)
}


const toggleBody = ref(false)
const bodyOverflowToggler = () => {
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
}


const sizeUpFunction = (e) => {
  e.target.parentNode.parentNode.classList.toggle("open")
  e.target.parentNode.classList.toggle("open__post")
  bodyOverflowToggler()
  e.target.parentNode.parentNode.querySelector('.post__readmore').classList.toggle("hide")
  
}

const LikeHandler = async (e) => {
    try{
        const response = await HTTP.post(`posts/like/${post.value[0].id}/`,{},{
            headers:{
                Authorization: `Token ${user.token}`
            }
        })
        if (response.status == 200){
            if (emit('remove',post.value[0].id)){
              return
            }
            if (post.value[0].liked.includes(user.name)){
              post.value[0].liked = post.value[0].liked.filter(item => {
                  return item != user.name
              })
              post.value[0].likes--
            }
            else{
              post.value[0].liked.push(user.name)
              post.value[0].likes++
            }
        }
    }
    catch(err){
        console.log(err)
    }
}

const deletePost = async () => {
  try{
    const response = await HTTP.delete(`posts/delete/${post.value[0].id}`, {
      headers:{
        Authorization: `Token ${user.token}`
      }
    })
    if (response.status === 204){
      emit('remove',post.value[0].id)
    }
  }
  catch(err){
    console.log(err)
  }
}

const showDialogDelete = (e) => {
  if (e.target.classList.contains("post_dialog")){
    e.target.classList.toggle("__show")
  }
  else if(e.target.parentNode.classList.contains("post__dialog-block")){
    e.target.parentNode.parentNode.classList.toggle("__show")
  }
  else{
    e.target.parentNode.querySelector(".post__dialog").classList.toggle("__show")
  }
  bodyOverflowToggler()  
}

</script>
<template>
    <article class="post">
        <div v-on:click="sizeUpFunction" class="post__head">
            <img v-if="post.image" class="post__image" />
            <img v-else src="../../../public/bg.png" class="post__image" /> 
            <div class="post__name">{{ post[0].name }}</div>
        </div>
        <div class="post__desc">{{ post[0].desc }}</div>
        <router-link class="post__readmore" :to="{name:'Home'}">Read More</router-link>
        <div class="post__footer">
            <div class="post__likes">{{ post[0].likes }}</div>
            <div v-if="post[0].author != user.id">
                <button v-if="!post[0].liked.includes(user.name)" v-on:click="LikeHandler" class="post__like-btn">Like</button>
                <button v-else v-on:click="LikeHandler" class="post__like-btn">Unlike</button>
            </div>
            <div v-else>
                Likes: 
            </div>    
        </div>
        <div style="margin: 0 auto; margin-top: 0.5em;" v-if="user.id == post[0].author">
          <button class="post__delete-btn" v-on:click="showDialogDelete">Delete</button>
          <div class="post__dialog" v-on:click.self="showDialogDelete">
            <h1>Are you really want to delete this post({{ post[0].name }})?</h1>
            <div style="display: flex;gap: 1em;position: relative; z-index: 10000;" class="post__dialog-block">
              <button class="post__delete-btn" v-on:click="deletePost">Yes</button>
              <button class="post__like-btn" v-on:click.stop="showDialogDelete">No</button>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 1em;">
          {{ new Date(post[0].created).toUTCString() }}
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
    &__dialog{
      position: absolute;
      top: -100%;
      left: 50%;
      transform: translate(-50%,-50%);
      background-color: rgba(0, 0, 0, 0.7);
      display: flex;
      flex-direction: column;
      gap: 1em;
      justify-content: center;
      align-items: center;
      width: 100%;
      z-index: 100;
      transition: 300ms all ease-in;
      height: 100vh;
    }
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
    &__like-btn, &__delete-btn{
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
    &__delete-btn{
      background-color: darkred;
    }
    &__delete-btn:hover{
      transform: scale(1.1,1.1);
      background-color: red;
    }
  }
  .overflow_disable{
    overflow: hidden;
  }
  .__show{
    top: 50%;
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