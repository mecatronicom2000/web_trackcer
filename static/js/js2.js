console.log("welcome to my file");

window.localStorage.setItem('color_1','#FF000000');
window.localStorage['color_2']='#005500AA';


const vistors=document.getElementById("v_result");
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
}


