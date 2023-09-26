let count_x=document.getElementById("count_x");
let router_ip=fetch('https://api.ipify.org?format=json').then(del=>del.json().then(ip_x=>ip_x.ip))
window.sessionStorage.setItem('client_sessionhost',router_ip);


var count=0;
fetch('https://api.ipify.org?format=json').then(del=>del.json()).then(evol=>{

if (router_ip===window.sessionStorage.getItem('client_sessionhost')) {
    count_x.innerHTML=count;
} else {
    count_x.innerHTML=count+1;
}
  console.log(evol.ip);
//count_x.innerHTML=evol.ip;
});

