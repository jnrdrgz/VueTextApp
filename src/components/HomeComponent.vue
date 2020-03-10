<template>
	<div class="container">
		
		<div class="columns">
			<div v-if="texts" class="column">

			<a class="button is-primary">Home</a><br>
			<router-link :to="{ name: 'UserProfileComponent', params: { id: 123 }}" class="button is-primary">Profile</router-link><br>
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
				<div v-if="texts">
					<NewTextComponent/>
					<ViewTextComponent :texts="texts"/>
				</div>
				<div v-else>
					Log in or sing up to see other people texts!!!
				</div>

				<!-- v-if text -->
				

			<!-- center columns -->
			</div> 
			

			<div class="column">
				<SearchComponent/>
				<br>
				<TrendsComponent :trends="trends"/>
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
	import {getTextRoutine, getTrendsRoutine} from '../http-constants'
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
		data () {
			return {
				texts: "",
				trends: "",
			}
		},
		mounted () {

			getTextRoutine().then( (r) => {
					this.texts = r.data
					//console.log(this.texts)

				})
				.catch( (err) => {
					console.log(err)
				});
			
			getTrendsRoutine().then( (r) => {
					this.trends = r.data
				})
				.catch( (err) => {
					console.log(err)
				});

		},
	}


</script>