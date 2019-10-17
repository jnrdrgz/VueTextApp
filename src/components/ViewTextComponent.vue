<template>
	<!--for text in texts-->
	<div class="Texts">
			<div class="card" v-for="text in texts" :key="text.id">
				<div class="card-content">
					<div class="media">
						<div class="media-left">
							<figure class="image is-48x48">
								<img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
							</figure>
						</div>
						<div class="media-content">
							<!--{{text.username}}-->
							<p class="title is-4">{{text.username}}</p>
						</div>
					</div>
				<div class="content">
					<!--{{text.text}}-->
					{{text.text}}
					<br>
					<!--{{created on}}-->
					<time datetime="2016-1-1">{{text.texted_on}}</time>
					<br>
					<button v-if="user_id == text.user_id" v-on:click="delete_text(text.id)">DELETE</button>
				</div>
			</div>
		</div>
	</div>

</template>
<script>
	import {deleteTextRoutine} from '../http-constants'
	
	export default {
		name: "ViewTextComponent",
		props: ['texts'],
		data: () => ({
			user_id: localStorage.getItem('user-id')
		}),
		methods: {
			delete_text: function(uid) {
				deleteTextRoutine(uid)
				.then( () => {
					this.$router.go(0);
				})
				.catch( (err) => {
					console.log("Error")
					this.error = err
				})
			}
		}
	}	
</script>