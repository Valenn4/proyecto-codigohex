/*setInterval(() => {
    fetch(`http://127.0.0.1:8000/api/feeling/${document.querySelector(".id_user").innerHTML}`)
    .then(response => response.json())
    .then(json => {
        document.querySelector(".alert_feeling").style.display = 'block'
        document.querySelector(".alert_feeling").innerHTML = json["feeling"]
    })
}, 2500);
*/


let alert_activity = document.querySelector(".alert_activity")

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
                    if(date.getMinutes().toString().length==1){
                        if(date.getSeconds().toString().length==1){
                            if(el["time"]==`${date.getHours()}:0${date.getMinutes()}:0${date.getSeconds()}`){
                                alert_activity.style.display = 'block'
                                alert_activity.innerHTML = "Hay una actividad para realizar"
                                setTimeout(() => {
                                    alert_activity.innerHTML = ''
                                }, 5000);
                            }
                        } else {
                            if(el["time"]==`${date.getHours()}:0${date.getMinutes()}:${date.getSeconds()}`){
                                alert_activity.style.display = 'block'
                                alert_activity.innerHTML = "Hay una actividad para realizar"
                                setTimeout(() => {
                                    alert_activity.innerHTML = ''
                                }, 5000);
                            }
                        }
                    } else {
                        if(date.getSeconds().toString().length==1){
                            if(el["time"]==`${date.getHours()}:${date.getMinutes()}:0${date.getSeconds()}`){
                                alert_activity.style.display = 'block'
                                alert_activity.innerHTML = "Hay una actividad para realizar"
                                setTimeout(() => {
                                    alert_activity.innerHTML = ''
                                }, 5000);
                            }
                        } else {
                            if(el["time"]==`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`){
                                alert_activity.style.display = 'block'
                                alert_activity.innerHTML = "Hay una actividad para realizar"
                                setTimeout(() => {
                                    alert_activity.innerHTML = ''
                                }, 5000);
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
document.addEventListener("DOMContentLoaded", function () {
    var toggleButton = document.getElementById("toggleDropdown");
    var dropdownContent = document.getElementById("dropdownContent");
    dropdownContent.style.display = "block"

    toggleButton.addEventListener("click", function () {
        if (dropdownContent.style.display === "none" || dropdownContent.style.display === "") {
            dropdownContent.style.display = "block";
        } else {
            dropdownContent.style.display = "none";
        }
    });
});
