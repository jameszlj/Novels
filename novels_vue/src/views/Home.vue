<template>
  <div class="home">
    <Header />

    <b-container>
      <b-carousel
      id="carousel-1"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      class="mb-2">
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=52"></b-carousel-slide>
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54"></b-carousel-slide>
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>
      </b-carousel>

      <b-row class="mb-2">
        <b-col><h4 style="color:blue">最新推荐Top5</h4></b-col>
      </b-row>  

      <b-row>
        <b-col class="normal-center" cols="12" md="2" v-for="item in  items.top5NewItems" :key="item.book_id">
          <!-- <b-card fluid no-body :img-src="item.image_urls" img-alt="Image" img-top>
            <template v-slot:header >
              <a :href="'/novel/'+item.book_id" class="text-muted">{{ item.book_name }}</a>
            </template>
          </b-card> -->
          <b-img thumbnail fluid :src="item.image_urls" alt="image"></b-img>
          <div >
            <a class="text-muted" :href="'/novel/'+item.book_id">{{ item.book_name }}</a>
          </div>
        </b-col>
      </b-row>

    </b-container>

    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import { reactive } from '@vue/composition-api'
import { GetInfoPost } from '../apis/read'

export default {
  name: 'Home',
  components: {
    Header,
    Footer
  },
  filters: {
    // 超出字体一行显示超出显示省略号
    ellipsis (value) {
      if (!value) return ''
      if (value.length > 9) {
        return value.slice(0,9) + '...'
      }
      return value
    }
  },
  setup(props,context) {
    const top5NewParams = reactive({
      url:'/novel/top',
      key:'top5_new'
    })
    const items = reactive({
      top5NewItems:[]
    })
    GetInfoPost(top5NewParams).then(resp =>{
      // console.log(resp.data.data)
      items.top5NewItems = resp.data.data
    })
    return {
      items
    }
  }

}
</script>
