import Vue from 'vue'
import Router from 'vue-router'
import HomeComponent from '@/components/HomeComponent'
import RegisterComponent from '@/components/RegisterComponent'
import LoginComponent from '@/components/LoginComponent'

Vue.use(Router)

export default new Router({
	routes: [
		{
			path: "/",
			name: "HomeComponent",
			component: HomeComponent
		},
		{
			path: "/register",
			name: "RegisterComponent",
			component: RegisterComponent
		},
		{
			path: "/login",
			name: "LoginComponent",
			component: LoginComponent
		},
		{
			path: "/user/:id",
			name: "UserProfileComponent",
			component: UserProfileComponent
		}
	]
})