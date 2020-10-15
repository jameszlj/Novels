export function replacebr(str) {
  return str.replace(/\s+|&nbsp;/gi,"<br/>")
}

// /gi(全文查找、忽略大小写)
