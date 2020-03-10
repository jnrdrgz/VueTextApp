<template>
	<div class="Trends">
		<div class="has-background-primary has-text-white" id="trend">

			<!-- for trend in trends -->
			<h2><b>TRENDS</b></h2>
			<!--<div v-for="trend in trends" :key="trend.index">-->
			<div v-for="{ind, word} in trends" :key="ind">
				{{ind}} - {{word}}<br>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "TrendsComponent",
		props: ['trends'],
	}	
</script>

