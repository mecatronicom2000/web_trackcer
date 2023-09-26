const lib1=require('./js1.js');
const lib2=require('os');
const lib3=require('fs');
const lib4=require('./js4.js');
const { log } = require('console');
console.log(lib1['display_s']);
console.log('display memoy size ',lib2.totalmem(),'MB');



/**
 * 
 * 
let cross=lib3.readFileSync("./");
lib3.readdir('./',function(err,file) {
    if (cross) {
        console.log('file found named as',file);
    } else {
        console.log('error code',err);
    }
    
})
 * 
 * 
 */