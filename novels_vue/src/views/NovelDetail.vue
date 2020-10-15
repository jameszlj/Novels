<template>
  <div id="NovelDetail">
    <Header />
    <b-container v-if="items.detailItems.length == 1">
      <b-row class="mt-3">
        <b-col>
          当前路径：<a href="/">首页</a>
          ><a :href="'/novel/'+items.detailItems[0].book_id">{{ items.detailItems[0].book_name}}</a>
          >{{items.detailItems[0].detail_title}} 
        </b-col>
      </b-row>
      <b-row class="mt-3 mb-3">
        <b-col id="book_detail_title">{{items.detailItems[0].detail_title}}</b-col>
      </b-row>
      <b-row class="mb-3">
        <b-col class="normal-center " cols="4" md="4"  v-if="items.detailItems[0].before_sort_id == ''">
            <a :href="'/novel/'+ items.detailItems[0].book_id ">上一页</a>
        </b-col>
        <b-col class="normal-center" cols="4" md="4"  v-else>
            <a :href="'/novel/'+ items.detailItems[0].book_id +'/'+ items.detailItems[0].before_sort_id">上一页</a>
        </b-col>
        <b-col class="normal-center" cols="4" md="4">
            <a :href="'/novel/'+ items.detailItems[0].book_id">返回目录</a>
        </b-col>

        <b-col class="normal-center" cols="4" md="4" v-if="items.detailItems[0].next_sort_id == ''">
            <a :href="'/novel/'+ items.detailItems[0].book_id  ">下一页</a>
        </b-col>
        <b-col class="normal-center" cols="4" md="4" v-else>
            <a :href="'/novel/'+ items.detailItems[0].book_id +'/'+ items.detailItems[0].next_sort_id">下一页</a>
        </b-col>
      </b-row>

      <b-row>
        <b-col>
          <p id="content-text" v-html="replacebr(items.detailItems[0].detail_content)"></p>
        </b-col>
      </b-row>

      <b-row class="mb-3">
        <b-col class="normal-center " cols="4" md="4"  v-if="items.detailItems[0].before_sort_id == ''">
            <a :href="'/novel/'+ items.detailItems[0].book_id ">上一页</a>
        </b-col>
        <b-col class="normal-center" cols="4" md="4"  v-else>
            <a :href="'/novel/'+ items.detailItems[0].book_id +'/'+ items.detailItems[0].before_sort_id">上一页</a>
        </b-col>
        <b-col class="normal-center" cols="4" md="4">
            <a :href="'/novel/'+ items.detailItems[0].book_id">返回目录</a>
        </b-col>

        <b-col class="normal-center" cols="4" md="4" v-if="items.detailItems[0].next_sort_id == ''">
            <a :href="'/novel/'+ items.detailItems[0].book_id  ">下一页</a>
        </b-col>
        <b-col class="normal-center" cols="4" md="4" v-else>
            <a :href="'/novel/'+ items.detailItems[0].book_id +'/'+ items.detailItems[0].next_sort_id">下一页</a>
        </b-col>
      </b-row>
    </b-container>
    <b-container v-else>
      你要查询的图书章节不存在啦
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import { reactive } from '@vue/composition-api'
import { GetInfoPost } from '../apis/read.js'
import { replacebr } from '../utils/replaceBr.js';

export default {
  name: "NovelDetail",
  components:{
    Header,
    Footer
  },
  setup(props,context){
    const detailParams = reactive({
      url: context.root.$route.path,
      key:''
    })

    const items = reactive({
      detailItems:[]
    })
    GetInfoPost(detailParams).then(resp =>{
      console.log("detail data", resp.data.data)
      items.detailItems = resp.data.data
    })

    return {
      items,
      replacebr
    }
  }
}
</script>

<style lang="scss" scoped>
#book_detail_title{
  text-align: center;
  font-size: 28px;
}
#content-text{
  line-height: 40px;
  font-size: 18px;
}
</style>