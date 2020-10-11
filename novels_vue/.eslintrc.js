module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ['plugin:vue/essential', 'eslint:recommended', '@vue/prettier'],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    //严格的检查缩进问题，不是报错，我们可以关闭这个检查规则,然后在终端输入npm run dev
    "indent": ["off", 2],
    //使用eslint时，严格模式下，报错Missing space before function parentheses的问题，意思是在方法名和刮号之间需要有一格空格。
    'space-before-function-paren': 0,
    //关闭prettier
    "prettier/prettier": "off",
    // 未引用参数报错
    "no-unused-vars": 0,

    // allow debugger during development
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',

    // //空行最多不能超过100行
    // "no-multiple-empty-lines": [0, { "max": 100 }],
    // //关闭禁止混用tab和空格
    // "no-mixed-spaces-and-tabs": [0],
    // 句末加分号，状态：关闭
    // 'semi': ["off"],
  }
}
