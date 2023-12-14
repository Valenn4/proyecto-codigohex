setInterval(() => {
    fetch(`http://127.0.0.1:8000/api/feeling/${document.querySelector(".id_user").innerHTML}`)
    .then(response => response.json())
    .then(json => {
        console.log(json)
        document.querySelector(".alert_feeling").style.display = 'flex'
        document.querySelector(".alert_feeling").innerHTML = json["feeling"]
    })
}, 100);

let alert_activityy = document.querySelector(".alert_activity")

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
        fetch(`http://127.0.0.1:8000/api/activities/${document.querySelector(".id_user").innerHTML}/${year}/${month}/${day}`, {
            headers: {
                'Authorization': `Bearer ${data.access_token}`
            }
        })
        .then(request => request.json())
        .then(json => {
            if(json!=null){
                for(el of json){
                    let type = ''
                    if (el["id_action"] != null){
                        type = "id_action"
                    } else if (el["id_object"] != null){
                        type = "id_object"
                    } else if (el["id_music"] != null){
                        type = "id_music"
                    } else {
                        type = "id_game"
                    }
                    if(el["time"]==`${date.getHours()}:${date.getMinutes()}:00`){
                        alert_activityy.style.display = 'block'
                        alert_activityy.innerHTML = ''
                        alert_activityy.insertAdjacentHTML('beforeend', `<div><p>Tienes una tarea para realizar: ${el[type].name}</p></div>
                        `)
                    }  else if (el["time"]==`0${date.getHours()}:0${date.getMinutes()}:00`){
                        alert_activityy.style.display = 'block'
                        alert_activityy.innerHTML = ''
                        alert_activityy.insertAdjacentHTML('beforeend', `<div><p>Tienes una tarea para realizar: ${el[type].name}</p></div>
                        `)
                    }else if (el["time"]==`0${date.getHours()}:${date.getMinutes()}:00`){
                        alert_activityy.style.display = 'block'
                        alert_activityy.innerHTML = ''
                        alert_activityy.insertAdjacentHTML('beforeend', `<div><p>Tienes una tarea para realizar: ${el[type].name}</p></div>
                        `)
                    }
                    
                }
            }
        })
      })
},1000);
