console.log("getting the IP");
counter=1;

function count_visits() {
    let x=fetch('https://api.ipify.org?format=json').then(del=>del.json()).then(ip_x=>ip_x.ip);
sessionStorage.setItem("x_host",x);
return 1;

}

function total_visits(){
let sum=0;
if (sessionStorage.getItem("x_host")) {
      counter++;
    console.log(counter);
}
  
}

total_visits();