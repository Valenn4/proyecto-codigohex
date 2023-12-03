setInterval(() => {
    const url = "https://accounts.spotify.com/api/token";
    const client_id = "6f6a277ceb024282bd6b71a5ec18d995";
    const client_secret = "67038f5e05ec4e13873b3cc68ff2d52d";
    const data = new URLSearchParams();
    data.append("grant_type", "client_credentials");
    data.append("client_id", client_id);
    data.append("client_secret", client_secret);

    let date = new Date()
    
    let day = date.getDate()
    let month = date.getMonth()+1
    let year = date.getFullYear()

    fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: data,
      })
      .then(response => response.json())
      .then(data => {
        fetch(`http://127.0.0.1:8000/api/activities/1/${year}/${month}/${day}`, {
            headers: {
                'Authorization': `Bearer ${data.access_token}`
            }
        })
        .then(request => request.json())
        .then(json => {
            if(json!=null){
                for(el of json){
                    if(date.getMinutes().toString().length==1){
                        if(date.getSeconds().toString().length==1){
                            if(el["time"]==`${date.getHours()}:0${date.getMinutes()}:0${date.getSeconds()}`){
                                alert("Hay una actividad para realizar")
                            }
                        } else {
                            if(el["time"]==`${date.getHours()}:0${date.getMinutes()}:${date.getSeconds()}`){
                                alert("Hay una actividad para realizar")
                            }
                        }
                    } else {
                        if(date.getSeconds().toString().length==1){
                            if(el["time"]==`${date.getHours()}:${date.getMinutes()}:0${date.getSeconds()}`){
                                alert("Hay una actividad para realizar")
                            }
                        } else {
                            if(el["time"]==`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`){
                                alert("Hay una actividad para realizar")
                            }
                        }
                    }
                }
            } else {
                console.log("mal")
            }
        })
      })
},1000);