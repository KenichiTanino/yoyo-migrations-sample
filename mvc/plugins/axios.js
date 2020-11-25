
export default ({ $axios }) => {
  //baseURL: process.env.API_URL
 
  // リクエストログ
  $axios.onRequest((config) => {
   console.log(config)
  })
  // レスポンスログ
  $axios.onResponse((config) => {
   console.log(config)
  })
  // エラーログ
  $axios.onError((e) => {
   console.log(e.response)
  })
}
