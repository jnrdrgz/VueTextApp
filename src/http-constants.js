import axios from 'axios'

let baseURL
baseURL = 'http://127.0.0.1:5000/'

export const HTTP = axios.create({baseURL:baseURL})

export const loginRoutine = (user, password) => new Promise(
		(resolve, reject) => {
			axios({url: baseURL+"login", data: user, password, method: 'POST' })
			.then(resp => {
				const token = resp.data.access_token
				localStorage.setItem('user-token', token)
				localStorage.setItem('user-id', resp.data.user_id)
				resolve(resp)
			})
			.catch(err => {
				localStorage.removeItem('user-token')
				reject(err);
			})
		}
	)

export const registerRoutine = (user, password) => new Promise(
		(resolve, reject) => {
			axios({url: baseURL+"register", data: user, password, method: 'POST' })
			.then(resp => {
				resolve(resp)
			})
			.catch(err => {
				reject(err);
			})
		}
	)

export const getTextRoutine = () => new Promise(
		(resolve, reject) => {
			axios({url: baseURL+"text", headers:{"Authorization" : "Bearer " + localStorage.getItem('user-token') }, method: 'GET' })
			.then(resp => {
				resolve(resp)
			})
			.catch(err => {
				reject(err);
			})
		}
	)

export const deleteTextRoutine = (text_id) => new Promise(
		(resolve, reject) => {
			let r = confirm("Are you sure?");
			if(r){
				axios({url: baseURL+"text/"+text_id, headers:{"Authorization" : "Bearer " + localStorage.getItem('user-token') }, method: 'DELETE' })
				.then(resp => {
					resolve(resp)
				})
				.catch(err => {
					reject(err);
				})
			}
		}
	)

export const postTextRoutine = (user_id, text) => new Promise(
		(resolve, reject) => {
			axios({url: baseURL+"text", headers:{"Authorization" : "Bearer " + localStorage.getItem('user-token') }, data: user_id, text, method: 'POST' })
			.then(resp => {
				resolve(resp)
			})
			.catch(err => {
				reject(err);
			})
		}
	)


export const getTrendsRoutine = () => new Promise(
		(resolve, reject) => {
			axios({url: baseURL+"trends", method: 'GET' })
			.then(resp => {
				resolve(resp)
			})
			.catch(err => {
				reject(err);
			})
		}
	)

