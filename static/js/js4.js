const http_req=require('http');
const fs=require('fs');
const port=3000;
const server_x=http_req.createServer(function (req,res) {
    res.writeHead(200,{'Content-type':"text/html"})
    fs.readFile("node_pages/client.html",function (err,file) {
        if (err) {
            res.writeHead(404);
            res.write("FILE NOT FOUND")
        } else {
            res.write(file);
        }res.end(); 
    });
    
   
})



server_x.listen(port,function (err) {
    if (err) {
        console.log("error",err);
    }else
    {console.log("Server Running",server_x);}
    
})