<template>
	<div class="container">
		
		<div class="columns">
			<div class="column">
				<router-link :to="{name: 'RegisterComponent'}" class="button is-primary">Register</router-link><br>
				<router-link :to="{name: 'LoginComponent'}" class="button is-primary">Log In</router-link><br>
			<!-- first columns -->
			</div> 



			<div class="column is-three-fifths">
				<div class="Texts">

				<div class="columns">
					<div class="column">  
					</div>
					<div class="column is-three-fifths"> 
						<h1 class="title is-1">Register to Texts</h1> 
						<p v-if="error">{{error}}</p>
						<div class="field">
							<div class="control">
								<input class="input" type="text" placeholder="Username" v-model="username">
							</div>
						</div>
						<div class="field">
							<div class="control">
								<input class="input" type="password" placeholder="Passoword" v-model="password">
							</div>
						</div>

						<p class="control">
							<input class="button is-primary" type="submit" value="Log In" v-on:click="submit">
							
						</p>

					</div>
					<div class="column">  
					</div>
				</div>

				</div>
				

			<!-- center columns -->
			</div> 

			<div class="column">
			<!-- third columns -->
			</div>
		
		 <!-- columns -->
		</div> 
	<!-- conteiner -->
	</div>
</template>


<script>
	import {registerRoutine} from '../http-constants'
	export default {
		name: "RegisterComponent",
		data: () => ({
			username: '',
			password: '',
			error: ''
		}),
		methods: {
			submit: function() {
				const { username, password } = this;

				registerRoutine({username,password})
				.then( () => {
					this.$router.push('/') 
				})
				.catch( (err) => {
					console.log("Error")
					this.error = err
				})
			}
		}
	}
</script>