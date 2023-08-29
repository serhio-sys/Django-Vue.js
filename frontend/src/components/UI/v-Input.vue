<script setup>
import { defineProps, defineEmits } from 'vue';


const properties = defineProps({
    type:String,
    name:String,
    placeholder:String
})

const emit = defineEmits(['inputHandler'])


</script>
<template>
    <input v-bind:placeholder="properties.placeholder"
           v-bind:name="properties.name"
           v-bind:type="properties.type"
           class="input" v-on:input="$emit('inputHandler')" />
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
@keyframes anim{
    0%{
        background-size: 0% 2px;
    }
    100%{
        background-size: 100% 2px;
    }
}
.input{
    color: gray;
    background: transparent;
    background-image: linear-gradient(currentcolor,currentcolor);
    background-repeat: no-repeat;
    background-size: 100% 2px;
    outline: none;
    border: none;
    font-size: 18px;    
    padding: 0.3em 0.5em;
    transition: all ease-in 300ms;
    background-position: 0% 100%;
}
.input:focus{
    background-image: linear-gradient(to right, white,lightgray);
    background-size: 100% 2px;
    animation: anim 400ms 1;
    color: white;
}
</style>