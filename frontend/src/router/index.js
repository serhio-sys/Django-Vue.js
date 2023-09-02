import { createRouter, createWebHistory } from 'vue-router'
import { isAuthenticated } from '../utils/utils'
import App from '../components/HomeComponent.vue'
import PostsComponent from '../components/PostsComponent.vue'
import SignInComponent from '../components/SignInComponent.vue'
import SignUpComponent from '../components/SignUpComponent.vue'
import CreatePostComponent from '../components/CreatePostComponent.vue'
import LikedComponent from '../components/LikedComponent.vue'
import UserPostsComponent from '../components/UserPostsComponent.vue'

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
        component: CreatePostComponent,
        meta: {
            requiresAuth: true,
        },
    },
    {
        path: "/liked/",
        name: "liked",
        component: LikedComponent,
        meta: {
            requiresAuth: true,
        },
    },
    {
        path: "/my-posts/",
        name: "my-posts",
        component: UserPostsComponent,
        meta: {
            requiresAuth: true,
        },
    }
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

router.beforeEach((to,from,next) => {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (!isAuthenticated()) {
            router.push({ path: '/sign-in/'})
        }
        else{
            next()
        }
    } else {
        next()
    }
})

export default router;