<template>
  <div id="NovelIndex">
    <Header />
    <b-container class="mt-4" v-if="items.indexItems.length == 1">
      <b-row class="mb-3">
        <b-col cols="12" md="4">
          <b-img thumbnail fluid style="width:80%; margin-left:10%" :src="items.indexItems[0].image_urls" alt="Image 1">
          </b-img>
        </b-col>
        <b-col cols="12" md="8">
          <b-jumbotron header-level="0" class="pt-3">
            <template v-slot:header class="mt-1 mb-3">{{ items.indexItems[0].book_name }}</template>

            <div class="mb-3">作者：{{ items.indexItems[0].book_author }}</div>
            <div class="mb-3">最新章节：{{ items.indexItems[0].book_newest_name }}</div>
            <div class="mb-3">最新更新时间：{{ items.indexItems[0].book_last_update_time }}</div>
            <div class="mb-3">本书状态：{{ items.indexItems[0].book_status }}</div>
            <hr class="my-4">

            <p v-text="items.indexItems[0].book_desc">
            </p>

            <b-button variant="primary" class="left" :href="'/novel/'+items.indexItems[0].book_id+'/'+items.cap20Items[0].sort_id" :v-if="items.cap20Items.length == 1" style="float:left;margin-lefg:5px" >开始阅读</b-button>
            <b-button variant="success" class="right" href="#" style="float:right;margin-lefg:5px">加入收藏</b-button>
          </b-jumbotron>
        </b-col>
      </b-row>

      <b-row class="mb-2">
        <b-col><h6>最新更新的20章图书</h6></b-col>
      </b-row>

      <b-row class="mb-4">
        <b-col cols="12" md="4" v-for="item in items.cap20Items" :key="item.id">
          <a :href="'/novel/'+item.book_id+'/'+item.sort_id">{{item.detail_title}}</a>
        </b-col>
      </b-row>

      <b-row class="mb-2">
        <b-col><h6>所有章节的内容</h6></b-col>
      </b-row>

      <b-row class="mb-2">
        <b-col cols="12" md="4" v-for="item in items.capAllItems" :key="item.id">
          <a :href="'/novel/'+item.book_id+'/'+item.sort_id">{{item.detail_title}}</a>
        </b-col>
      </b-row>
    </b-container>
    <b-container v-else>
      哦哦，您要查看的图书不存在
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import { ref, reactive} from "@vue/composition-api"
import { GetInfoPost } from "../apis/read.js"

export default {
  name:"NovelIndex",
  components:{
    Header,
    Footer
  },
  setup(props,context){
    const now_url = ref(context.root.$route.path)

    const indexParams = reactive({
      url: now_url.value,
      key:'index'
    })
    const cap20Params = reactive({
      url: now_url.value,
      key:'cap20'
    })
    const capAllParams = reactive({
      url: now_url.value,
      key:'all'
    })

    const items = reactive({
      indexItems:[],
      cap20Items:[],
      capAllItems:[]
    })
    GetInfoPost(indexParams).then(resp => {
      // console.log("in novelindex  index data:",resp.data.data)
      items.indexItems = resp.data.data
    })
    GetInfoPost(cap20Params).then(resp => {
      // console.log("in novelindex cap20 data:",resp.data.data)

      items.cap20Items = resp.data.data
    })
    GetInfoPost(capAllParams).then(resp => {
      // console.log("in novelindex cap all data:",resp.data.data)
      items.capAllItems = resp.data.data
    })
    return {
      items
    }
  }
}
</script>

<style lang="scss" scoped>
  
</style>