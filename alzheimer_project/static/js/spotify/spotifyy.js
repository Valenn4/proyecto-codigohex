const url = "https://accounts.spotify.com/api/token"
const client_id = "6f6a277ceb024282bd6b71a5ec18d995";
const client_secret = "67038f5e05ec4e13873b3cc68ff2d52d";
const data = new URLSearchParams();
data.append("grant_type", "client_credentials");
data.append("client_id", client_id);
data.append("client_secret", client_secret);

document.querySelector(".search").style.display = 'none'

document.querySelector(".enter_music").addEventListener('click', (e) => {
  document.querySelector(".search").style.display = 'flex'

  e.preventDefault()
  value = document.querySelector(".input_music").value
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: data,
  })
    .then(response => response.json())
    .then(data => {
      url = `https://api.spotify.com/v1/search?q=${value}&type=album%2Cartist%2Cplaylist%2Ctrack&limit=4`

      fetch(url, {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${data.access_token}`
        }
      })
      .then(response => response.json())
      .then(data => {        
        // TRACK
        document.querySelector(".tracks").innerHTML = ''
        for(track of data["tracks"]["items"]){
          document.querySelector(".tracks").insertAdjacentHTML('beforeend', `
            <div id="${track["id"]}" class="track" style="width:20%">
                <img src="${track["album"]["images"][0].url}" width="100px">
                <div style="width:100%">
                  <p style="width:100%">${track["name"]}</p>
                </div>
            </div>
          `)
        }
        document.querySelectorAll(".track").forEach((e) => {
          e.addEventListener("click", () => {
            document.querySelector(".reproductor").innerHTML = ''
            document.querySelector(".reproductor").insertAdjacentHTML('beforeend', `
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/${e.id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>          `)
          })
        })

        // ARTIST
        document.querySelector(".artists").innerHTML = ''
        for(artist of data["artists"]["items"]){
          document.querySelector(".artists").insertAdjacentHTML('beforeend', `
            <div id="${artist["id"]}" class="artist" style="width:20%">
                <img src="${artist["images"][0].url}" width="100px">
                <div style="width:100%">
                  <p style="width:100%">${artist["name"]}</p>
                </div>
            </div>
          `)
        }
        document.querySelectorAll(".artist").forEach((e) => {
          e.addEventListener("click", () => {
            document.querySelector(".reproductor").innerHTML = ''
            document.querySelector(".reproductor").insertAdjacentHTML('beforeend', `
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/${e.id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>            `)
          })
        })

        // ALBUMS
        document.querySelector(".albums").innerHTML = ''
        for(album of data["albums"]["items"]){
          document.querySelector(".albums").insertAdjacentHTML('beforeend', `
          <div id="${album["id"]}" class="album" style="width:20%">
            <img src="${album["images"][0].url}" width="100px">
            <div style="width:100%">
              <p style="width:100%">${album["name"]}</p>
            </div>
        </div>
          `)
        }
        document.querySelectorAll(".album").forEach((e) => {
          e.addEventListener("click", () => {
            document.querySelector(".reproductor").innerHTML = ''
            document.querySelector(".reproductor").insertAdjacentHTML('beforeend', `
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/${e.id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>            `)
          })
        })

        // PLAYLISTS
        document.querySelector(".playlists").innerHTML = ''
        for(playlist of data["playlists"]["items"]){
          document.querySelector(".playlists").insertAdjacentHTML('beforeend', `
          <div id="${playlist["id"]}" class="playlist" style="width:20%">
              <img src="${playlist["images"][0].url}" width="100px">
              <div style="width:100%">
                <p style="width:100%">${playlist["name"]}</p>
              </div>
          </div>
          `)
        }
        document.querySelectorAll(".playlist").forEach((e) => {
          e.addEventListener("click", () => {
            document.querySelector(".reproductor").innerHTML = ''
            document.querySelector(".reproductor").insertAdjacentHTML('beforeend', `
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/${e.id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            `)
          })
        })
      })
      .catch(error => console.error('Error:', error));
  
    })
    .catch(error => console.error('Error:', error));
})

