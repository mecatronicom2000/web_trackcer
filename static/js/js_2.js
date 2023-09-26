console.log("welcome to my file");

window.localStorage.setItem('color_1','#FF000000');
window.localStorage['color_2']='#005500AA';
window.localStorage['bkg']='#005500AA';
const vistors=document.getElementById("v_result");


var drag_me=false;
var model_img=document.querySelector("#model_img");

const counter_area=document.querySelector("#counter_area");
var brand_style=document.querySelector("#brand_style");
var model_color=document.querySelector("#model_color"),
count_x=document.querySelector("#count_x"),
v_result=document.querySelector("#v_result");
let target_col=document.querySelectorAll("ol li");

  function change_the_bk(color_x) {
    window.localStorage.setItem('counter_bkg',color_x)

    counter_area.style.backgroundColor=window.localStorage.setItem("bkg_model",document.getElementById("model_color").value);
   document.getElementById("contacts").style.background=model_color.value;
    
  }
  
  function change_brand() {
    brand_style.src=URL.createObjectURL(model_img.files[0]);
    console.log("display img");
    console.log(model_img.files[0]);
  }
  



    target_col.forEach(
        li => {
        li.addEventListener("click",(e)=>{
            console.log(e.currentTarget.dataset.color);console.log("displayed");
        target_col.forEach((li) => {
            li.classList.remove('active');
        });
        e.currentTarget.classList.add('active');
        window.localStorage.setItem('target_col',e.currentTarget.dataset.color);
        counter_area.style.backgroundColor=window.localStorage.getItem('target_col');
        })
    });
    if (window.localStorage.getItem('target_col')) {
        console.log("good");
        counter_area.style.backgroundColor=window.localStorage.getItem('target_col');
    } else {
        console.log("not good");
        counter_area.style.backgroundColor=window.localStorage.getItem('target_col');
        
    }



































console.log(vistors);




count_visits();
function count_visits(){
    let c_visits;
    if (!localStorage.getItem('c_visits')) {
        console.log("c_visits not found....creating a one");
        console.log(localStorage.setItem('c_visits',1));
    } else {
        console.log("Permission Disabled");
    }
    c_visits=+localStorage.getItem('c_visits');
    const const_c_visits=c_visits+1;
    localStorage.setItem('c_visits',const_c_visits);
console.log("current count item :"+const_c_visits);
vistors.innerHTML=const_c_visits;

function send_visits_value() {

    return const_c_visits
}


} 

/*
count=localStorage.getItem('c_visits')
function counter_func(e) {
    let var_count=e.dataset.goal;
    let auto_count=setInterval(()=>{
        e.textContent++;
        if (e.textContent==localStorage.getItem('c_visits')) {
            clearInterval(auto_count);
            console.log(auto_count);
            e.value=auto_count
        }
    },100)
    
}
counter_func(count);
*/


