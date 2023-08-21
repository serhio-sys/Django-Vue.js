<script setup>
</script>
<template>
    <button class="btn"><slot></slot></button>
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
.btn{
    margin-top: 1em;
    width: 150px;
    padding: 0.4em 0.6em;
    outline: none;
    font-size: 18px;
    border-radius: 0.4em;
    color: $colorDarkOrange;
    border: none;
    cursor: pointer;
}
</style>