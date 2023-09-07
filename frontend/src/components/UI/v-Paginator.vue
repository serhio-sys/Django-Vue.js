<script setup>
import { defineEmits, defineProps } from 'vue'

const props = defineProps({
    maxPages:Number,
    currentPage:Number,
})

const emit = defineEmits(['changePage'])


</script>
<template>
<div class="paginator">
    <div class="paginator__numbers">
        <div v-for="i in maxPages" v-on:click="(event) => emit('changePage',event)"><button v-if="currentPage==i" class="paginator__index selectedPage">{{ i }}</button><button class="paginator__index" v-else>{{ i }}</button></div>
    </div>
</div>
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
.paginator{
    display: flex;
    gap: 0.2em;
    &__numbers{
      display: flex;
      gap: 0.5em;
    }
    &__index{
      cursor: pointer;
      padding: 0.6em 1em;
      color: white;
      background-color: rgba($color: #000000, $alpha: 0.6);
      border: 2px solid white;
      border-radius: 0.4em;
      transition: 300ms ease-in all;
    }
    &__index:hover{
      background-color: white;
      color: black;
    }
  }
  .selectedPage{
    background-color: white;
    color: black;
  }
</style>