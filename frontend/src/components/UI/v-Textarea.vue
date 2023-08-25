<script setup>
import { defineProps, defineEmits } from 'vue';


const properties = defineProps({
    type:String,
    name:String,
    placeholder:String
})

const emit = defineEmits(['inputHandler'])

console.log(properties)

</script>
<template>
    <textarea v-bind:placeholder="properties.placeholder"
           v-bind:name="properties.name"
           class="input" v-on:input="$emit('inputHandler')" ></textarea>
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
    max-width: 600px;
    max-height: 200px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
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