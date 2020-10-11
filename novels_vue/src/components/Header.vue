<template>
  <b-container id="Header">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">咪小说</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item v-for="item in headData.headers" :key="item.id" :href="item.url">{{item.text}}</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="输入小说名字或者作者"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </b-container>
</template>

<script>
import { GetCates } from '../apis/read.js'
import { reactive, ref } from "@vue/composition-api" // ref 定义常量； reactive 定义对象

export default {
  name: 'Header',
  setup(props, context) {
    const headData = reactive({
      headers : []
    })
    GetCates().then(response =>{
      // console.log("in header components res==>",response.data.data)
      headData.headers = response.data.data
      // console.log("headData.headers ==>",headData.headers)
    })
    return {
      headData
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
