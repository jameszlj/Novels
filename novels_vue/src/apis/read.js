import service from "../utils/request.js"


export function GetCates() {
  return service.request({
    method: 'get',
    url: "/novel_cate"
  })
}

export function GetInfoPost(postParms){
  return service.request({
    method: "post",
    url:postParms.url,
    data:{
      key:postParms.key,
      secretKey:"" //预留字段给加密用
    }
  })
}