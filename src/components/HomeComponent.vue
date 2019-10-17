<template>
	<div class="container">
		
		<div class="columns">
			<div v-if="texts" class="column">

			<a class="button is-primary">Home</a><br>
			<a class="button is-primary">Profile</a><br>
			<button class="button is-primary" onclick="localStorage.removeItem('user-token');location.reload();">Log Out</button>

			</div>

			<div v-else class="column">
				<router-link :to="{name: 'RegisterComponent'}" class="button is-primary">Register</router-link><br>
				<router-link :to="{name: 'LoginComponent'}" class="button is-primary">Log In</router-link><br>
				

			<!-- first columns -->
			</div> 



			<div class="column is-three-fifths">
				<section class="hero is-primary">
				<div class="hero-body">
					<h1 class="title">
					  TEXT
					</h1>
					<h2 class="subtitle">
						A test app made in Vue with a Flask API in the backend
					</h2>
				</div>
				</section>

				<!-- v-if text -->
				<NewTextComponent/>
				<ViewTextComponent :texts="texts"/>
				<!-- v-if text -->
				

			<!-- center columns -->
			</div> 
			

			<div class="column">
				<SearchComponent/>
				<br>
				<TrendsComponent/>
				<br>
				<UsersComponent/>
				

			<!-- third column -->
			</div>		
		 <!-- columns -->
		</div> 

	<!-- conteiner -->
	</div>
</template>

<script>
	import {getTextRoutine} from '../http-constants'
	import NewTextComponent from './NewTextComponent.vue'
	import ViewTextComponent from './ViewTextComponent.vue'
	import SearchComponent from './SearchComponent.vue'
	import TrendsComponent from './TrendsComponent.vue'
	import UsersComponent from './UsersComponent.vue'
	
	export default {
		name: "HomeComponent",
		components: {
			NewTextComponent,
			ViewTextComponent,
			SearchComponent,
			TrendsComponent,
			UsersComponent,
			//
		}, 
		data() {
			return {
				texts: ""
			}
		},
		mounted () {
			getTextRoutine().then( (r) => {
					this.texts = r.data
				})
				.catch( (err) => {
					console.log(err)
				})
		},
	}


</script>