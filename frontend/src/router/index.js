import { createRouter, createWebHistory } from 'vue-router'
import App from '../components/HomeComponent.vue'
import PostsComponent from '../components/PostsComponent.vue'
import SignInComponent from '../components/SignInComponent.vue'
import SignUpComponent from '../components/SignUpComponent.vue'
import CreatePostComponent from '../components/CreatePostComponent.vue'

const routes = [
    {
        path: "/",
        name: "Home",
        component: App
    },
    {
        path: "/posts/",
        name: "Posts",
        component: PostsComponent
    },
    {
        path: "/sign-in/",
        name: "sign-in",
        component: SignInComponent
    },
    {
        path: "/sign-up/",
        name: "sign-up",
        component: SignUpComponent
    },
    {
        path: "/create-post/",
        name: "create-post",
        component: CreatePostComponent
    }
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;