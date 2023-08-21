<script setup>
import BaseComponent from './BaseComponent.vue'
import { useStore } from 'vuex'
import { ref } from 'vue'
import Button from './UI/v-button.vue'
import { useRouter } from 'vue-router'

const route = useRouter()
const user = ref(useStore().state.user) 
</script>

<template>
  <BaseComponent>
      <div v-if="!user.name" class="text">
          <div>
            You can log in or create your account!
          </div>
          <div style="display: flex; gap: 1em;">
            <Button v-on:click="route.push({path:'/sign-in/'})">Sign In</Button>
            <Button v-on:click="route.push({path:'/sign-up/'})">Sign Up</Button>
          </div>
      </div>
      <div v-else class="text">
          Hello, {{ user.name }}
      </div>
  </BaseComponent>
</template>

<style scoped lang="scss">
  .text{
    width: 100%;
    font-size: 36px;
    height: calc(100vh - 200px);
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .body__content{
    margin-top: 0;
  }
</style>
