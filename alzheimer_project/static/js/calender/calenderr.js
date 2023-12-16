const url_account = "https://accounts.spotify.com/api/token"
const client_id_account = "6f6a277ceb024282bd6b71a5ec18d995";
const client_secret_account = "67038f5e05ec4e13873b3cc68ff2d52d";
const data_account = new URLSearchParams();
data_account.append("grant_type", "client_credentials");
data_account.append("client_i_accountd", client_id_account);
data_account.append("client_secret", client_secret_account);

const formAction = document.querySelector(".formAction")
const formObject = document.querySelector(".formObject")
const formGame = document.querySelector(".formGame")
const formMusic = document.querySelector(".formMusic")
formObject.style.display = 'none'
formMusic.style.display = 'none'
formGame.style.display = 'none'

let error = document.querySelector(".error")

if(error.innerHTML == 'Ya hay cargada una tarea en el mismo horario.'){
  error.style.display = 'block'
  setTimeout(() => {
    error.style.display = 'none'
  }, 5000);
}

function closeWindowActivities(){
  document.querySelector(".window_day").style.display = 'none'
  document.querySelector(".window_day").innerHTML = `<div class="close_window" onclick="closeWindowActivities()">
  <span class="material-symbols-outlined close_window" style="width:50%; text-align:right; margin:auto; cursor: pointer">
    close
  </span>
</div>`
}

function clickOption(option){
  switch(option){
    case 'action':
      formAction.style.display = 'block'
      formObject.style.display = 'none'
      formGame.style.display = 'none'
      formMusic.style.display = 'none'
      break;
    case 'object':
      formAction.style.display = 'none'
      formObject.style.display = 'block'
      formGame.style.display = 'none'
      formMusic.style.display = 'none'
      break;
    case 'game':
      formAction.style.display = 'none'
      formObject.style.display = 'none'
      formGame.style.display = 'block'
      formMusic.style.display = 'none'
      break;
    case 'music':
      formAction.style.display = 'none'
      formObject.style.display = 'none'
      formGame.style.display = 'none'
      formMusic.style.display = 'block'
      break;
  }
}
  
// MUSIC
document.getElementById("id_id_music").style.display = 'none'
document.getElementById("id_category").style.display = 'none'
document.querySelector(".input_name_music").childNodes[1].setAttribute('readonly', 'true')
document.querySelector(".search_music").addEventListener("click", () => {
  open_search_music()
})

function open_search_music(){
  document.querySelector(".list_spotify").style.display = 'flex'

  fetch(url_account, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: data_account,
  })
  .then(response => response.json())
  .then(data => {
    document.querySelector(".enter_music").addEventListener('click', () => {
      value = document.querySelector(".input_music").value
      fetch(`http://127.0.0.1:8000/api/spotify/${value}`,{
      headers: {
        'Authorization': `Bearer ${data.access_token}`
      }
      })
      .then(response => response.json())
      .then(json => {
        // TRACK
        document.querySelector(".tracks").innerHTML = ''
        for(track of json["tracks"]["items"]){
          document.querySelector(".tracks").insertAdjacentHTML('beforeend', `
            <div id="${track["id"]}" class="track">
                <p style="display:none;" class="type_music">${track["type"]}</p>
                <img src="${track["album"]["images"][0].url}" width="100px">
                <div id="hola">
                  <p class="name_track">${track["name"]}</p>
                </div>
            </div>
          `)
        }
        document.querySelectorAll(".track").forEach((e) => {
          e.addEventListener("click", () => {
            document.getElementById("id_id_music").value = e.id
            document.getElementById("id_category").value = e.childNodes[1].innerHTML
            document.querySelector(".input_name_music").childNodes[1].value = e.childNodes[5].innerText
            document.querySelector(".list_spotify").style.display = 'none'
          })
        })
  
        // ARTIST
        document.querySelector(".artists").innerHTML = ''
        for(artist of json["artists"]["items"]){
          document.querySelector(".artists").insertAdjacentHTML('beforeend', `
            <div id="${artist["id"]}" class="artist">
                <p style="display:none;" class="type_music">${artist["type"]}</p>
                <img src="${artist["images"][0].url}" width="100px">
                <div>
                  <p class="name_artist">${artist["name"]}</p>
                </div>
            </div>
          `)
        }
        document.querySelectorAll(".artist").forEach((e) => {
          e.addEventListener("click", () => {
            document.getElementById("id_id_music").value = e.id
            document.getElementById("id_category").value = e.childNodes[1].innerHTML
            document.getElementById("id_name").value = e.childNodes[5].innerText
            document.querySelector(".list_spotify").style.display = 'none'
          })
        })
  
        // ALBUMS
        document.querySelector(".albums").innerHTML = ''
        for(album of json["albums"]["items"]){
          document.querySelector(".albums").insertAdjacentHTML('beforeend', `
          <div id="${album["id"]}" class="album">
            <p style="display:none;" class="type_music">${album["type"]}</p>
            <img src="${album["images"][0].url}" width="100px">
            <div>
              <p class="name_album">${album["name"]}</p>
            </div>
        </div>
          `)
        }
        document.querySelectorAll(".album").forEach((e) => {
          e.addEventListener("click", () => {
            document.getElementById("id_id_music").value = e.id
            document.getElementById("id_category").value = e.childNodes[1].innerHTML
            document.getElementById("id_name").value = e.childNodes[5].innerText
            document.querySelector(".list_spotify").style.display = 'none'
          })
        })
  
        // PLAYLISTS
        document.querySelector(".playlists").innerHTML = ''
        for(playlist of json["playlists"]["items"]){
          document.querySelector(".playlists").insertAdjacentHTML('beforeend', `
          <div id="${playlist["id"]}" class="playlist">
              <p style="display:none;" class="type_music">${playlist["type"]}</p>
              <img src="${playlist["images"][0].url}" width="100px">
              <div>
                <p class="name_playlist">${playlist["name"]}</p>
              </div>
          </div>
          `)
        }
        document.querySelectorAll(".playlist").forEach((e) => {
          e.addEventListener("click", () => {
            document.getElementById("id_id_music").value = e.id
            document.getElementById("id_category").value = e.childNodes[1].innerHTML
            document.getElementById("id_name").value = e.childNodes[5].innerText
            document.querySelector(".list_spotify").style.display = 'none'
          })
        })
      })
    })
    
  })
}



const months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];
  
const weekdays = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
  
const today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();

document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;

function renderCalendar() {
  const calendarDays = document.getElementById("calendarDays");
  calendarDays.innerHTML = "";
  const firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();
  const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

  for (let i = 0; i < firstDayOfMonth; i++) {
    const emptyDay = document.createElement("div");
    calendarDays.appendChild(emptyDay);
  }
  for (let i = 1; i <= daysInMonth; i++) {
    const day = document.createElement("div");
    day.insertAdjacentHTML("beforeend", `<p class="id_dia" name="id_dia">${i}</p>`)
    day.style.display = 'block'
    let window_day = document.querySelector(".window_day")
    fetch(`http://127.0.0.1:8000/api/activities/${document.getElementById("id_user").innerHTML}/${currentYear}/${currentMonth+1}/${i}`)
    .then(response => response.json())
    .then(json => {
      if(json.length>0){
        day.addEventListener("click", (e) => {
          window_day.style.display = 'flex'
          window_day.innerHTML = `<div class="close_window" onclick="closeWindowActivities()">
            <span class="material-symbols-outlined close_window" style="width:50%; text-align:right; margin:auto; cursor: pointer">
              close
            </span>
          </div>
          <div><p>${i} del ${currentMonth+1} del ${currentYear}</p></div>`
          for(a of json){
            if(a.id_action!=null){
              let activity = a.id_action
              window_day.insertAdjacentHTML("beforeend", `
                <div class="activity">
                  <p>${a.time}${activity.name}</p>
                  <video width="50%" height="500px" controls>
                    <source src="..${activity.video}" type="video/mp4">
                  </video>
                </div>
              `)
            } else if(a.id_music!=null){
              let activity = a.id_music
              let time = a.time
              fetch(url, {
                method: "POST",
                headers: {
                  "Content-Type": "application/x-www-form-urlencoded",
                },
                body: data,
              })
              .then(response => response.json())
              .then(data => {
                fetch(`http://127.0.0.1:8000/api/spotify/${activity.category}s/${activity.id_music}`,{
                headers: {
                  'Authorization': `Bearer ${data.access_token}`
                }
                })
                .then(response => response.json())
                .then(json => {
                  if(activity.category=='track'){
                    window_day.insertAdjacentHTML("beforeend", `
                    <div class="activity" id="${activity.id_music}">
                      <p>${time}</p>
                      <p style="display:none;">${activity.category}</p>
                      <img width="50%" src="${json["album"]["images"][0].url}">
                      <p>Escuchar:</p>
                      <p>${activity.name}</p>
                    </div>`)
                  } else {
                    window_day.insertAdjacentHTML("beforeend", `
                    <div class="music_activity" id="${activity.id_music}">
                      <p>${a.time}</p>
                      <p style="display:none;">${activity.category}</p>
                      <img width="50%" src="${json["images"][0].url}">
                      <p>Escuchar:</p>
                      <p>${activity.name}</p>
                    </div>`)
                  }
                  document.getElementById(activity.id_music).addEventListener("click", (e) => {
                    document.querySelector(".reproductor").innerHTML = ''
                    document.querySelector(".reproductor").insertAdjacentHTML('beforeend', `
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/${activity.category}/${activity.id_music}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>            
                    `)
                  })
                })
              })
                
            } else if(a.id_game!=null){
              let activity = a.id_game
              window_day.insertAdjacentHTML("beforeend", `
                <div class="activity" id=${a.id}>
                  <p>${a.time}</p>
                  <p>Jugar:</p>
                  <p>${activity.name}</p>
                </div>
              `)
              document.getElementById(a.id).addEventListener("click", (e) => {
                location.href = `../juegos/${activity.name.toLowerCase()}`
              })
            } else if(a.id_object!=null){
              activity = a.id_object
              window_day.insertAdjacentHTML("beforeend", `
                <div class="activity">
                  <p>${a.time}${activity.name}</p>
                  <img width='50%' src="..${activity.image}">
                </div>
              `)
            }
          }
        })
        day.insertAdjacentHTML('beforeend', `<span class="material-symbols-outlined">
        push_pin
        </span>`)
      }
    })
    calendarDays.appendChild(day);
  }
}


renderCalendar();

  document.getElementById("prevButton").addEventListener("click", () => {
    currentMonth -= 1;
    if (currentMonth < 0) {
      currentMonth = 11;
      currentYear -= 1;
    }
    document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;
    renderCalendar();
  });
  
  document.getElementById("nextButton").addEventListener("click", () => {
    currentMonth += 1;
    if (currentMonth > 11) {
      currentMonth = 0;
      currentYear += 1;
    }
    document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;
    renderCalendar();
  });
