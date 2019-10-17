<template>
	<div>
		<div class="field">
			<textarea class="textarea has-fixed-size" placeholder="TeXT sOmething" rows="3" maxlength="140" id="text-area" v-model="text"></textarea>
		</div>

		<div class="field is-grouped is-grouped-right">
			<p class="control" id="text-length">140</p>
			<p class="control">
				<button class="button is-primary" v-on:click="submit">
					Submit
				</button>
			</p>
		</div>
	</div>

</template>

<script>
	import {postTextRoutine} from '../http-constants'

	export default {
		name: "NewTextComponent",
		data: () => ({
			text: '',
		}),
		watch: {
			text: function(){
				let text_area =  document.getElementById("text-area");
				let ln = document.getElementById("text-length")
				ln.innerHTML = 140 - text_area.value.length
			}
		},
		methods: {
			submit: function() {
				const { text } = this;
				const user_id = localStorage.getItem('user-id');
				postTextRoutine({user_id, text})
				.then( () => {
					this.$router.go(0); 
				})
				.catch( (err) => {
					console.log("Error")
					this.error = err
				})
			},
			
		}
	}
	
</script>