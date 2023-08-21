<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router';
import { useStore } from "vuex"


const store = useStore()


const burger_active = ref(false);
const user = ref(store.state.user)


const open_menu = () =>{
    window.scroll({
        top: 0,
        left: 0,
        behavior: "smooth",
    });
    if (burger_active.value === false){
        document.body.style.overflow = "hidden";
    }
    else{
        document.body.style.overflow = "auto";
    }
    burger_active.value = !burger_active.value;

}

</script>

<template>
    <header class="header">
        <div class="header__container">
            <div class="header__logo"><router-link :to="{name:'Home'}">Post App</router-link></div>
            <div class="header__posts"><router-link :to="{name:'Posts'}">All Posts</router-link></div>
            <div class="header__reg" v-if="!user.name">
                <div class="log-up"><router-link :to="{name: 'sign-up'}">SignUp</router-link></div>
                <div class="log-in"><router-link :to="{name:'sign-in'}">SignIn</router-link></div>
            </div>
            <div class="header__reg" v-else>
                <router-link :to="{name: 'sign-up'}">Liked</router-link>
                <router-link :to="{name: 'sign-up'}">{{ user.name }}</router-link>
                <div class="log-up"><a href="" v-on:click="store.dispatch('logout')">Logout</a></div>
            </div>
            <div class="burger__btn" @click="open_menu()" :class="{burger__btn_active: burger_active}"><span></span></div>
        </div>
    </header>
    <div class="header__reg_burger" >
        <div class="burger__row" :class="{burger__row_active: burger_active}">
            <a href="">All Posts</a>
            <div style="display: flex;flex-direction: column;" v-if="!user.name">
                <router-link :to="{name: 'sign-up'}">SignUp</router-link>
                <router-link :to="{name:'sign-in'}">SignIn</router-link>
            </div>
            <div style="display: flex;flex-direction: column;" v-else>
                <router-link :to="{name: 'sign-up'}">Liked</router-link>
                <router-link :to="{name: 'sign-up'}">{{ user.name }}</router-link>
                <a href="" v-on:click="store.dispatch('loguot')">Logout</a>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
@import "../../scss/variables.scss";

.header {
    width: 100%;
    height: 80px;
    position: fixed;
    z-index: 100;
    background-color: $colorGrey;
    &__container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 80px;
        padding: 0px 20px;
    }
    &__posts{
      transition: all ease 400ms;
    }
    &__posts a{
      color: #d4ff009e;
      font-size: 24px;
      text-decoration: none;
      font-weight: 800;
    }
    &__posts:hover a{
      color: #3e3e3e;
    }
    &__posts:hover{
      transform: scale(1.2,1.2);
    }
    &__logo {
      a{
        text-decoration: none;
        color: $colorOrange;
      }
        font-size: 36px;
    }
    &__reg {
        display: flex;
        gap: 1em;
        align-items: center ;
        a{
          text-decoration: none;
          color: $colorDarkOrange;
          transition: 300ms;
        }
        a:hover{
          color: $colorOrange;
        }
        *{
            font-size: 24px;
        }
    }
    &__reg_burger{
        display: none;
        align-items: center;
        *{
            font-size: 32px;
        }
    }
    *{
        font-family: $fontES;
    }
}
.burger__btn{
    display: none;
}
.newcolor{
    color: $colorOrange;
}
@media (max-width:581px) {
    .header{
        &__reg{
            display: none;
        }
        &__posts{
            display: none;
        }
        &__reg_burger{
            display: block;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    }
    .burger{
        &__row{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            min-height: 100vh;
            position: relative;
            bottom: 0;
            z-index: 10;
            background-color: #000000;
            transform: translateY(-100%);
            transition: transform 300ms;
            & div{
                margin-bottom: 20px;
            }
            & div:last-child{
                margin-bottom: 0px;
            }
            &_active{
                transform: translate(0);
            }
            a{
                width: 200px;
                text-align: center;
                color: white;
                text-decoration: none;
                margin-bottom: 0.5em;
                border-left: 2px #fff solid;
                border-right: 2px #fff solid;
            }
        }
        &__btn{
            display: block;
            position: relative;
            width: 30px;
            height: 16px;
            cursor: pointer;
            &::before{
                content: '';
                transition: all 300ms;
                left: 0;
                top: 0;
                position: absolute;
                height: 10%;
                width: 100%;
                background-color: #fff;
            }
            &::after{
                content: '';
                transition: all 300ms;
                left: 0;
                bottom: 0;
                position: absolute;
                height: 10%;
                width: 100%;
                background-color: #fff;
            }
            & span{
                transition: all 300ms;
                left: 0;
                top: 50%;
                transform: scale(1) translate(0px, -50%);
                position: absolute;
                height: 10%;
                width: 100%;
                background-color: $colorDarkOrange;
            }
        }
        &__btn_active{
            &::before{
                transform: rotate(-45deg);
                top: 8px;
            }
            &::after{
                content: '';
                transform: rotate(45deg);
                bottom: 6px;
            }
            & span{
                transform: scale(0) translate(0px, -50%);
            }
        }
    }
}
</style>