<script setup>
import vNavBar from './UI/v-NavBar.vue';
import vFooter from './UI/v-Footer.vue';

</script>

<template>
    <img src="../assets/back.jpg" class="back_img">
  <vNavBar/>
  <div class="body">
    <div class="body__content">
        <slot></slot>
    </div>
  </div> 
  <vFooter/>
</template>

<style scoped lang="scss">

@import "../scss/variables.scss";
.back_img{
    position: fixed;
    width: 100%;
    height: 100vh;
    left: 0;
    top: 0;
    object-fit: cover;
    z-index: -1;
}
.body{
  overflow: hidden;
  display: flex;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  justify-content: center;
  align-items: center;
  background-color: rgba($color: #000000, $alpha: 0.6);
  &__content{
    margin-top: 80px;
    width: 100%;
    min-height: calc(90vh - 1.2em);
    padding: 0.6em;
    background-color: rgba($color: #000000, $alpha: 0.8 );
  }
}
</style>
