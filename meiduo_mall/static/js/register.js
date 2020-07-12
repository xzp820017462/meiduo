let vm = new Vue({
    el: "#app",
    data:{
        username:"",
        password:"",
        password2:"",
        mobile:"",
        allow:"",
        image_code_url:'',
        uuid:'',
        error_name:false,
        error_password:false,
        error_password2:false,
        error_mobile:false,
        error_allow:false,
        error_name_message:'',
        error_mobile_err_message:'',
    },
    mounted(){
        this.generate_image_code();
    },
    methods:{
        generate_image_code(){
            this.uuid = this.generateUUID();
            this.image_code_url='/image_codes/'+this.uuid+'/';
        },
        //check username
        check_username(){
        let re = /^[a-zA-z0-9_-]{5,20}$/;
        if (re.test(this.username)){
            this.error_name = false;
        }else{
            this.error_name_message = '请输入5-20个字符的用户名';
            this.error_name_message = true;
              },
        if (this.error_name == false){
            let url = '/username/'+this.username+'/count/';
            axios.get(url,{
                responseType:'json';
            })
            .then(response =>{
                if(response.data.get.count == 1){
                    this.error_name_message ='username is create';
                    this.error_name = true;
                }else{
                    this.error_name = false;
                }
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        },

    check_password(){
        let re = /^[0-9a-zA-Z]{8,20}$/;
        if (re.test(this.password)){
            this.error_password = false;
        }else{
            this.error_password = true;
        }
    },

    check_password2(){
        if (check_password2 != check_password){
            this.error_password2 = true;
        }else{
            this.error_password2 = false;
        }
    },
    check_mobile(){
    let re /^1[345789]\d{9}$/;
    if (re.test(this.mobile)){
        this.error_mobile = false;
    }else{
        this.error_mobile_message = '您输入的手机号格式不正确';
        this.error_mobile true;
    }
    },
    check_allow(){
    if (!this.allow){
        this.error_allow=true;
    }else{
        this.error_allow=false;
    }
    },
    on_submit(){
            this.check_username();
            this.check_password();
            this.check_password2();
            this.check_mobile();
            // this.check_sms_code();
            this.check_allow();

            if (this.error_name_message == true || this.error_password == true || this.error_password2 == true
                || this.error_mobile == true ||  this.error_allow == true) {
                // 不满足注册条件：禁用表单
                window.event.returnValue = false;
            }
        }
}
})