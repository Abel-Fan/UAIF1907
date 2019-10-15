<template>
  <div class="login">
      <div class="login-box">
          <div class="left">
              <div class="icon"></div>
          </div>
          <div class="right">
              <h6>用户登录</h6>
              <el-form :model="formData" :rules="formRules">
                    <el-form-item prop="username">
                        <el-input placeholder="用户名" v-model="formData.username"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                      <el-input placeholder="密码" v-model="formData.password"></el-input>
                    </el-form-item>
                    <el-form-item>
                      <el-button type="primary" style="width:100%;">登录</el-button>
                    </el-form-item>
              </el-form>
          </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'login',
    data:function(){
        return {
            formData:{
                username:"",
                password:"",
            },
            formRules:{
                username:[
                    {required:true,message:"用户名是必填的",trigger:"blur"},
                    { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                ],
                password:[]
            }
        }  
    },
    components: {
        // HelloWorld
    }
}
</script>
<style>
    .login{
        background-image:url("../../assets/bg.jpg");
        background-size:cover;
        width:100%;
        height:100%;
        overflow: hidden;
    }
    .login-box{
        width:550px;
        height:230px;
        position:fixed;
        top:0;
        bottom:0;
        left:0;
        right:0;
        margin:auto;
    }
    .login-box .left {
        width:240px;
        height:230px;
        overflow: hidden;
        border-right:1px solid #fff;
        float:left;
        box-sizing: border-box;
    }
    .login-box .left .icon{
        width:100%;
        height:175px;
        background:url("../../assets/login-icon.png");
        background-size:240px 175px;
        margin-top:27px;

    }
    .login-box .right{
        width:280px;
        float:right;
        padding-left:30px;
    }
    .login-box .right h6{
        color:#fff;
        font-size:16px;
        font-weight: 400;
        padding:10px 0;
        text-align: left;
    }
</style>
